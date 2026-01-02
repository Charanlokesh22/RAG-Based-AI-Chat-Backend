from fastapi import APIRouter
from pydantic import BaseModel
from app.services.rag import rag_query

router = APIRouter()

class ChatRequest(BaseModel):
    question: str

@router.post("/chat")
def chat(request: ChatRequest):
    answer = rag_query(request.question)
    return {"answer": answer}
