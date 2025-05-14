# === Imports ===
from app.infrastructure.file_loader import load_text_file
from app.infrastructure.chunker import chunk_text
from app.infrastructure.translator import DeepLTranslator 
from app.infrastructure.cache.json_cache import JsonCache

from app.adapters.embedding_provider import CohereEmbedder
from app.adapters.vector_store import ChromaVectorStore
from app.adapters.llm_client import CohereChatClient
from app.adapters.default_prompt_builder import DefaultPromptBuilder
from app.adapters.cache_manager import CacheManager
from app.adapters.langdetect_adapter import LangDetectAdapter

from app.interfaces.embedding_interface import EmbeddingProvider
from app.interfaces.vector_store_interface import VectorStore
from app.interfaces.prompt_interface import PromptBuilder

from app.utils.hashing import stable_hash

from app.domain.validation_rules import ValidationRules

from dotenv import load_dotenv
import os

# === Globals ===
_index_checked = False  # Prevent reindexing multiple times

# === Document Indexing ===
def prepare_index_if_needed():
    global _index_checked
    if _index_checked:
        return
    _index_checked = True

    vector_store = ChromaVectorStore()

    if vector_store.count() > 0:
        print("📦 Vector store already has embeddings. Skipping indexing.")
        return

    print("🧱 Indexing document...")
    text = load_text_file("data/documento.docx")
    chunks = chunk_text(text)
    embedder = CohereEmbedder()
    embeddings = embedder.get_embeddings(chunks)
    vector_store.save(chunks, embeddings)
    print("✅ Indexing complete.")

# === RAG Pipeline ===
async def run_rag_pipeline(question: str, user_name: str) -> str:
    
    load_dotenv()  # Carga las variables del .env

    # api_key = os.getenv("COHERE_API_KEY")
            
    # print('apikey', api_key)
    
    prepare_index_if_needed()

    # 1. Initialize dependencies
    cache = CacheManager(JsonCache("./cache"))
    translator = DeepLTranslator()
    detector = LangDetectAdapter()
    prompt_builder: PromptBuilder = DefaultPromptBuilder()

    # 2. Generate stable ID for the question
    question_id = stable_hash(question)

    # 3. Detect language
    lang = await detector.detect(question)
    print(f"🌐 Detected language: {lang}")

    # 4. Check cached response
    cached_response = cache.get_response(question_id)
    if cached_response:
        print(f'cached_response: {cached_response}')
        print(f'(🔁 from cache)...')
        return f"{user_name} preguntó: '{question}' 🤖, respuesta: {cached_response}"

    # 5. Translate question to Spanish for embedding
    translated_question = cache.get_translated_question(question_id)
    print(f'translated_question: {translated_question}')

    if not translated_question:
        print(f'No translated_question... translating')
        translated_question = translator.translate_to_spanish(question, lang)
        print(f'translated_question: {translated_question}')
        cache.store_translated_question(question_id, translated_question)
        print(f'store_translated_question correct.')

    # 6. Embed translated question
    embedder: EmbeddingProvider = CohereEmbedder()
    question_vector = embedder.get_embeddings([translated_question])[0]

    # 7. Semantic search in vector store
    vector_store: VectorStore = ChromaVectorStore()
    result = vector_store.search(question_vector, top_k=1)
    context_es = result["documents"][0][0] if result["documents"] and result["documents"][0] else ""
    print(f'context: {context_es}')

    # 8. Translate context back to original language
    translated_context = cache.get_translated_context(question_id)
    print('translated_context cached: {translated_context}')

    if not translated_context:
        translated_context = translator.translate_from_spanish(context_es, lang)
        print('translated_context translated: {translated_context}')
        cache.store_translated_context(question_id, translated_context)
        print(f'store_translated_context correct.')

    # 9. Prompt generation
    prompt = cache.get_prompt(question_id)
    if not prompt:
        print(f'No cached prompt..')
        prompt = await prompt_builder.build_prompt(context=translated_context, question=question, language=lang)
        print(f'Prompt: {prompt}')
        cache.store_prompt(question_id, prompt)
        print(f'store_prompt correct.')

    # 10. Call to LLM
    llm = CohereChatClient()
    response = await llm.generate(prompt)
    print(f"🔄 response: {response['text']}")

    # 11. Validation loop with feedback
    validator = ValidationRules(expected_lang=lang)
    MAX_RETRIES = 2
    attempts = 0
    valid = validator.validate(response)
    invalid_responses = []

    while not valid and attempts <= MAX_RETRIES:
        print(f"⚠️ Attempt {attempts+1}: invalid response. Retrying...")
        invalid_responses.append(response)

        _, feedback_messages = validator.validate_with_feedback(response)
        feedback_block = "\n".join(translator.translate(text, "es", lang) for text in feedback_messages)

        prompt = await prompt_builder.build_prompt(
            context=translated_context,
            question=question,
            language=lang,
            extra_instructions=feedback_block
        )
        response = await llm.generate(prompt)
        valid = validator.validate(response)
        attempts += 1

    if not valid:
        invalid_responses.append(response)
        print("❌ Max retries exceeded. Invalid responses:")
        for idx, r in enumerate(invalid_responses):
            print(f"\n🔁 Attempt {idx+1}:")
            print(r)
        return f"⚠️ No valid response generated for question: '{question}'"

    # 12. Cache final response
    cache.store_response(question_id, response['text'])

    # 13. Return final response
    return f"{user_name} preguntó: '{question}' 🤖, respuesta: {response['text']}"




