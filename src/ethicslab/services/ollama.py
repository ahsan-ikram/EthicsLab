import os
import httpx
from fastapi import HTTPException

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434")


async def generate_response(prompt: str, model: str, stream: bool):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{OLLAMA_URL}/api/generate",
                json={
                    "model": model,
                    "prompt": prompt,
                    "stream": stream
                },
                timeout=60.0
            )
            response.raise_for_status()
            ollama_response = response.json()
            return ollama_response["response"]
    except httpx.RequestError as e:
        raise HTTPException(status_code=503, detail=f"Error connecting to Ollama: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {e}")
