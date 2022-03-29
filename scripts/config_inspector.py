import kubernetes as k8s
import os
import numpy as np

from db_layers import GeoserverBoostrap
from api.GeoserverApi import GeoserverAPI, GWCLayer
from api import (
    GEOSERVER_URL,
    GEOSERVER_REST_URL,
    GEOSERVER_BASE_URL,
    GEOSERVER_PASSWORD,
    GEOSERVER_USERNAME,
    PGDATABASE,
    PGHOST,
    PGPASSWORD,
    PGPORT,
    PGUSER,
    AUTHKEY,
)

from owslib.wms import WebMapService
from owslib.wfs import WebFeatureService
from owslib.wmts import WebMapTileService

k8s.config.load_incluster_config()
k_client = k8s.client.CoreV1Api()


def create_service(pod_ip, service):
    baseUrl = f"http://{pod_ip}:8080{GEOSERVER_BASE_URL}"
    if service == "wms":
        return WebMapService(baseUrl + "/wms", version="1.3.0", authkey=AUTHKEY)
    elif service == "wfs":
        return WebFeatureService(baseUrl + "/wfs", version="1.1.0", authkey=AUTHKEY)
    elif service == "gwc":
        return WebMapTileService(
            baseUrl + "/gwc/service/wmts?REQUEST=GetCapabilities", authkey=AUTHKEY
        )
    else:
        return None


service_pods = {}

pod_list = k_client.list_namespaced_pod(os.getenv("K8S_NAMESPACE", "default"))


geoserverInstance = GeoserverBoostrap()
geoserverInstance.create_stuff(2, 3, 3)
geoserverInstance.delete_some_stuff(2)

for p in pod_list.items:
    try:
        if p.metadata.labels["app.k8s.io/component"] in [
            "wms",
            "wfs",
            "gwc",
        ]:
            service_pods[p.status.pod_ip] = create_service(
                p.status.pod_ip, p.metadata.labels["app.k8s.io/component"]
            )
    except KeyError:
        # there might be pods without "app.k8s.io/component"
        # we just skip ahead
        pass

    # todo
    response = GWCLayer().list_all()
    sorted(list(wmts.contents.keys())) == sorted(response)
