FROM python:3.7-alpine
RUN apk update \
  && apk add \
    build-base \
#    postgresql \
#    postgresql-dev \
    icu-dev \
    libffi-dev \
    openssl-dev \
    libpq
RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN python /usr/src/app/src/index.py

ENV PYTHONUNBUFFERED 1

COPY . .