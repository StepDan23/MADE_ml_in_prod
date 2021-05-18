FROM python:3.9

COPY online_inference   /opt/app/online_inference
COPY artefacts/model.pkl setup.py requirements.txt  /opt/app/
WORKDIR /opt/app
RUN pip install .

ENV MODEL_PATH="/opt/app/model.pkl"
ENTRYPOINT ["uvicorn", "online_inference.app:app", "--host", "0.0.0.0"]