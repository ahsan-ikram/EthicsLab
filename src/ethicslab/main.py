import json
import uuid
from datetime import datetime

import httpx
# import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.ethicslab.model import Tweeter, TweeterFactory

app = FastAPI()
tweeter: Tweeter = TweeterFactory.create_instance()


class ChatRequest(BaseModel):
    prompt: str
    model: str = "llama2"
    stream: bool = False


@app.get("/")
async def root():
    return {"message": "Welcome to Ethics Lab. Please use /docs for API documentation."}


@app.get("/tweet")
async def predict():
    response: dict[str, str] = dict({"timestamp": str(datetime.now()),
                                     "response_id": str(uuid.uuid4()),
                                     "tweet": tweeter.tweet()})

    return json.dumps(response)


@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": request.model,
                    "prompt": request.prompt,
                    "stream": request.stream
                },
                timeout=60.0
            )
            response.raise_for_status()
            ollama_response = response.json()
            return {"response": ollama_response["response"]}
    except httpx.RequestError as e:
        raise HTTPException(status_code=503, detail=f"Error connecting to Ollama: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {e}")


@app.get("/health")
async def health():
    return {"message": "Congratulations, I am healthy :) "}
