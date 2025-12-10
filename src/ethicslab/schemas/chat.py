from pydantic import BaseModel


class ChatRequest(BaseModel):
    prompt: str
    model: str = "llama2"
    stream: bool = False
