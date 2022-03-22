FROM python:3.9


# put the usual apt mess for docker images
RUN apt install 
ENV \
    DEBIAN_FRONTEND=noninteractive \
    SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

# hadolint ignore=SC1091,DL3008
RUN \
    . /etc/os-release && \
    apt-get update && \
    apt-get --assume-yes upgrade && \
    apt-get install --assume-yes --no-install-recommends apt-utils && \
    apt-get install --assume-yes --no-install-recommends apt-transport-https gettext less gnupg libpq5 postgresql-client vim && \
    apt-get clean && \
    rm --recursive --force /var/lib/apt/lists/*

WORKDIR /workdir
COPY geoserver/ /workdir/geoserver/
COPY OWSLib/ /workdir/OWSLib/
COPY scripts/ /workdir/scripts/
COPY requirements.txt /workdir/requirements.txt

RUN pip install ./geoserver && \
    pip install ./OWSLib && \
    pip install -r requirements.txt && \
    pip cache purge

