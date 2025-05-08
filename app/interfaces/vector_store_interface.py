from typing import Protocol
from abc import abstractmethod

class VectorStore(Protocol):
    """
    Interface (protocol) for vector store implementations.

    Defines the required methods for saving vectors, performing similarity search,
    and retrieving the current document count from the store.
    """

    @abstractmethod
    def save(self, chunks: list[str], embeddings: list[list[float]]) -> None:
        """
        Stores text chunks and their corresponding embedding vectors in the vector store.

        Args:
            chunks (list[str]): List of text segments or documents.
            embeddings (list[list[float]]): Corresponding list of embedding vectors.
        """
        ...

    @abstractmethod
    def search(self, query_vector: list[float], top_k: int) -> dict:
        """
        Searches for the most similar documents to a given query vector.

        Args:
            query_vector (list[float]): The vector to search against the vector store.
            top_k (int): Number of top results to return.

        Returns:
            dict: A dictionary containing the closest matching documents and metadata.
        """
        ...

    @abstractmethod
    def count(self) -> int:
        """
        Returns the number of documents currently stored in the vector store.

        Returns:
            int: Total number of stored entries.
        """
        ...
