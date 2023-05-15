FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt
COPY requirements-dev.txt requirements-dev.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt

ENV PYTHONPATH "${PYTHONPATH}:/"

CMD ["python", "api/main.py"]
