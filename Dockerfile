FROM python:3.11-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONPATH="/"

COPY ./poetry.lock /
COPY ./pyproject.toml /

#  Instalando o cur para instalar o poetry
RUN apt-get update -y && apt-get install curl -y \
&& curl -sSL https://install.python-poetry.org | python3 - \
#  Configuração para não criar o env
&& poetry config virtualenvs.create false\
&& poetry install \
#  Remover o curl
&& apt-get remove curl -y

COPY . .
WORKDIR /app

