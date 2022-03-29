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

k8s.config.load_incluster_config()
k_client = k8s.client.CoreV1Api()


def create_service(pod_ip, service):
    baseUrl = f"http://{pod_ip}:8080{GEOSERVER_BASE_URL}"
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


service_pods = {}

pod_list = k_client.list_namespaced_pod(os.getenv("K8S_NAMESPACE", "default"))


geoserverInstance = GeoserverBoostrap()
geoserverInstance.create_stuff(2, 3, 3)
# geoserverInstance.delete_some_stuff(2)


results = {}
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
            results[p.status.pod_ip : False]

    except KeyError:
        # there might be pods without "app.k8s.io/component"
        # we just skip ahead
        pass


# todo
created_layers = sorted(geoserverInstance.created_layers)
deleted_workspaces = sorted(geoserverInstance.deleted_workspaces)


# np.where(b[:] == "bla")[0]

wmts_layers = GWCLayer().list_all()
for pod in service_pods:
    if service_pods[pod]["service"] == "wms":
        pass
    elif service_pods[pod]["service"] == "wfs":
        pass
    elif service_pods[pod]["service"] == "gwc":
        results[pod] = (
            sorted(list(service_pods[pod]["ogc_service"].contents.keys()))
            == wmts_layers
        )

print(results)