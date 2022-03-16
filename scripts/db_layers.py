#!/usr/bin/env python

from __future__ import print_function

import os
import sys
import time

# FIXME: this is dirty
# sys.path.append("./generated")
import os.path

import geoserver
from geoserver.rest import ApiException

from pprint import pprint
import string
import random

# A bit of dirty globals
GEOSERVER_URL = (
    os.getenv("GEOSERVER_URL", "http://localhost:8085/geoserver-cloud").strip("/")
    + "/rest"
)
GEOSERVER_USERNAME = os.getenv("GEOSERVER_USERNAME", "admin")
GEOSERVER_PASSWORD = os.getenv("GEOSERVER_PASSWORD", "geoserver")


configuration = geoserver.Configuration()
configuration.host = GEOSERVER_URL
configuration.username = GEOSERVER_USERNAME
configuration.password = GEOSERVER_PASSWORD


# create a new workspace
worskpace_name = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))


api_instance = geoserver.WorkspacesApi(geoserver.ApiClient(configuration))
body = geoserver.WorkspaceWrapper(
    geoserver.WorkspaceInfo(worskpace_name)
)  # WorkspaceWrapper | The Workspace body information to upload.
default = False  # bool | New workspace will be the used as the default. Allowed values are true or false,  The default value is false. (optional) (default to false)

try:
    # add a new workspace to GeoServer
    api_instance.create_workspace(body, default=default)
except ApiException as e:
    print("Exception when calling WorkspacesApi->create_workspace: %s\n" % e)


# check that it is there
api_instance = geoserver.WorkspacesApi(geoserver.ApiClient(configuration))

try:
    # Get a list of workspaces
    api_response = api_instance.get_workspaces()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->get_workspaces: %s\n" % e)
