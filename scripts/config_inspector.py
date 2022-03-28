import kubernetes
import os

from api.GeoserverApi import GeoserverAPI
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

kubernetes.config.load_incluster_config()
k_client = kubernetes.client.CoreV1Api()


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

for p in pod_list.items:
    try:
        if p.metadata.labels["app.kubernetes.io/component"] in ["wms", "wfs"]: # FIXME: gwc not working
            service_pods[p.status.pod_ip] = create_service(
                p.status.pod_ip, p.metadata.labels["app.kubernetes.io/component"]
            )
    except KeyError:
        pass
