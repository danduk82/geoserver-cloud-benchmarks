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
import multiprocessing as mp

from pprint import pprint

import pandas as pd
import shapely
import shapely.wkt as wkt
import geopandas as gpd

import sqlalchemy
from sqlalchemy import Column, Integer, String, Table, MetaData
from sqlalchemy.engine import create_engine
from geoalchemy2 import Geometry
from urllib.parse import quote_plus as urlquote


def randomStr(nb_char=10, str_type=string.ascii_lowercase, prefix=""):
    return prefix + "".join(random.choices(str_type, k=nb_char))


class StupidPgLayers:
    def __init__(self, engine, table_name, workspace_name, geom_type="POINT"):
        self.engine = engine
        self.layer_name = table_name
        self.workspace_name = workspace_name
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


class GeoserverBoostrap:
    def __init__(
        self,
        geoserver_rest_url=GEOSERVER_REST_URL,
        geoserver_username=GEOSERVER_USERNAME,
        geoserver_password=GEOSERVER_PASSWORD,
    ):
        self.finalCleanup = False
        self.created_workspaces = []
        self.created_pgstores = []
        self.created_layers = []
        self.created_pg_layers = []
        self.deleted_workspaces = []
        self.geoserverServer = GeoserverAPI(
            geoserver_rest_url, geoserver_username, geoserver_password
        )

    def create_stuff(
        self, nb_workspaces=1, nb_stores=1, nb_layers=1, prefix="", nb_processes=1
    ):

        # create a new workspace
        for w_i in range(nb_workspaces):
            workspace_name = randomStr(12, string.ascii_uppercase, prefix=prefix)
            self.geoserverServer.create_workspace(workspace_name)
            self.created_workspaces.append(workspace_name)

            for pg_i in range(nb_stores):
                # create db store
                store_name = randomStr(prefix=prefix)
                self.geoserverServer.create_pg_store(
                    workspace_name,
                    store_name,
                    PGHOST,
                    PGPORT,
                    PGDATABASE,
                    PGUSER,
                    PGPASSWORD,
                )
                self.created_pgstores.append(store_name)

                # create layer in postgis
                engine = create_engine(
                    f"postgresql://{PGUSER}:%s@{PGHOST}:{PGPORT}/{PGDATABASE}"
                    % urlquote(PGPASSWORD)
                )
                for l_i in range(nb_layers):
                    layer_name = randomStr(prefix=prefix)
                    pg_layer = StupidPgLayers(
                        engine, layer_name, workspace_name, "POLYGON"
                    )
                    pg_layer.insert(
                        name=randomStr(),
                        geom="SRID=3857;POLYGON((0 0,1 0,1 1,0 1,0 0))",
                    )
                    self.created_pg_layers.append(pg_layer)

                    # setup the layer in geoserver
                    self.geoserverServer.create_pg_layer(
                        workspace_name,
                        store_name,
                        layer_name,
                        native_name=layer_name,
                        feature_type="Polygon",
                    )
                    self.geoserverServer.create_gwc_layer(workspace_name, layer_name)

                    self.created_layers.append(f"{workspace_name}:{layer_name}")
                    print(f"layer: {workspace_name}:{layer_name}")

    def delete_some_stuff(self, nb_workspaces=1):
        # FIXME: not working because of random id for the moment and GWC not deleting the layers
        for i_w in range(nb_workspaces):
            to_del = random.randint(0, len(self.created_workspaces))
            try:
                self.deleted_workspaces.append(self.created_workspaces[to_del])
                self.geoserverServer.delete_workspace(self.created_workspaces[to_del])
                del self.created_workspaces[to_del]
            except ValueError:
                self.deleted_workspaces.append(self.created_workspaces[to_del])
                self.geoserverServer.delete_workspace(self.created_workspaces[to_del])
                del self.created_workspaces[to_del]

    def tabula_rasa(self):
        workspaces = self.geoserverServer.list_workspaces()
        for workspace in workspaces:
            self.geoserverServer.delete_workspace(workspace)

    def cleanup(self):
        # brutal cleanup at the end
        for workspace in self.created_workspaces:
            self.geoserverServer.delete_workspace(workspace)

        for pg_layer in self.created_pg_layers:
            pg_layer.drop()
