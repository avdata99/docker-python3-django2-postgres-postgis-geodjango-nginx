FROM python:3.5

# Initialize
RUN mkdir -p /data/web
WORKDIR /data/web
COPY requirements.txt /data/web/

# Setup

RUN apt-get update -y
# RUN apt-get upgrade -y
# RUN apt-get install -y python3 python3-dev postgresql-client postgresql-dev build-base gettext
RUN apt-get install -y python3 python3-setuptools postgresql gettext gunicorn

# geolibs para geodjango
RUN apt-get install -y binutils libproj-dev gdal-bin

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Prepare
COPY . /data/web/
WORKDIR /data/web/mydjango
