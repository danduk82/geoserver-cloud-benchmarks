#!/usr/bin/env python

import os
import sys
import time

# FIXME: this is dirty
# sys.path.append("./generated")
import os.path

from api.GeoserverApi import GeoserverAPI

from pprint import pprint
import string
import random

# A bit of dirty globals
# GEOSERVER configuration
GEOSERVER_URL = os.getenv(
    "GEOSERVER_URL", "http://localhost:8085/geoserver-cloud"
).strip("/")
GEOSERVER_REST_URL = os.getenv("GEOSERVER_REST_URL", GEOSERVER_URL + "/rest").strip("/")
GEOSERVER_USERNAME = os.getenv("GEOSERVER_USERNAME", "admin")
GEOSERVER_PASSWORD = os.getenv("GEOSERVER_PASSWORD", "geoserver")

# POSTGIS database
PGUSER = os.getenv("PGUSER", "username")
PGPASSWORD = os.getenv("PGPASSWORD", "password")
PGHOST = os.getenv("PGHOST", "172.17.0.1")
PGPORT = os.getenv("PGPORT", 5432)
PGDATABASE = os.getenv("PGDATABASE", "test")


def main():
    finalCleanup = True
    # create a new workspace
    worskpace_name = "".join(
        random.choices(string.ascii_uppercase + string.digits, k=10)
    )
    pprint(worskpace_name)
    geoserverServer = GeoserverAPI(
        GEOSERVER_REST_URL, GEOSERVER_USERNAME, GEOSERVER_PASSWORD
    )
    geoserverServer.create_workspace(worskpace_name)
    workspaces = geoserverServer.list_workspaces()
    print(workspaces)

    layer_name = "".join(random.choices(string.ascii_lowercase + string.digits, k=10))
    # create one db store
    geoserverServer.create_pg_store(
        worskpace_name, layer_name, PGHOST, PGPORT, PGDATABASE, PGUSER, PGPASSWORD
    )

    if finalCleanup:
        # brutal cleanup at the end
        for workspace in workspaces:
            geoserverServer.delete_workspace(workspace)


if __name__ == "__main__":
    main()