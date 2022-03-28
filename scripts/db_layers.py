#!/usr/bin/env python

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

import os
import os.path
import random
import string

from pprint import pprint

import pandas as pd
import shapely
import shapely.wkt as wkt
import geopandas as gpd

import sqlalchemy
from sqlalchemy import Column, Integer, String, Table, MetaData
from sqlalchemy.engine import create_engine
from geoalchemy2 import Geometry


# a = wkt.loads("POLYGON ((0 0, 0 -1, 7.5 -1, 7.5 0, 0 0))")
# b = wkt.loads("POLYGON ((0 1, 1 0, 2 0.5, 3 0, 4 0, 5 0.5, 6 -0.5, 7 -0.5, 7 1, 0 1))")
# d = {"name": ["a", "b"], "geometry": [a, b]}
# gdf = gpd.GeoDataFrame(d, crs=4326)
# conn = psycopg2.connect(
#     database=PGDATABASE, user=PGUSER, password=PGPASSWORD, host=PGHOST
# )


def randomStr(nb_char=10, str_type=string.ascii_lowercase):
    return "".join(random.choices(str_type, k=nb_char))


class StupidPgLayers:
    def __init__(self, engine, table_name, geom_type="POINT"):
        self.engine = engine
        self.metadata_obj = MetaData()
        self.create_layer(table_name, geom_type)

    def create_layer(self, table_name, geom_type="POINT"):
        self._table = Table(
            table_name,
            self.metadata_obj,
            Column("id", Integer, primary_key=True),
            Column("name", String),
            Column("geom", Geometry(geometry_type=geom_type, srid=3857)),
        )
        try:
            self._table.create(self.engine)
        except sqlalchemy.exc.ProgrammingError:
            pass

    def insert(self, name, geom):
        stmt = sqlalchemy.insert(self._table).values(name=name, geom=geom)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)

    def drop(self):
        self._table.drop(self.engine)


def main():
    finalCleanup = False
    created_workspaces = []
    created_pgstores = []
    created_layers = []
    created_pg_layers = []
    # create a new workspace
    for w_i in range(random.randint(1, 1)):
        workspace_name = randomStr(12, string.ascii_uppercase)
        geoserverServer = GeoserverAPI(
            GEOSERVER_REST_URL, GEOSERVER_USERNAME, GEOSERVER_PASSWORD
        )
        geoserverServer.create_workspace(workspace_name)
        created_workspaces.append(workspace_name)
        workspaces = geoserverServer.list_workspaces()
        pprint(workspaces)

        # create one db store
        store_name = randomStr()
        geoserverServer.create_pg_store(
            workspace_name, store_name, PGHOST, PGPORT, PGDATABASE, PGUSER, PGPASSWORD
        )
        created_pgstores.append(store_name)

        # create layer in postgis
        engine = create_engine(
            f"postgresql://{PGUSER}:{PGPASSWORD}@{PGHOST}:{PGPORT}/{PGDATABASE}"
        )
        for l_i in range(random.randint(1, 1)):
            layer_name = randomStr()
            pg_layer = StupidPgLayers(engine, layer_name, "POLYGON")
            pg_layer.insert(name=randomStr(), geom="POLYGON((0 0,1 0,1 1,0 1,0 0))")
            created_pg_layers.append(pg_layer)

            # setup the layer in geoserver
            geoserverServer.create_pg_layer(
                workspace_name,
                store_name,
                layer_name,
                native_name=layer_name,
                feature_type="Polygon",
            )
            geoserverServer.create_gwc_layer(workspace_name, layer_name)

            created_layers.append(layer_name)
            print(f"layer: {workspace_name}:{layer_name}")

    if finalCleanup:
        # brutal cleanup at the end
        for workspace in created_workspaces:
            geoserverServer.delete_workspace(workspace)

        for pg_layer in created_pg_layers:
            pg_layer.drop()


if __name__ == "__main__":
    main()