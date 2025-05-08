from app.interfaces.prompt_interface import PromptBuilder
from app.adapters.langdetect_adapter import LangDetectAdapter

class DefaultPromptBuilder(PromptBuilder):
    """
    Default implementation of the PromptBuilder interface.

    This class is responsible for building a multilingual prompt based on the context,
    the user's question, the target language, and optional extra instructions.
    It uses a language detector to verify the context and instruction languages.
    """
    
    def __init__(self):
        # Initialize the language detector adapter
        self.detector = LangDetectAdapter()

    async def build_prompt(self, context: str, question: str, language: str, extra_instructions: str = "") -> str:
        """
        Builds a prompt using the provided context, question, and language, enriched with 
        predefined instructions and optional extra instructions.

        Args:
            context (str): The context to use in the prompt.
            question (str): The user’s question.
            language (str): The target language code ('es', 'en', 'pt').
            extra_instructions (str, optional): Additional instructions to append to the prompt.

        Returns:
            str: The fully constructed prompt.
        """
        print('build_prompt.. language received', language)

        # Detect language of the provided context
        context_lang = await self.detector.detect(context)
        print('build_prompt.. context language received', context_lang)

        # Language-specific base instructions
        instructions = {
            "es": (
                "Respondé en una sola oración, en tercera persona, con emojis y en español.\n"
                "El idioma de la respuesta debe ser español.\n"
                "Debe responder siempre exactamente lo mismo si la pregunta es la misma.\n"
                "No agregues contenido aleatorio, ni emojis aleatorios.\n"
                "Usá solo emojis relevantes al contenido.\n"
            ),
            "en": (
                "Respond in one sentence, third person, with emojis, in English.\n"
                "The response must be in English.\n"
                "It must always be exactly the same for the same question.\n"
                "Do not include randomness or random emojis.\n"
                "Only use emojis relevant to the content.\n"
            ),
            "pt": (
                "Responda em uma única frase, na terceira pessoa, com emojis e em português.\n"
                "A resposta deve estar em português.\n"
                "Deve responder sempre exatamente o mesmo para a mesma pergunta.\n"
                "Não inclua elementos aleatórios ou emojis aleatórios.\n"
                "Use apenas emojis relevantes ao conteúdo.\n"
            )
        }

        # Fallback to English if language is not recognized
        instruction = instructions.get(language, instructions["en"])

        # Detect language of the instruction block
        instruction_lang = await self.detector.detect(instruction)
        print(f"build_prompt.. instruction language received {instruction_lang}")

        # Append any extra instructions provided by the user
        if extra_instructions:
            instruction = f"{instruction}\n{extra_instructions.strip()}"

        # Final prompt composition
        return f"""
{instruction}

Contexto: {context}

Pregunta: {question}
"""