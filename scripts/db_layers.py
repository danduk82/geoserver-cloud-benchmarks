#!/usr/bin/env python

from api.GeoserverBoostrap import GeoserverBoostrap

# a = wkt.loads("POLYGON ((0 0, 0 -1, 7.5 -1, 7.5 0, 0 0))")
# b = wkt.loads("POLYGON ((0 1, 1 0, 2 0.5, 3 0, 4 0, 5 0.5, 6 -0.5, 7 -0.5, 7 1, 0 1))")
# d = {"name": ["a", "b"], "geometry": [a, b]}
# gdf = gpd.GeoDataFrame(d, crs=4326)
# conn = psycopg2.connect(
#     database=PGDATABASE, user=PGUSER, password=PGPASSWORD, host=PGHOST
# )

workspace_name = "bbbbKAPKAXISCWFF"
store_name = "bbbbvmjhvhayjv"
native_name = "bbbbbzxqgcerbp"

import sys


def main():
    layer_name = f"xxx_{sys.argv[1]}"
    print(layer_name)
    geoserverInstance = GeoserverBoostrap()
    # geoserverInstance.create_stuff(prefix="xxx")
    geoserverInstance.create_one_layer(
        workspace_name, store_name, layer_name, native_name
    )


if __name__ == "__main__":
    main()