from fastapi import FastAPI
from pydantic import BaseModel

from chatbot import ask_chatbot


app = FastAPI(
    title="AI FAQ Chatbot API",
    description="RAG-based college FAQ chatbot"
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "AI FAQ Chatbot API is running"
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):

    answer = ask_chatbot(request.question)

    return {
        "question": request.question,
        "answer": answer
    }