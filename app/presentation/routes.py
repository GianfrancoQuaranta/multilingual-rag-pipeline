from fastapi import Body
from fastapi import APIRouter

from app.presentation.schemas import AskRequest, AskResponse
from app.domain.rag_pipeline import run_rag_pipeline

# Create an instance of the FastAPI router
router = APIRouter()

@router.get("/")
def home():
    """
    Root route for the API.

    Returns:
        str: Welcome message indicating how to use the service.
    """
    return 'You are in the project home, if you want to ask go to /ask.'

@router.post("/ask", response_model=AskResponse)
async def ask(request: AskRequest = Body(...)):
    """
    Endpoint to handle user questions using the RAG pipeline.

    Args:
        request (AskRequest): The request body containing user_name and question.

    Returns:
        AskResponse: The generated answer from the pipeline.
    """
    # Run the main retrieval-augmented generation pipeline
    answer = await run_rag_pipeline(request.question, request.user_name)

    return AskResponse(answer=answer)
