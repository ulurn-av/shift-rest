FROM python:3.11-slim-buster

RUN mkdir /app

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

COPY . .