from fastapi import FastAPI
from app.presentation.routes import router

app = FastAPI(title='RAG API')

app.include_router(router)