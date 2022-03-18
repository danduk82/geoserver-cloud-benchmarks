#!/usr/bin/env python

from api import (
    GEOSERVER_URL,
    GEOSERVER_REST_URL,
    GEOSERVER_PASSWORD,
    GEOSERVER_USERNAME,
)

from api.GeoserverApi import GeoserverAPI
from pprint import pprint
import pandas
from collections import Counter

from random import randint

from owslib.wms import WebMapService
from owslib.util import ServiceException

import matplotlib.pyplot as plt

plt.tight_layout()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)


class Bbox:
    def __init__(self, center: Point, delta: Point = Point(1, 1)):
        self.ll = center - delta
        self.ur = center + delta

    def get(self):
        return (self.ll.x, self.ll.y, self.ur.x, self.ur.y)


fullConfig = {}
instances = []

geoserverServer = GeoserverAPI(
    GEOSERVER_REST_URL, GEOSERVER_USERNAME, GEOSERVER_PASSWORD
)

headers = []

for workspace_name in geoserverServer.list_workspaces():
    fullConfig[workspace_name] = WebMapService(
        GEOSERVER_URL + "/" + workspace_name + "/wms",
        version="1.3.0",
        username=GEOSERVER_USERNAME,
        password=GEOSERVER_PASSWORD,
    )

wms = fullConfig[list(fullConfig.keys())[0]]
print(type(wms))

EPSG_3857_BBOX = Bbox(Point(-20037508, -20037508), Point(20037508, 20037508))

for i in range(10):
    try:
        img = wms.getmap(
            layers=[
                list(wms.contents.keys())[
                    randint(0, len(list(wms.contents.keys())) - 1)
                ]
            ],
            srs="EPSG:3857",
            bbox=Bbox(
                Point(
                    randint(EPSG_3857_BBOX.ll.x, EPSG_3857_BBOX.ur.x),
                    randint(EPSG_3857_BBOX.ll.y, EPSG_3857_BBOX.ur.y),
                ),
                Point(1, 1),
            ).get(),
            size=(256, 256),
            format="image/png",
            transparent=True,
        )

        instances.append(img.info()["X-Gs-Cloud-Service-Id"])
    except ServiceException:
        pass

instances_count = Counter(instances)
df = pandas.DataFrame.from_dict(instances_count, orient="index")
fig = df.plot(kind="bar").get_figure()
fig.tight_layout(rect=(0, 0.1, 1, 1))
fig.savefig("/tmp/barplot.png")


pprint(instances)