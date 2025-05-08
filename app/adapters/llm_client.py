import os
import cohere
from dotenv import load_dotenv
from app.adapters.langdetect_adapter import LangDetectAdapter

# Load environment variables from .env file (override existing ones if needed)
load_dotenv(override=True)

class CohereChatClient:
    """
    A chat client that interfaces with Cohere's generate API and performs
    automatic language detection for both input prompts and model responses.
    """

    def __init__(self) -> None:
        """
        Initializes the Cohere client and the language detector.

        Raises:
            ValueError: If the COHERE_API_KEY is not set in environment variables.
            ConnectionError: If the API health check fails.
        """
        api_key = os.getenv("COHERE_API_KEY")
        if not api_key:
            raise ValueError("❌ Environment variable COHERE_API_KEY not found.")

        self.client = cohere.Client(api_key)
        self.detector = LangDetectAdapter()

        # API connection check using a lightweight tokenize call
        try:
            self.client.tokenize(text="ping", model="embed-multilingual-v3.0")
        except Exception as e:
            raise ConnectionError(f"❌ Failed to connect to Cohere API: {e}")

    async def generate(self, prompt: str) -> dict:
        """
        Generates a response using Cohere's chat model based on the provided prompt.
        Also detects the language of both the input and the output.

        Args:
            prompt (str): The input prompt to send to the language model.

        Returns:
            dict: A dictionary with the response text and its detected language.

        Raises:
            RuntimeError: If the call to the Cohere generate API fails.
        """
        # Detect the language of the prompt (input)
        prompt_lang = await self.detector.detect(prompt)
        print("📥 detected language in CohereChat PROMPT:", prompt_lang)

        try:
            # Call the Cohere text generation endpoint
            response = self.client.generate(
                model="command-r-plus",
                prompt=prompt,
                max_tokens=80,
                temperature=0.0
            )
        except Exception as e:
            raise RuntimeError(f"❌ Failed to generate response with Cohere: {e}")

        # Clean the output and get the result
        text = response.generations[0].text.strip()

        # Detect the language of the response (output)
        response_lang = await self.detector.detect(text)
        print("📤 detected language in CohereChat RESPONSE:", response_lang, "\n")

        return {
            "text": text,
            "lang": response_lang
        }
