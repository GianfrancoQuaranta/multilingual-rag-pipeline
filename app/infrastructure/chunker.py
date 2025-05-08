from typing import List

def chunk_text(text: str) -> List[str]:
    """
    Splits the input text into chunks based on paragraphs.
    Each paragraph is treated as an independent unit.

    Args:
        text (str): The full input text.

    Returns:
        List[str]: A list of cleaned paragraphs as chunks.

    Raises:
        ValueError: If the input is not a string.
    """
    try:
        if not isinstance(text, str):
            raise ValueError("Input must be a string.")

        # Strip each paragraph and remove empty lines
        paragraphs = [p.strip() for p in text.split('\n') if p.strip()]
        return paragraphs

    except Exception as e:
        print(f"❌ Error while chunking text: {e}")
        return []
