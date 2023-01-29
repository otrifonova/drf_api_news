FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /tmp/

RUN pip install --requirement /tmp/requirements.txt --no-cache-dir

COPY . .