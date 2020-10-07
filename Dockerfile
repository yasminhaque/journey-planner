FROM python:3.7

RUN mkdir /app

COPY /app /app
COPY pyproject.toml /app

WORKDIR /app

ENV PYTHONPATH=${PYTHONPATH}:${PWD}

ARG APPLICATION_CONFIG

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
