#!/usr/bin/env python
import mercantile
from random import randint, sample
import requests
from owslib.wms import WebMapService
import numpy as np

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

wms = WebMapService(GEOSERVER_URL + "/wms", version="1.3.0", authkey=AUTHKEY)

# # DB global
# GEOPORTAL_SHARED:ZIPS
# GEOPORTAL_SHARED:OFZ_ALL
# # DB local
# GEOPORTAL:cu_classic_fl_river

# # Raster
# "GEOPORTAL_SHARED:SRGFZ_v3"
# GEOPORTAL_SHARED:SRPFZ <-- super heavy, 90gb raster tiles
# BES_*

# LAYERS = "GEOPORTAL_SHARED:Windspeed"


def tupleBbox(bbox):
    return (bbox.left, bbox.bottom, bbox.right, bbox.top)


def generateRandomBboxesInExtent(extent, min_zl, max_zl, nb_tiles):
    diff_x = extent[2] - extent[0]
    diff_y = extent[3] - extent[1]
    rand_x = (np.random.random((nb_tiles,)) * diff_x) + extent[0]
    rand_y = (np.random.random((nb_tiles,)) * diff_y) + extent[1]
    rand_z = np.random.randint(min_zl, max_zl, (nb_tiles,))
    return [
        tupleBbox(
            mercantile.xy_bounds(mercantile.tile(rand_x[i], rand_y[i], rand_z[i]))
        )
        for i in range(nb_tiles)
    ]


layers = [
    "GEOPORTAL_SHARED:ZIPS",
    "GEOPORTAL_SHARED:OFZ_ALL",
    "GEOPORTAL:cu_classic_fl_river",
    "GEOPORTAL:SRGFZ",
    "GEOPORTAL_SHARED:SRPFZ",
]

total_nb_requests = 20000

layerInfo = {}
for layer in layers:
    layerInfo[layer] = {}
    layerInfo[layer]["bboxWGS84"] = wms[layer].boundingBoxWGS84  # (xmin,ymin,xmax,ymax)
    layerInfo[layer]["bbox3857"] = mercantile.xy(
        layerInfo[layer]["bboxWGS84"][0], layerInfo[layer]["bboxWGS84"][1]
    ) + mercantile.xy(
        layerInfo[layer]["bboxWGS84"][2], layerInfo[layer]["bboxWGS84"][3]
    )
    all_cached_tiles = [
        i
        for i in mercantile.tiles(
            layerInfo[layer]["bboxWGS84"][0],
            layerInfo[layer]["bboxWGS84"][1],
            layerInfo[layer]["bboxWGS84"][2],
            layerInfo[layer]["bboxWGS84"][3],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        )
    ]
    nb_real_cached = len(all_cached_tiles)
    nb_should_be_cached = int(total_nb_requests * 0.8)
    nb_cached = (
        nb_real_cached if nb_real_cached <= nb_should_be_cached else nb_should_be_cached
    )

    sampled_cached_tiles = sample(all_cached_tiles, nb_cached)
    layerInfo[layer]["tileWmsBboxes"] = [
        tupleBbox(mercantile.xy_bounds(sample_tile))
        for sample_tile in sampled_cached_tiles
    ]
    layerInfo[layer]["tileWmsBboxes"] += generateRandomBboxesInExtent(
        layerInfo[layer]["bboxWGS84"], 10, 15, total_nb_requests - nb_cached
    )
    with open(f"/tmp/{layer}.csv", "w") as f_out:
        f_out.writelines(
            [
                ",".join("%.5f" % x for x in a) + "\n"
                for a in layerInfo[layer]["tileWmsBboxes"]
            ]
        )

# tileBbox = []
# for i in range(250):
#     z = randint(4, 9)
#     x = randint(0, (2 ** z) - 1)
#     y = randint(0, (2 ** z) - 1)
#     # print(f"x={x},y={y},z={z}")
#     tile = mercantile.Tile(x=x, y=y, z=z)
#     bbox = mercantile.xy_bounds(tile)
#     tileBbox.append((tile, f"{bbox.left},{bbox.bottom},{bbox.right},{bbox.top}\n"))

# results = []

# for tile, bbox_str in tileBbox:
#     r_url = f"{GEOSERVER_URL}/wms?authkey={AUTHKEY}&SERVICE=WMS&FORMAT=image/png8&exceptions=application/json&SRS=EPSG:3857&Request=GetMap&VERSION=1.3.0&Service=WMS&WIDTH=256&HEIGHT=256&TRANSPARENT=TRUE&tiled=true&LAYERS={LAYERS}&CRS=EPSG:3857&BBOX={bbox_str}"
#     print(r_url)
#     resp = requests.get(r_url)
#     gwc_hit = resp.headers["geowebcache-cache-result"]
#     results.append(f"{gwc_hit};{tile};{bbox_str}")
#     print(f"{tile}; {gwc_hit}\n")


# with open("/tmp/results.csv", "w") as output:
#     output.writelines(results)


# # manually cleanup results csv and then
# LAYERS = "GEOPORTAL:cu_classic_tc_wind"

# with open("/tmp/urls.csv", "r") as input:
#     urls = input.readlines()

# results = []
# for url in urls:
#     bbox_str = url.replace("\n", "")
#     if not bbox_str == "":
#         r_url = f"{GEOSERVER_URL}/wms?authkey={AUTHKEY}&SERVICE=WMS&FORMAT=image/png8&exceptions=application/json&SRS=EPSG:3857&Request=GetMap&VERSION=1.3.0&Service=WMS&WIDTH=256&HEIGHT=256&TRANSPARENT=TRUE&tiled=true&LAYERS={LAYERS}&CRS=EPSG:3857&BBOX={bbox_str}"
#         print(r_url)
#         resp = requests.get(r_url)
#         gwc_hit = resp.headers["geowebcache-cache-result"]
#         results.append(f"{gwc_hit};{bbox_str}\n")
#         print(resp.headers)
#         print(f"{gwc_hit}\n")

# with open("/tmp/replay1000.csv", "w") as output:
#     output.writelines(results)
