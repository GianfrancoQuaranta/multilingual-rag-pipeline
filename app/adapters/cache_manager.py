from app.infrastructure.cache.json_cache import JsonCache
from typing import Optional

class CacheManager:
    def __init__(self, cache: JsonCache):
        """
        Initializes the CacheManager with a JsonCache instance
        and sets up a mapping for various cache file types.
        """
        try:
            self.cache = cache
            self.files = {
                "translated_questions": "translated_questions.json",
                "translated_contexts": "translated_contexts.json",
                "prompts": "prompts.json",
                "responses": "responses.json"
            }
        except Exception as e:
            print(f"[ERROR] CacheManager.__init__: {e}")

    def get_translated_question(self, question_id: str) -> Optional[str]:
        """Retrieves a translated question from the cache."""
        try:
            return self.cache.get(self.files["translated_questions"], question_id)
        except Exception as e:
            print(f"[ERROR] CacheManager.get_translated_question: {e}")
            return None

    def store_translated_question(self, question_id: str, translated: str) -> None:
        """Stores a translated question in the cache."""
        try:
            self.cache.set(self.files["translated_questions"], question_id, translated)
        except Exception as e:
            print(f"[ERROR] CacheManager.store_translated_question: {e}")

    def get_translated_context(self, question_id: str) -> Optional[str]:
        """Retrieves a translated context from the cache."""
        try:
            return self.cache.get(self.files["translated_contexts"], question_id)
        except Exception as e:
            print(f"[ERROR] CacheManager.get_translated_context: {e}")
            return None

    def store_translated_context(self, question_id: str, translated: str) -> None:
        """Stores a translated context in the cache."""
        try:
            self.cache.set(self.files["translated_contexts"], question_id, translated)
        except Exception as e:
            print(f"[ERROR] CacheManager.store_translated_context: {e}")

    def get_prompt(self, question_id: str) -> Optional[str]:
        """Retrieves a prompt from the cache."""
        try:
            return self.cache.get(self.files["prompts"], question_id)
        except Exception as e:
            print(f"[ERROR] CacheManager.get_prompt: {e}")
            return None

    def store_prompt(self, question_id: str, prompt: str) -> None:
        """Stores a prompt in the cache."""
        try:
            self.cache.set(self.files["prompts"], question_id, prompt)
        except Exception as e:
            print(f"[ERROR] CacheManager.store_prompt: {e}")

    def get_response(self, question_id: str) -> Optional[str]:
        """Retrieves a generated response from the cache."""
        try:
            return self.cache.get(self.files["responses"], question_id)
        except Exception as e:
            print(f"[ERROR] CacheManager.get_response: {e}")
            return None

    def store_response(self, question_id: str, response: str) -> None:
        """Stores a generated response in the cache."""
        try:
            self.cache.set(self.files["responses"], question_id, response)
        except Exception as e:
            print(f"[ERROR] CacheManager.store_response: {e}")
