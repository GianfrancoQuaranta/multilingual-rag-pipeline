from app.interfaces.language_detector import LanguageDetectorInterface
from deepl import Translator
import os

# Custom exception to handle unsupported languages
class UnsupportedLanguageError(Exception):
    pass

class DeepLLanguageDetectorAdapter(LanguageDetectorInterface):
    """
    Adapter for language detection using the DeepL API.

    Implements the LanguageDetectorInterface to provide language detection
    functionality, returning simplified language codes (es, en, pt).
    """

    def __init__(self):
        """
        Initializes the DeepL Translator with the API key from environment variables.
        """
        self.translator = Translator(auth_key=os.getenv("DEEPL_API_KEY"))

    def detect(self, text: str) -> str:
        """
        Detects the language of the input text using DeepL and maps it to a simplified code.

        Args:
            text (str): The input text to detect language for.

        Returns:
            str: The detected language code ('es', 'en', 'pt').

        Raises:
            UnsupportedLanguageError: If the language is not supported or detection fails.
        """
        try:
            result = self.translator.detect_language(text)
            lang = result.language.lower()

            if lang.startswith('es'):
                return 'es'
            elif lang.startswith('pt'):
                return 'pt'
            elif lang.startswith('en'):
                return 'en'
            else:
                # Raise error if language is not one of the supported ones
                raise UnsupportedLanguageError(f"Unsupported language: {lang}")

        except Exception as e:
            # Raise custom exception in case of failure in the detection process
            raise UnsupportedLanguageError(f"Failed to detect language: {e}")
