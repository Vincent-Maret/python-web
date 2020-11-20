FROM ubuntu:latest

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev pipenv vim  \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

COPY . /app

RUN cd /app \
  pipenv shell \
  pip3 install Flask