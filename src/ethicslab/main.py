import json
import uuid
from datetime import datetime

# import uvicorn
from fastapi import FastAPI

from src.ethicslab.model import Tweeter, TweeterFactory

app = FastAPI()
# tweeter: Tweeter = TweeterFactory.create_instance()


@app.get("/")
async def root():
    return {"message": "Welcome to auto tweet generator API"}


@app.get("/tweet")
async def predict():
    response: dict[str, str] = dict({"timestamp": str(datetime.now()),
                                     "response_id": str(uuid.uuid4()),
                                     # "tweet": tweeter.tweet()})
                                     "tweet": "Hard coded tweet for testing purposes."})
    return json.dumps(response)


@app.get("/health")
async def health():
    return {"message": "Congratulations, I am healthy :) "}


