from fastapi import FastAPI
from pydantic import BaseModel

from rag import ask_rag


app = FastAPI(
    title="Azure AI RAG API",
    description="Dockerized RAG application using Azure OpenAI and Azure AI Search"
)


class Question(BaseModel):
    question: str


@app.get("/")
def home():

    return {
        "message": "Azure AI RAG application is running"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


@app.post("/ask")
def ask(question: Question):

    result = ask_rag(question.question)

    return result