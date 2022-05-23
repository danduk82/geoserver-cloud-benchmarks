import mercantile
from random import randint

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

import requests

# LAYERS = "GEOPORTAL_SHARED:Windspeed"
LAYERS = "GEOPORTAL:SRGFZ"

tileBbox = []
for i in range(250):
    z = randint(4, 9)
    x = randint(0, (2 ** z) - 1)
    y = randint(0, (2 ** z) - 1)
    # print(f"x={x},y={y},z={z}")
    tile = mercantile.Tile(x=x, y=y, z=z)
    bbox = mercantile.xy_bounds(tile)
    tileBbox.append((tile, f"{bbox.left},{bbox.bottom},{bbox.right},{bbox.top}\n"))

results = []

for tile, bbox_str in tileBbox:
    r_url = f"{GEOSERVER_URL}/wms?authkey={AUTHKEY}&SERVICE=WMS&FORMAT=image/png8&exceptions=application/json&SRS=EPSG:3857&Request=GetMap&VERSION=1.3.0&Service=WMS&WIDTH=256&HEIGHT=256&TRANSPARENT=TRUE&tiled=true&LAYERS={LAYERS}&CRS=EPSG:3857&BBOX={bbox_str}"
    print(r_url)
    resp = requests.get(r_url)
    gwc_hit = resp.headers["geowebcache-cache-result"]
    results.append(f"{gwc_hit};{tile};{bbox_str}")
    print(f"{tile}; {gwc_hit}\n")


with open("/tmp/results1000_deprecated.csv", "w") as output:
    output.writelines(results)
results = []


LAYERS = "GEOPORTAL:cu_classic_tc_wind"

with open("/tmp/urls.csv", "r") as input:
    urls = input.readlines()

results = []
for url in urls:
    bbox_str = url.replace("\n", "")
    if not bbox_str == "":
        r_url = f"{GEOSERVER_URL}/wms?authkey={AUTHKEY}&SERVICE=WMS&FORMAT=image/png8&exceptions=application/json&SRS=EPSG:3857&Request=GetMap&VERSION=1.3.0&Service=WMS&WIDTH=256&HEIGHT=256&TRANSPARENT=TRUE&tiled=true&LAYERS={LAYERS}&CRS=EPSG:3857&BBOX={bbox_str}"
        print(r_url)
        resp = requests.get(r_url)
        gwc_hit = resp.headers["geowebcache-cache-result"]
        results.append(f"{gwc_hit};{bbox_str}\n")
        print(resp.headers)
        print(f"{gwc_hit}\n")

with open("/tmp/replay1000.csv", "w") as output:
    output.writelines(results)
