#!/usr/bin/env python

from api.GeoserverBoostrap import GeoserverBoostrap

# a = wkt.loads("POLYGON ((0 0, 0 -1, 7.5 -1, 7.5 0, 0 0))")
# b = wkt.loads("POLYGON ((0 1, 1 0, 2 0.5, 3 0, 4 0, 5 0.5, 6 -0.5, 7 -0.5, 7 1, 0 1))")
# d = {"name": ["a", "b"], "geometry": [a, b]}
# gdf = gpd.GeoDataFrame(d, crs=4326)
# conn = psycopg2.connect(
#     database=PGDATABASE, user=PGUSER, password=PGPASSWORD, host=PGHOST
# )


def main():
    geoserverInstance = GeoserverBoostrap()
    geoserverInstance.create_stuff(2, 3, 3)
    geoserverInstance.delete_some_stuff(2)


if __name__ == "__main__":
    main()