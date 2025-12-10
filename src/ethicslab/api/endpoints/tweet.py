import json
import uuid
from datetime import datetime

from fastapi import APIRouter

from src.ethicslab.model import Tweeter, TweeterFactory

router = APIRouter()

tweeter: Tweeter = TweeterFactory.create_instance()


@router.get("/")
async def predict():
    response: dict[str, str] = dict({"timestamp": str(datetime.now()),
                                     "response_id": str(uuid.uuid4()),
                                     "tweet": tweeter.tweet()})

    return json.dumps(response)
