from abc import ABC, abstractmethod
from typing import Literal

class TranslatorInterface(ABC):
    """
    Abstract base class for translation service implementations.

    Any concrete class must provide methods to translate text
    to and from Spanish, and also perform generic language translation.
    """

    @abstractmethod
    def translate_to_spanish(self, text: str, source_lang: str) -> str:
        """
        Translates the given text from the specified source language into Spanish.

        Args:
            text (str): The text to translate.
            source_lang (str): The language code of the source text.

        Returns:
            str: The translated text in Spanish.
        """
        pass

    @abstractmethod
    def translate_from_spanish(self, text: str, target_lang: Literal["es", "en", "pt"]) -> str:
        """
        Translates the given Spanish text into the specified target language.

        Args:
            text (str): The Spanish source text.
            target_lang (Literal["es", "en", "pt"]): The desired output language.

        Returns:
            str: The translated text.
        """
        pass

    @abstractmethod
    def translate(self, text: str, source_lang: str, target_lang: str) -> str:
        """
        Translates text from the source language into the target language.

        Args:
            text (str): The text to translate.
            source_lang (str): The language code of the input text.
            target_lang (str): The language code to translate the text into.

        Returns:
            str: The translated output text.
        """
        pass
