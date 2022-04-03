#!/usr/bin/env python
import argparse as ap
import kubernetes as k8s
import json
from json.decoder import JSONDecodeError
import multiprocessing as mp
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


def create_service(pod, results_dict, suffix):
    try:
        service_type = pod.metadata.labels["app.kubernetes.io/component"]
        if service_type in [
            "wms",
            "wfs",
            "gwc",
        ]:
            results_dict[f"{service_type}:{pod.status.pod_ip}:{suffix}"] = False
            baseUrl = f"http://{pod.status.pod_ip}:8080"
            if service_type == "wms":
                return {
                    "service": "wms",
                    "ogc_service": WebMapService(
                        baseUrl + "/wms", version="1.3.0", authkey=AUTHKEY
                    ),
                }
            elif service_type == "wfs":
                return {
                    "service": "wfs",
                    "ogc_service": WebFeatureService(
                        baseUrl + "/wfs", version="1.1.0", authkey=AUTHKEY
                    ),
                }
            elif service_type == "gwc":
                return {
                    "service": "gwc",
                    "ogc_service": WebMapTileService(
                        baseUrl + "/gwc/service/wmts?REQUEST=GetCapabilities",
                        authkey=AUTHKEY,
                    ),
                }
            else:
                return None

    except KeyError:
        # there might be pods without "app.kubernetes.io/component"
        # we just skip ahead
        pass
    return None


def createParser():
    parser = ap.ArgumentParser(
        description="""
This software creates dummy layers in geoserver-cloud using the
rest api, and then checks if all the pods have correctly updated
their configuration.

It is meant to run inside a pod.

The pod must be granted with these k8s priviledges:

    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: Role
    metadata:
        namespace: default
        name: pod-reader
    rules:
        - apiGroups: [""] # "" indicates the core API group
    resources: ["pods"]
    verbs: ["get", "watch", "list"]


""",
        epilog="""
Disclaimer:
    This software is provided \"as is\" and
    is not granted to work in particular cases or without bugs. The author
    disclaims any responsability in case of data loss, computer damage or any
    other bad issue that could arise using this software.
    Author:
    Andrea Borghi, Camptocamp SA, Switzerland
    last update: March, 2022
Example:
   config_inspector -w 2 -s 3 -l 4 -o output_folder/output_file.json
    """,
        formatter_class=ap.RawDescriptionHelpFormatter,
    )

    optionGroup = parser.add_argument_group("Program options")
    optionGroup.add_argument(
        "-v", "--version", action="version", version="%(prog)s v0.1 Licence: WTFPL v2"
    )

    optionGroup.add_argument(
        "-o",
        "--output",
        dest="output_file",
        action="store",
        default="/tmp/results.json",
        type=str,
        help="output file name to be used, the defalut is '/tmp/results.json'",
    )
    optionGroup.add_argument(
        "-p",
        "--prefix",
        dest="prefix",
        action="store",
        default="deleteme",
        type=str,
        help="prefix to use for the tmp workspaces and layer names",
    )
    optionGroup.add_argument(
        "-c",
        "--nb-processes",
        dest="nb_processes",
        action="store",
        type=int,
        default=1,
        help="number of total processes to use, if absent 'nb_workspaces' will be used",
    )
    optionGroup.add_argument(
        "-w",
        "--nb-workspaces",
        dest="nb_workspaces",
        action="store",
        type=int,
        default=1,
        help="number of total workspaces to create, default=1",
    )
    optionGroup.add_argument(
        "-s",
        "--nb-stores",
        dest="nb_stores",
        action="store",
        type=int,
        default=2,
        help="number of total stores to create in each workspace, default=2",
    )
    optionGroup.add_argument(
        "-l",
        "--nb-layers",
        dest="nb_layers",
        action="store",
        type=int,
        default=4,
        help="number of total layers to create in each store, default=4",
    )
    return parser


def main():
    parser = createParser()
    options = parser.parse_args()
    options.prefix

    nb_processes = (
        options.nb_workspaces if options.nb_processes == 0 else options.nb_processes
    )

    # FIXME: https://stackoverflow.com/questions/38393269/fill-up-a-dictionary-in-parallel-with-multiprocessing
    manager = mp.Manager()
    service_pods = {}

    pod_list = k_client.list_namespaced_pod(os.getenv("K8S_NAMESPACE", "default"))

    geoserverInstance = GeoserverBoostrap()
    geoserverInstance.create_stuff(
        options.nb_workspaces,
        options.nb_stores,
        options.nb_layers,
        prefix=options.prefix,
        nb_processes=nb_processes,
    )
    # geoserverInstance.delete_some_stuff(2) # FIXME: not working

    # load results from older tests
    try:
        with open(options.output_file) as output_file:
            output_results = json.load(output_file)
    except (FileNotFoundError, JSONDecodeError):
        output_results = []
    results = manager.dict()

    pool = mp.Pool(len(pod_list.items))
    service_pods_list = list(
        filter(
            None,
            [
                pool.apply(create_service, args=(pod, results, "creation"))
                for pod in pod_list.items
            ],
        )
    )
    pool.close()
    for k, v in service_pods_list:
        service_pods[k] = v

    # todo
    created_layers = sorted(geoserverInstance.created_layers)
    # deleted_workspaces = sorted(geoserverInstance.deleted_workspaces)

    # validate creation
    print("validating creation")
    try:
        wmts_layers = GWCLayer().list_all()
    except ServiceException:
        wmts_layers = False
    for pod in service_pods:
        service_type = service_pods[pod]["service"]
        if service_type == "wms" or service_type == "wfs":
            results[f"{service_type}:{pod}:creation"] = all(
                layer in list(service_pods[pod]["ogc_service"].contents.keys())
                for layer in [f"{n}:{l}" for n, l in created_layers]
            )
        elif service_type == "gwc":
            if not wmts_layers:
                results[f"{service_type}:{pod}:creation"] = False
            else:
                results[f"{service_type}:{pod}:creation"] = all(
                    layer in wmts_layers
                    for layer in [f"{n}:{l}" for n, l in created_layers]
                )

    # delete everything
    geoserverInstance.cleanup()
    for l in wmts_layers:
        if l.startswith(options.prefix):
            GWCLayer.delete_layer(l)

    # validate deletion
    print("validating deletion")
    pool = mp.Pool(len(pod_list.items))
    service_pods_list = list(
        filter(
            None,
            [
                pool.apply(create_service, args=(pod, results, "deletion"))
                for pod in pod_list.items
            ],
        )
    )
    pool.close()
    for k, v in service_pods_list:
        service_pods[k] = v

    try:
        wmts_layers = GWCLayer().list_all()
    except ServiceException:
        wmts_layers = False
    for pod in service_pods:
        service_type = service_pods[pod]["service"]
        if service_type == "wms" or service_type == "wfs":
            results[f"{service_type}:{pod}:deletion"] = not any(
                layer in list(service_pods[pod]["ogc_service"].contents.keys())
                for layer in [f"{n}:{l}" for n, l in created_layers]
            )
        elif service_type == "gwc":
            if not wmts_layers:
                results[f"{service_type}:{pod}:deletion"] = False
            else:
                results[f"{service_type}:{pod}:deletion"] = not any(
                    layer in wmts_layers
                    for layer in [f"{n}:{l}" for n, l in created_layers]
                )
    results["parameters"] = {
        "nb_workspaces": options.nb_workspaces,
        "nb_stores": options.nb_stores,
        "nb_layers": options.nb_layers,
    }
    output_results.append(
        dict(results)
    )  # cast mp.Manager.dict to normal dict for serialization

    with open(options.output_file, "w") as output_file:
        json.dump(output_results, output_file)


if __name__ == "__main__":
    main()