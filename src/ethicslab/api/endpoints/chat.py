from fastapi import APIRouter

from src.ethicslab.schemas.chat import ChatRequest
from src.ethicslab.services.ollama import generate_response

router = APIRouter()


@router.post("/")
async def chat(request: ChatRequest):
    response = await generate_response(
        prompt=request.prompt,
        model=request.model,
        stream=request.stream
    )
    return {"response": response}
