FROM python:3.10-slim

RUN python -m pip install --upgrade pip
WORKDIR /usr/src/blog

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

COPY . .

