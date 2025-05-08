from typing import Literal
from app.interfaces.translator_interface import TranslatorInterface
from app.utils.language_normalizer import LanguageNormalizer
from deepl import Translator
import deepl
import os


SUPPORTED_LANGUAGES = ["es", "en", "pt"]

class MockTranslator(TranslatorInterface):
    def translate_to_spanish(self, text: str, source_lang: str) -> str:
        source_lang = LanguageNormalizer.normalize(source_lang)
        if source_lang == "es":
            return text
        return f"[ES from {source_lang}]: {text}"

    def translate_from_spanish(self, text: str, target_lang: Literal["es", "en", "pt"]) -> str:
        target_lang = LanguageNormalizer.normalize(target_lang)
        if target_lang == "es":
            return text
        return f"[{target_lang.upper()} from ES]: {text}"

    def translate(self, text: str, source_lang: str, target_lang: str) -> str:
        source_lang = LanguageNormalizer.normalize(source_lang)
        target_lang = LanguageNormalizer.normalize(target_lang)
        if source_lang == target_lang:
            return text
        return f"[{target_lang.upper()} from {source_lang}]: {text}"


class DeepLTranslator(TranslatorInterface):
    """
    Implementación real usando DeepL y respetando los idiomas normalizados.
    """
    LANG_MAP = {
        "es": "ES",
        "en": "EN-US",
        "pt": "PT-PT"
    }

    def __init__(self):
        self.translator = Translator(auth_key=os.getenv("DEEPL_API_KEY"))

    def translate_to_spanish(self, text: str, source_lang: str) -> str:
        try:
            print(f'Source_lang in translate_to_spanish {source_lang}')
            source_lang = LanguageNormalizer.normalize(source_lang)
            print(f'Source_lang in translate_to_spanish after {source_lang}')
            if source_lang == "es":
                return text
            
            if source_lang not in self.LANG_MAP:
                raise ValueError(f"Unsupported source_lang: {source_lang}")
            
            result = self.translator.translate_text(
                text,
                target_lang="ES"
            )
            return result.text

        except deepl.DeepLException as e:
            print("DeepL error:", str(e))
            if hasattr(e, 'response') and e.response is not None:
                print("Status code:", e.response.status_code)
                print("Response body:", e.response.text)
            raise e

    def translate_from_spanish(self, text: str, target_lang: Literal["es", "en", "pt"]) -> str:
        
        target_lang = LanguageNormalizer.normalize(target_lang)
        if target_lang == "es":
            return text
        result = self.translator.translate_text(
            text,
            target_lang=self.LANG_MAP[target_lang]
        )
        return result.text

    def translate(self, text: str, source_lang: str, target_lang: str) -> str:
        
        print(f'Source_lang in translate {source_lang}')
        
        
        source_lang = LanguageNormalizer.normalize(source_lang)
        target_lang = LanguageNormalizer.normalize(target_lang)
        if source_lang == target_lang:
            return text
        result = self.translator.translate_text(
            text,
            target_lang=self.LANG_MAP[target_lang]
        )
        return result.text
