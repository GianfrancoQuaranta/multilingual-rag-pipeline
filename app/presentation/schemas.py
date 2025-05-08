from pydantic import BaseModel

class AskRequest(BaseModel):
    """
    Request schema for submitting a question to the system.

    Attributes:
        user_name (str): Name or identifier of the user asking the question.
        question (str): The actual question text submitted by the user.
    """
    user_name: str
    question: str

class AskResponse(BaseModel):
    """
    Response schema for returning an answer from the system.

    Attributes:
        answer (str): The generated answer to the user's question.
    """
    answer: str
