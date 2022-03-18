# A bit of dirty globals
# GEOSERVER configuration
import os

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