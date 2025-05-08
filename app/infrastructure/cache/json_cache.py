import os
import json
from typing import Optional, Any


class JsonCache:
    """
    A file-based JSON caching system for storing and retrieving key-value pairs.

    This class adheres to SOLID principles:
    - SRP: Responsible solely for JSON-based caching.
    - OCP: Easily extensible to support other formats (e.g., YAML) without modification.

    Attributes:
        cache_dir (str): The directory path where cache files are stored.
    """
    
    def __init__(self, cache_dir: str = "./cache"):
        """
        Initializes the cache system and creates the cache directory if it does not exist.

        Args:
            cache_dir (str): Path to the folder where JSON cache files will be stored.
        """
        try:
            self.cache_dir = cache_dir
            os.makedirs(self.cache_dir, exist_ok=True)
        except Exception as e:
            print(f"[ERROR] JsonCache.__init__: {e}")

    def _get_file_path(self, filename: str) -> str:
        """
        Constructs the full path for a given cache file.

        Args:
            filename (str): The name of the JSON file (e.g., 'questions.json').

        Returns:
            str: Absolute path to the specified cache file.
        """
        try:
            return os.path.join(self.cache_dir, filename)
        except Exception as e:
            print(f"[ERROR] JsonCache._get_file_path: {e}")
            return filename  # fallback mínimo para evitar fallos críticos

    def get(self, filename: str, key: str) -> Optional[Any]:
        """
        Retrieves a value from the specified cache file by key.

        Prints a cache hit or miss message based on key availability.

        Args:
            filename (str): Name of the cache file to read from.
            key (str): Key to retrieve from the cache.

        Returns:
            Optional[Any]: The cached value if found; otherwise, None.
        """
        try:
            file_path = self._get_file_path(filename)
            if not os.path.exists(file_path):
                print(f"[CACHE MISS] File not found: {filename}")
                return None

            with open(file_path, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    print(f"[ERROR] JsonCache.get: Corrupted cache file: {filename}")
                    return None

            if key in data:
                print(f"[CACHE HIT] {filename} => {key}")
            else:
                print(f"[CACHE MISS] {filename} => {key}")

            return data.get(key)
        except Exception as e:
            print(f"[ERROR] JsonCache.get: {e}")
            return None

    def set(self, filename: str, key: str, value: Any) -> None:
        """
        Stores a key-value pair in the specified cache file.

        If the file does not exist, it is created. If it exists but is unreadable,
        it will be overwritten with a new structure.

        Args:
            filename (str): Name of the cache file to write to.
            key (str): The key under which the value will be stored.
            value (Any): The value to store.
        """
        try:
            file_path = self._get_file_path(filename)
            data = {}

            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as f:
                    try:
                        data = json.load(f)
                    except json.JSONDecodeError:
                        print(f"[WARN] JsonCache.set: Corrupted file: {filename}. Overwriting.")

            data[key] = value

            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

            print(f"[CACHE WRITE] {filename} => {key}")
        except Exception as e:
            print(f"[ERROR] JsonCache.set: {e}")