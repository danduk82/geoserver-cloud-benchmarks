import geoserver
from geoserver.rest import ApiException
from geoserver import (
    DataStoreInfo,
    DataStoreInfoWrapper,
    ConnectionParameterEntry,
)


class GeoserverAPI:
    def __init__(
        self, geoserver_rest_url, geoserver_username, geoserver_password
    ) -> None:
        self.configuration = geoserver.Configuration()
        self.configuration.host = geoserver_rest_url
        self.configuration.username = geoserver_username
        self.configuration.password = geoserver_password

    def create_workspace(self, workspace_name, default=False):
        api_instance = geoserver.WorkspacesApi(geoserver.ApiClient(self.configuration))
        body = geoserver.WorkspaceWrapper(
            geoserver.WorkspaceInfo(workspace_name)
        )  # WorkspaceWrapper | The Workspace body information to upload.
        try:
            # add a new workspace to GeoServer
            api_instance.create_workspace(body, default=default)
        except ApiException as e:
            print("Exception when calling WorkspacesApi->create_workspace: %s\n" % e)
            return None
        return True

    def get_workspace(self, workspace_name):
        api_instance = geoserver.WorkspacesApi(geoserver.ApiClient(self.configuration))
        try:
            api_response = api_instance.get_workspace(workspace_name)
        except ApiException as e:
            print(
                "Exception when calling Workspaces->get_workspace('%s'): %s\n"
                % (workspace_name, e)
            )
            return None
        return api_response

    def update_workspace(self, workspace_name):
        pass

    def delete_workspace(self, workspace_name):
        api_instance = geoserver.WorkspacesApi(geoserver.ApiClient(self.configuration))
        try:
            # Get a list of workspaces
            api_response = api_instance.delete_workspace(workspace_name, recurse=True)
        except ApiException as e:
            print(
                "Exception when calling WorkspacesApi->delete_workspace(%s): %s\n"
                % (workspace_name, e)
            )
            return None

    def list_workspaces(self):
        api_instance = geoserver.WorkspacesApi(geoserver.ApiClient(self.configuration))
        try:
            # Get a list of workspaces
            api_response = api_instance.get_workspaces()
        except ApiException as e:
            print("Exception when calling WorkspacesApi->get_workspaces: %s\n" % e)
            return None
        workspaces = []
        for w in api_response.to_dict()["workspaces"]["workspace"]:
            workspaces.append(w["name"])
        return workspaces

    def create_pg_store(
        self,
        workspace_name,
        store_name,
        host="172.17.0.1",
        port="5432",
        database="test",
        username="username",
        password="password",
    ):

        api_instance = geoserver.DatastoresApi(geoserver.ApiClient(self.configuration))
        pg_store = DataStoreInfoWrapper(
            DataStoreInfo(
                name=store_name,
                enabled=True,
                workspace=workspace_name,
                connection_parameters={
                    "entry": [
                        ConnectionParameterEntry(key="host", value=host),
                        ConnectionParameterEntry(key="port", value=port),
                        ConnectionParameterEntry(key="database", value=database),
                        ConnectionParameterEntry(key="user", value=username),
                        ConnectionParameterEntry(key="passwd", value=password),
                        ConnectionParameterEntry(key="dbtype", value="postgis"),
                    ]
                },
            )
        )

        try:
            # Create a new data store
            api_instance.create_datastore(pg_store, workspace_name)
        except ApiException as e:
            print("Exception when calling DatastoresApi->create_datastore: %s\n" % e)
        pass

    def delete_pg_store(self, workspace_name, store_name):
        pass

    def get_pg_store(self, workspace_name, store_name):
        pass

    def create_pg_layer(
        self, workspace_name, store_name, layer_name, native_name, feature_type="Point"
    ):
        api_instance = geoserver.FeaturetypesApi(
            geoserver.ApiClient(self.configuration)
        )
        body = geoserver.FeatureTypeInfoWrapper(
            feature_type={
                "name": layer_name,
                "nativeName": native_name,
                "namespace": {"name": workspace_name},
                "title": layer_name,
                "keywords": {"string": ["features", layer_name]},
                "srs": "EPSG:3857",
                "projectionPolicy": "FORCE_DECLARED",
                "enabled": True,
                "store": {
                    "@class": "dataStore",
                    "name": f"{workspace_name}:{store_name}",
                },
                "attributes": {
                    "attribute": [
                        {
                            "name": "name",
                            "minOccurs": 0,
                            "maxOccurs": 1,
                            "nillable": True,
                            "binding": "java.lang.String",
                        },
                        {
                            "name": "geom",
                            "minOccurs": 0,
                            "maxOccurs": 1,
                            "nillable": True,
                            "binding": f"org.locationtech.jts.geom.{feature_type}",
                        },
                    ]
                },
            }
        )
        try:
            api_instance.create_feature_type(body, workspace_name)
        except ApiException as e:
            print(
                "Exception when calling FeaturetypesApi->create_feature_type: %s\n" % e
            )

    def delete_pg_layer(self, workspace_name, store_name, layer_name):
        pass

    def get_pg_layer(self, workspace_name, store_name, layer_name):
        pass

    def create_gwc_layer(self, workspace_name, layer_name):
        pass
