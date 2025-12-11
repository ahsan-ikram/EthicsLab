from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from src.ethicslab.api.api import api_router

app = FastAPI()


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")


@app.get("/health")
async def health():
    return {"message": "Congratulations, I am healthy :) "}


app.include_router(api_router, prefix="/api")
