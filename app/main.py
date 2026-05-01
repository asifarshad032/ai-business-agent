from fastapi import FastAPI
from pydantic import BaseModel
from app.ai_agent import chat_with_ai

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "AI Business Agent Running 🚀"}

@app.post("/chat")
def chat(req: ChatRequest):
    response = chat_with_ai(req.message)
    return {"response": response}