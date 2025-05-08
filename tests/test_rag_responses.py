import pytest
from app.domain.rag_pipeline import run_rag_pipeline
from app.domain.validation_rules import ValidationRules
import os
import glob

# List of test questions and their expected language
test_questions = [
    ("¿Quién es Zara?", "es"),
    ("¿Cómo se llama la flor mágica?", "es"),
    ("¿Qué decidió hacer Emma?", "es"),
    ("¿Cuál es el poder de la flor \"Luz de Luna\"?", "es"),
    ("¿Quién es \"Sombra Silenciosa\"?", "es"),

    ("Who is Zara?", "en"),
    ("What did Emma decide to do?", "en"),
    ("What is the name of the magical flower?", "en"),
    ("What power does the “Moonlight” flower have?", "en"),
    ("Who is the Silent Shadow?", "en"),

    ("Quem é Zara?", "pt"),
    ("Qual é o nome da flor mágica?", "pt"),
    ("O que Emma decidiu fazer?", "pt"),
    ("Quem é a Sombra Silenciosa?", "pt"),
    ("Qual é o poder da flor \"Luz da Lua\"?", "pt")
]

CACHE_DIR = "./cache"

# Fixture to clean the cache directory before each test
@pytest.fixture(autouse=True)
def clear_cache_files():
    """
    Clears all .json files from the cache directory before each test run.
    Ensures tests start with a clean slate and no cached responses.
    """
    if os.path.exists(CACHE_DIR) and os.path.isdir(CACHE_DIR):
        for file_path in glob.glob(os.path.join(CACHE_DIR, "*.json")):
            try:
                os.remove(file_path)
            except Exception as e:
                print(f"⚠️ Error deleting {file_path}: {e}")
        print("🧹 Cache cleared. Ready to run test.")

# Regression and determinism test with language validation
@pytest.mark.asyncio
@pytest.mark.parametrize("question,lang", test_questions)
async def test_rag_pipeline_respuestas_deterministas(question: str, lang: str):
    """
    This test checks that the RAG pipeline:
    - Returns consistent (deterministic) answers for the same question.
    - Produces a response that passes language-specific validation rules.
    """
    user = "TestUser"
    print("\n\n \033[95m-------------------------------------- LINE OF SEPARATION --------------------------------------\033[0m")
    print(f"\n🌐 Testing question: {question} [{lang}]")

    # First pipeline run
    respuesta_1 = await run_rag_pipeline(question, user)
    print(f'respuesta_1: {respuesta_1}')

    # Second pipeline run (should be identical)
    respuesta_2 = await run_rag_pipeline(question, user)
    print(f'respuesta_2: {respuesta_2}')

    # Ensure deterministic output
    assert respuesta_1 == respuesta_2, f"❌ Response is not deterministic for: {question}"

    # Validate language-specific rules
    validador = ValidationRules(expected_lang=lang)
    assert validador.validate(respuesta_1), f"❌ Response does not meet language rules: {respuesta_1}"
