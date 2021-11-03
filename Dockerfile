FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install -y python3.9 python3-pip

RUN mkdir /django
WORKDIR /django

ADD requirements.txt .
RUN python3.9 -m pip install -r requirements.txt

ADD db.sqlite3 .
ADD media /var/cursedbound/media
RUN chmod -R a+r /var/cursedbound/media

ADD cursedbound cursedbound
ADD cursedboundapp cursedboundapp 
ADD manage.py .

WORKDIR /django
RUN CURSEDBOUND_DEBUG=true python3.9 manage.py collectstatic

CMD gunicorn cursedbound.wsgi -b 0.0.0.0:80
