class LanguageNormalizer:
    """
    Utility class for standardizing language codes to a limited set of supported values.

    This is useful to ensure consistency across multilingual pipelines.
    """

    @staticmethod
    def normalize(lang_code: str) -> str:
        """
        Normalizes various forms of language codes to a standard value.

        Args:
            lang_code (str): A language code string (e.g., 'ES-es', 'en-US', 'pt-BR').

        Returns:
            str: One of the normalized language codes: 'es', 'en', or 'pt'.

        Raises:
            ValueError: If the provided language is not supported.
        """
        lang_code = lang_code.lower()

        if lang_code.startswith("es"):
            return "es"
        elif lang_code.startswith("en"):
            return "en"
        elif lang_code.startswith("pt"):
            return "pt"
        else:
            raise ValueError(f"Unsupported language code: {lang_code}")
