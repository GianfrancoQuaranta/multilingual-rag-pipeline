import cohere
import os
from dotenv import load_dotenv
from app.interfaces.embedding_interface import EmbeddingProvider

# Load environment variables from .env file
load_dotenv()

class CohereEmbedder(EmbeddingProvider):
    """
    Embedding provider that uses Cohere's multilingual model to generate vector embeddings.

    Implements the EmbeddingProvider interface to integrate into the RAG pipeline.
    """

    def __init__(self):
        """
        Initializes the Cohere client using the COHERE_API_KEY from environment variables.

        Raises:
            ValueError: If the API key is not found in the environment.
        """
        api_key = os.getenv("COHERE_API_KEY")
        if not api_key:
            raise ValueError("❌ Cohere API key (COHERE_API_KEY) not found in environment variables")
        
        self.client = cohere.Client(api_key)

    def get_embeddings(self, texts: list[str]) -> list[list[float]]:
        """
        Generates multilingual embeddings for a list of input texts using Cohere.

        Args:
            texts (list[str]): The list of text strings to embed.

        Returns:
            list[list[float]]: A list of embedding vectors for the input texts.

        Raises:
            RuntimeError: If the embedding request to Cohere fails.
        """
        try:
            response = self.client.embed(
                texts=texts,
                model="embed-multilingual-v3.0",
                input_type="search_document"
            )
            return response.embeddings
        
        except Exception as e:
            # Raise a RuntimeError to indicate the failure, with original exception details
            raise RuntimeError(f"❌ Failed to generate embeddings with Cohere: {e}")
