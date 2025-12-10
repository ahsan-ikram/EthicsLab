from fastapi import FastAPI

from src.ethicslab.api.api import api_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to Ethics Lab. Please use /docs for API documentation."}


@app.get("/health")
async def health():
    return {"message": "Congratulations, I am healthy :) "}


app.include_router(api_router, prefix="/api")
