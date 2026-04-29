from fastapi import FastAPI
from pydantic import BaseModel
from agent import process_chat

app = FastAPI()

class ChatInput(BaseModel):
    message: str

@app.post("/chat-log")
def chat_log(input: ChatInput):
    result = process_chat(input.message)
    return result