import re
from typing import List, Tuple, Dict, Union
from app.interfaces.language_detector import LanguageDetectorInterface
from app.adapters.langdetect_adapter import LangDetectAdapter

# Regex to detect any emoji character (covers most Unicode emojis)
EMOJI_REGEX = re.compile("[\U00010000-\U0010FFFF]", flags=re.UNICODE)

class EmojiValidator:
    # Checks if there's at least one emoji in the string
    def is_valid(self, text: str) -> bool:
        try:
            return bool(EMOJI_REGEX.search(text))
        except Exception as e:
            print(f"[EmojiValidator ERROR] {e}")
            return False

    def error_message(self) -> str:
        return "La respuesta debe contener al menos un emoji."


class SentenceValidator:
    # Validates if the text is a single sentence (no newline, max 1 period)
    def is_valid(self, text: str) -> bool:
        try:
            return text.count(".") <= 1 and "\n" not in text
        except Exception as e:
            print(f"[SentenceValidator ERROR] {e}")
            return False

    def error_message(self) -> str:
        return "La respuesta debe estar redactada en una sola oración."


class LanguageValidator:
    # Validates if the detected language matches the expected language
    def __init__(self, expected_lang: str):
        self.expected_lang = expected_lang

    def is_valid(self, detected_lang: str) -> bool:
        try:
            print(f"🧪 Detected lang: {detected_lang} | Expected: {self.expected_lang}")
            return detected_lang == self.expected_lang
        except Exception as e:
            print(f"[LanguageValidator ERROR] {e}")
            return False

    def error_message(self) -> str:
        return f"La respuesta debe estar completamente en {self.expected_lang.upper()}."


class ValidationRules:
    """
    Applies multiple validation rules to a response dict.
    Each response is expected to contain 'text' and 'lang' keys.
    """
    def __init__(self, expected_lang: str):
        self.emoji_validator = EmojiValidator()
        self.sentence_validator = SentenceValidator()
        self.language_validator = LanguageValidator(expected_lang)

    def validate(self, response: Union[Dict[str, str], str]) -> bool:
        try:
            # If the response is a string, assume it's plain text, wrap into dict for compatibility
            if isinstance(response, str):
                response = {"text": response, "lang": self.language_validator.expected_lang}

            text = response.get("text", "")
            lang = response.get("lang", "")

            return (
                self.emoji_validator.is_valid(text)
                and self.sentence_validator.is_valid(text)
                and self.language_validator.is_valid(lang)
            )
        except Exception as e:
            print(f"[ValidationRules.validate ERROR] {e}")
            return False

    def validate_with_feedback(self, response: Union[Dict[str, str], str]) -> Tuple[bool, List[str]]:
        errors = []
        try:
            if isinstance(response, str):
                response = {"text": response, "lang": self.language_validator.expected_lang}

            text = response.get("text", "")
            lang = response.get("lang", "")

            if not self.emoji_validator.is_valid(text):
                errors.append(self.emoji_validator.error_message())

            if not self.sentence_validator.is_valid(text):
                errors.append(self.sentence_validator.error_message())

            if not self.language_validator.is_valid(lang):
                errors.append(self.language_validator.error_message())

        except Exception as e:
            print(f"[ValidationRules.validate_with_feedback ERROR] {e}")
            errors.append(f"Error inesperado: {e}")

        return len(errors) == 0, errors
