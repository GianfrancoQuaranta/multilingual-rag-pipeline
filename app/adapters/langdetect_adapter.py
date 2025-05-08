from app.interfaces.language_detector import LanguageDetectorInterface
from deepl import Translator as DeepLTranslator
import asyncio
import os

# Custom exception for unsupported or undetectable languages
class UnsupportedLanguageError(Exception):
    pass

class LangDetectAdapter(LanguageDetectorInterface):
    """
    Language detection adapter using the DeepL translation API.

    Implements the LanguageDetectorInterface and supports asynchronous language detection
    for multilingual text inputs.
    """

    def __init__(self):
        """
        Initializes the DeepL translator with the API key from environment variables.

        Raises:
            ValueError: If the DEEPL_API_KEY is not found in the environment.
        """
        api_key = os.getenv("DEEPL_API_KEY")
        if not api_key:
            raise ValueError("❌ Environment variable DEEPL_API_KEY not found.")
        
        self.translator = DeepLTranslator(api_key)

    async def detect(self, text: str) -> str:
        """
        Asynchronously detects the language of the provided text using DeepL.

        Args:
            text (str): The input text to analyze.

        Returns:
            str: A simplified language code: 'es', 'en', or 'pt'.

        Raises:
            UnsupportedLanguageError: If the detected language is not supported.
        """
        loop = asyncio.get_event_loop()

        def detect_language():
            # Use DeepL's translate_text to detect source language
            result = self.translator.translate_text(text, target_lang="ES")
            return result.detected_source_lang.lower()

        try:
            # Run the detection function in a separate thread (non-blocking)
            lang = await loop.run_in_executor(None, detect_language)
        except Exception as e:
            raise UnsupportedLanguageError(f"❌ Language detection failed: {e}")

        # Normalize and map detected language to supported codes
        if lang.startswith('es') or lang in ['ca', 'gl']:
            return 'es'
        elif lang.startswith('pt'):
            return 'pt'
        elif lang.startswith('en'):
            return 'en'
        else:
            raise UnsupportedLanguageError(f"❌ Unsupported language detected: {lang}")
