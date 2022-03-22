import kubernetes
import os

from api.GeoserverApi import GeoserverAPI
from api import (
    GEOSERVER_URL,
    GEOSERVER_REST_URL,
    GEOSERVER_PASSWORD,
    GEOSERVER_USERNAME,
    PGDATABASE,
    PGHOST,
    PGPASSWORD,
    PGPORT,
    PGUSER,
)


from owslib.wms import WebMapService
from owslib.wfs import WebFeatureService
from owslib.wmts import WebMapTileService


wms = WebMapService(GEOSERVER_URL + "/" + worskpace_name + "/wms", version="1.3.0")
wfs = WebFeatureService(GEOSERVER_URL + "/" + worskpace_name + "/wfs", version="1.1.0")
wmts = WebMapTileService(GEOSERVER_URL + "/gwc/service/wmts?REQUEST=GetCapabilities")


kubernetes.config.load_incluster_config()
k_client = kubernetes.client.CoreV1Api()


service_types = ["wms", "gwc", "wfs"]


wms_pods = []
pod_list = k_client.list_namespaced_pod(os.getenv("K8S_NAMESPACE", "default"))

for p in pod_list.items:
    try:
        if p.metadata.labels["app.kubernetes.io/component"] == "wms":
            wms_pods.append(p.status.pod_ip)
    except KeyError:
        pass
