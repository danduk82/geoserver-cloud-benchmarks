#!/usr/bin/env python

from ast import arg
from api import (
    GEOSERVER_URL,
    GEOSERVER_REST_URL,
    GEOSERVER_PASSWORD,
    GEOSERVER_USERNAME,
)

from api.GeoserverApi import GeoserverAPI

import argparse as ap
from pprint import pprint
import pandas
from collections import Counter
import multiprocessing as mp

from random import randint

from owslib.wms import WebMapService
from owslib.util import ServiceException


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


# FIXME: dirty global
EPSG_3857_BBOX = Bbox(Point(-20037508, -20037508), Point(20037508, 20037508))


def createParser():
    parser = ap.ArgumentParser(
        description="""
This software runs several requests against a geoserver-cloud instance,
and performs basic statistic with regard to the load-balancing.
 
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
   check_balance -n 1000 -p 12 -o output_folder/output_file.png
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
        default="/tmp/barplot.png",
        type=str,
        help="output file name to be used, the defalut is '/tmp/barplot.png'",
    )
    optionGroup.add_argument(
        "-n",
        "--number",
        dest="nb_request",
        action="store",
        type=int,
        default=100,
        help="number of total requests that have to be performed, default is 100",
    )
    optionGroup.add_argument(
        "-p",
        "--processes",
        dest="nb_process",
        action="store",
        type=int,
        default=mp.cpu_count(),
        help="number of parallel processes to start, default is 'mp.cpu_count()'",
    )
    return parser


def parallel_requests(wms, dummy):
    try:
        img = wms.getmap(
            layers=[
                list(wms.contents.keys())[
                    randint(0, len(list(wms.contents.keys())) - 1)
                ]
            ],
            srs="EPSG:3857",
            # FIXME: Bbox should be taken between the EPSG_3857 layer boundaries
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
        return img.info()["X-Gs-Cloud-Service-Id"]
    except ServiceException:
        return None


def main():
    parser = createParser()
    options = parser.parse_args()

    fullConfig = {}

    geoserverServer = GeoserverAPI(
        GEOSERVER_REST_URL, GEOSERVER_USERNAME, GEOSERVER_PASSWORD
    )

    for workspace_name in geoserverServer.list_workspaces():
        fullConfig[workspace_name] = WebMapService(
            GEOSERVER_URL + "/" + workspace_name + "/wms",
            version="1.3.0",
            username=GEOSERVER_USERNAME,
            password=GEOSERVER_PASSWORD,
        )

    # FIXME: should randomly select from the different workspaces as well
    wms = fullConfig[list(fullConfig.keys())[0]]
    print(type(wms))

    pool = mp.Pool(options.nb_process)
    instances = list(
        filter(
            None,
            [
                pool.apply(parallel_requests, args=(wms, True))
                for i in range(options.nb_request)
            ],
        )
    )
    pool.close()

    instances_count = Counter(instances)
    df = pandas.DataFrame.from_dict(instances_count, orient="index")
    fig = df.plot(kind="bar").get_figure()
    fig.tight_layout(rect=(0, 0.1, 1, 1))
    fig.savefig(options.output_file)

    pprint(instances)
    pprint(len(instances))


if __name__ == "__main__":
    main()