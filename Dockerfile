FROM python:3.9

WORKDIR /workdir

COPY . /workdir

RUN ls
RUN pwd
RUN pip install ./geoserver
RUN pip install -r requirements.txt