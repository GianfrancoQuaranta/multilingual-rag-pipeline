from typing import Protocol

class PromptBuilder(Protocol):
    """
    Interface (protocol) for prompt construction modules.

    Implementations are responsible for generating the full text prompt
    to be passed to the LLM, using the retrieved context and user's question.
    """

    def build_prompt(self, context: str, question: str, language: str) -> str:
        """
        Builds a complete prompt to be sent to the LLM.

        Args:
            context (str): Text retrieved from the vector store related to the question.
            question (str): The original user question.
            language (str): Detected language of the question ('es', 'en', 'pt', etc.).

        Returns:
            str: The fully formatted prompt text for the LLM.
        """
        ...
