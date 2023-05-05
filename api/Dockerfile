FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY ../Model_final/* .
COPY ../create_spectrogram.py .

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--workers", "1"]


# FROM python:3.9-slim-buster

# WORKDIR /app

# COPY . /app

# RUN pip install --no-cache-dir -r requirements.txt \
#     && pip freeze > requirements.txt

# EXPOSE 8000

# CMD ["python", "main.py"]
