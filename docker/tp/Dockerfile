FROM ubuntu:latest

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev  vim  \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

COPY . /app

RUN cd /app \
  && pip install pipfile-requirements \
  && pipfile2req > requirements.txt \
  && pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD python app/app.py
