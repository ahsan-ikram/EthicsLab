from fastapi import APIRouter

from src.ethicslab.api.endpoints import chat, tweet

api_router = APIRouter()
api_router.include_router(chat.router, prefix="/chat", tags=["chat"])
api_router.include_router(tweet.router, prefix="/tweet", tags=["tweet"])
