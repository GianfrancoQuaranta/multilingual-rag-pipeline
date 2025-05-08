import chromadb
from app.interfaces.vector_store_interface import VectorStore

class ChromaVectorStore(VectorStore):
    """
    Vector store implementation using ChromaDB as the persistent backend.

    This class allows saving and querying document chunks and their embeddings,
    and provides an interface to count stored vectors.
    """

    def __init__(self):
        """
        Initializes the ChromaDB client and loads (or creates) the collection named 'documentos'.
        The data is persisted in the 'data/chroma_db' directory.

        Raises:
            Exception: If ChromaDB fails to initialize or access the collection.
        """
        try:
            self.client = chromadb.PersistentClient(path="data/chroma_db")
            self.collection = self.client.get_or_create_collection(name="documentos")
        except Exception as e:
            raise RuntimeError(f"❌ Failed to initialize ChromaDB: {e}")

    def save(self, chunks: list[str], embeddings: list[list[float]]) -> None:
        """
        Saves a list of text chunks and their corresponding embeddings to the Chroma collection.

        Args:
            chunks (list[str]): List of text chunks to store.
            embeddings (list[list[float]]): Corresponding list of embedding vectors.

        Logs:
            Prints an error message for each failed chunk insertion.
        """
        for i, (chunk, vector) in enumerate(zip(chunks, embeddings)):
            try:
                self.collection.add(
                    documents=[chunk],
                    embeddings=[vector],
                    ids=[f"doc_{i}"]
                )
            except Exception as e:
                print(f"❌ Failed to store chunk {i}: {e}")

    def search(self, query_vector: list[float], top_k: int) -> dict:
        """
        Searches the vector store for the most similar documents to a given embedding.

        Args:
            query_vector (list[float]): The embedding vector to query with.
            top_k (int): The number of top results to return.

        Returns:
            dict: A dictionary containing the search results.
        """
        try:
            return self.collection.query(
                query_embeddings=[query_vector],
                n_results=top_k
            )
        except Exception as e:
            print(f"❌ Failed to perform vector search: {e}")
            return {}

    def count(self) -> int:
        """
        Returns the number of documents stored in the Chroma collection.

        Returns:
            int: The number of stored vectors.

        Raises:
            RuntimeError: If the count operation fails unexpectedly.
        """
        try:
            return self.collection.count()
        except Exception as e:
            raise RuntimeError(f"❌ Failed to count documents in Chroma collection: {e}")
