FROM python:3.6-slim-buster
MAINTAINER Ewelina Dmowska <e.dmowskaa@gmail.com>

ENV LANG C.UTF-8

ENV INSTALL_PATH /srv/app
RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH

RUN apt-get update
RUN apt-get -y install python-pip python-pip-whl

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD /usr/local/bin/python3 manage.py runserver 0.0.0.0:8000
