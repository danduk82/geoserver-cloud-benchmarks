#!/usr/bin/env python
import kubernetes as k8s
import os
import numpy as np

from api.GeoserverBoostrap import GeoserverBoostrap
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
from owslib.util import ServiceException

k8s.config.load_incluster_config()
k_client = k8s.client.CoreV1Api()


def create_service(pod_ip, service):
    # baseUrl = f"http://{pod_ip}:8080{GEOSERVER_BASE_URL}"
    baseUrl = f"http://{pod_ip}:8080"
    if service == "wms":
        return {
            "service": "wms",
            "ogc_service": WebMapService(
                baseUrl + "/wms", version="1.3.0", authkey=AUTHKEY
            ),
        }
    elif service == "wfs":
        return {
            "service": "wfs",
            "ogc_service": WebFeatureService(
                baseUrl + "/wfs", version="1.1.0", authkey=AUTHKEY
            ),
        }
    elif service == "gwc":
        return {
            "service": "gwc",
            "ogc_service": WebMapTileService(
                baseUrl + "/gwc/service/wmts?REQUEST=GetCapabilities", authkey=AUTHKEY
            ),
        }
    else:
        return None


prefix = "deleteme"

service_pods = {}

pod_list = k_client.list_namespaced_pod(os.getenv("K8S_NAMESPACE", "default"))


geoserverInstance = GeoserverBoostrap()
geoserverInstance.create_stuff(2, 3, 3, prefix=prefix)
# geoserverInstance.delete_some_stuff(2)


results = {}
for p in pod_list.items:
    try:
        service_type = p.metadata.labels["app.kubernetes.io/component"]
        if service_type in [
            "wms",
            "wfs",
            "gwc",
        ]:
            service_pods[p.status.pod_ip] = create_service(
                p.status.pod_ip, service_type
            )
            results[f"{service_type}:{p.status.pod_ip}"] = False

    except KeyError:
        # there might be pods without "app.kubernetes.io/component"
        # we just skip ahead
        pass


# todo
created_layers = sorted(geoserverInstance.created_layers)
# deleted_workspaces = sorted(geoserverInstance.deleted_workspaces)

try:
    wmts_layers = GWCLayer().list_all()
except ServiceException:
    wmts_layers = False
for pod in service_pods:
    service_type = service_pods[pod]["service"]
    if service_type == "wms" or service_type == "wfs":
        results[f"{service_type}:{pod}"] = all(
            layer in list(service_pods[pod]["ogc_service"].contents.keys())
            for layer in [f"{n}:{l}" for n, l in created_layers]
        )
    elif service_type == "gwc":
        if not wmts_layers:
            results[f"{service_type}:{pod}"] = False
        else:
            results[f"{service_type}:{pod}"] = all(
                layer in wmts_layers
                for layer in [f"{n}:{l}" for n, l in created_layers]
            )


print(results)

# cleanup in the end
for w in geoserverInstance.geoserverServer.list_workspaces():
    if w.startswith(prefix):
        geoserverInstance.geoserverServer.delete_workspace(w)
for l in wmts_layers:
    if l.startswith(prefix):
        GWCLayer.delete_layer(l)