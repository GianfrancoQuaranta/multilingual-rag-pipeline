from abc import ABC, abstractmethod

class LanguageDetectorInterface(ABC):
    """
    Abstract base class for language detection providers.

    Any implementation must define a `detect` method that returns the language
    code of a given text input.
    """

    @abstractmethod
    def detect(self, text: str) -> str:
        """
        Detects the language of the given text.

        Args:
            text (str): The input text whose language is to be detected.

        Returns:
            str: A simplified language code (e.g., 'en', 'es', 'pt').
        """
        pass
