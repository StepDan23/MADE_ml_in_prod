import logging
import os
import time
from datetime import datetime

import pickle
from fastapi import FastAPI, status, Response
from fastapi.responses import RedirectResponse
import uvicorn

from online_inference.config.config_classes import QueryData, Prediction

logger = logging.getLogger("uvicorn")
app = FastAPI()
app.MODEL = None
app.START_TIME = datetime.now()
_PSEUDO_WAIT_SEC = 20
_PSEUDO_FAIL_SEC = 60


@app.get('/')
def root():
    return RedirectResponse(app.docs_url)


@app.get('/health')
def health():
    if (datetime.now() - app.START_TIME).seconds > _PSEUDO_FAIL_SEC:
        raise RuntimeError("Oops pseudo fail app")
    return bool(app.MODEL)


@app.on_event("startup")
def prepare_model():
    model_path = os.getenv("MODEL_PATH")
    logger.info("load model from %s", model_path)
    logger.info("waiting %s seconds for model init", _PSEUDO_WAIT_SEC)
    time.sleep(_PSEUDO_WAIT_SEC)

    try:
        with open(model_path, "rb") as fd:
            app.MODEL = pickle.load(fd)
    except Exception:
        raise RuntimeError(f"Can't load model from {model_path}")


@app.post('/predict')
async def predict(data: QueryData, response: Response):
    if not health():
        logger.warning("fail prediction model not ready")
        response.status_code = status.HTTP_425_TOO_EARLY
        return None

    logger.info("make prediction for query: %s", data)
    features = list(data.dict().values())[1:]
    y_pred = app.MODEL.predict_proba([features])[0, 1]
    prediction = Prediction(id=data.idx, y_pred=y_pred)
    return prediction


if __name__ == "__main__":
    uvicorn.run(app=app)
