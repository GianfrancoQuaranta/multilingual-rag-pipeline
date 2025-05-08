from app.domain.rag_pipeline import run_rag_pipeline

def test_rag_pipeline_integration():
    """
    Integration test for the RAG pipeline.

    Simulates a user asking a question and verifies that the pipeline
    produces an expected answer containing a reference to the 'magic flower'.
    """
    # Simulated user input
    question = "¿Cuál es el nombre de la flor mágica?"
    user_name = "Tester"

    # Run the RAG pipeline
    response = run_rag_pipeline(question, user_name)

    # Output the generated response for visual inspection (optional)
    print("Generated response:\n", response)

    # Assert that expected keywords appear in the response
    assert "flor" in response.lower() or "Luz de Luna" in response, "❌ Expected flower not mentioned in response"
