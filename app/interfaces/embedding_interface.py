from typing import Protocol
from abc import abstractmethod

class EmbeddingProvider(Protocol):
    """
    Interface (protocol) for any embedding provider implementation.

    Implementing classes must provide a method to convert a list of texts
    into their corresponding list of vector embeddings.
    """

    @abstractmethod
    def get_embeddings(self, texts: list[str]) -> list[list[float]]:
        """
        Takes a list of input texts and returns a list of embedding vectors.

        Args:
            texts (list[str]): List of input text strings.

        Returns:
            list[list[float]]: A list of embeddings, one per input text.
        """
        ...
