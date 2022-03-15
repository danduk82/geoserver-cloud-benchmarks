# geoserver.WorkspacesApi

All URIs are relative to _http://localhost:8080/geoserver/rest_

| Method                                                    | HTTP request                       | Description                      |
| --------------------------------------------------------- | ---------------------------------- | -------------------------------- |
| [**create_workspace**](WorkspacesApi.md#create_workspace) | **POST** /workspaces               | add a new workspace to GeoServer |
| [**delete_workspace**](WorkspacesApi.md#delete_workspace) | **DELETE** /workspaces/{workspace} |
| [**get_workspace**](WorkspacesApi.md#get_workspace)       | **GET** /workspaces/{workspace}    | Retrieve a Workspace             |
| [**get_workspaces**](WorkspacesApi.md#get_workspaces)     | **GET** /workspaces                | Get a list of workspaces         |
| [**modify_workspace**](WorkspacesApi.md#modify_workspace) | **PUT** /workspaces/{workspace}    | Update a workspace               |

# **create_workspace**

> create_workspace(body, default=default)

add a new workspace to GeoServer

Adds a new workspace to the server

### Example

```python
from __future__ import print_function
import time
import geoserver
from geoserver.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = geoserver.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = geoserver.WorkspacesApi(geoserver.ApiClient(configuration))
body = geoserver.WorkspaceWrapper() # WorkspaceWrapper | The Workspace body information to upload.
default = False # bool | New workspace will be the used as the default. Allowed values are true or false,  The default value is false. (optional) (default to false)

try:
    # add a new workspace to GeoServer
    api_instance.create_workspace(body, default=default)
except ApiException as e:
    print("Exception when calling WorkspacesApi->create_workspace: %s\n" % e)
```

### Parameters

| Name        | Type                                        | Description                                                                                                  | Notes                         |
| ----------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ----------------------------- |
| **body**    | [**WorkspaceWrapper**](WorkspaceWrapper.md) | The Workspace body information to upload.                                                                    |
| **default** | **bool**                                    | New workspace will be the used as the default. Allowed values are true or false, The default value is false. | [optional] [default to false] |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workspace**

> delete_workspace(workspace, recurse=recurse)

### Example

```python
from __future__ import print_function
import time
import geoserver
from geoserver.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = geoserver.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = geoserver.WorkspacesApi(geoserver.ApiClient(configuration))
workspace = 'workspace_example' # str | the name of the workspace to fetch
recurse = true # bool | delete workspace contents (default false) (optional)

try:
    api_instance.delete_workspace(workspace, recurse=recurse)
except ApiException as e:
    print("Exception when calling WorkspacesApi->delete_workspace: %s\n" % e)
```

### Parameters

| Name          | Type     | Description                               | Notes      |
| ------------- | -------- | ----------------------------------------- | ---------- |
| **workspace** | **str**  | the name of the workspace to fetch        |
| **recurse**   | **bool** | delete workspace contents (default false) | [optional] |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace**

> object get_workspace(workspace, quiet_on_not_found=quiet_on_not_found)

Retrieve a Workspace

Retrieves a single workspace definition.

### Example

```python
from __future__ import print_function
import time
import geoserver
from geoserver.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = geoserver.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = geoserver.WorkspacesApi(geoserver.ApiClient(configuration))
workspace = 'workspace_example' # str | the name of the workspace to fetch
quiet_on_not_found = True # bool |  (optional) (default to true)

try:
    # Retrieve a Workspace
    api_response = api_instance.get_workspace(workspace, quiet_on_not_found=quiet_on_not_found)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->get_workspace: %s\n" % e)
```

### Parameters

| Name                   | Type     | Description                        | Notes                        |
| ---------------------- | -------- | ---------------------------------- | ---------------------------- |
| **workspace**          | **str**  | the name of the workspace to fetch |
| **quiet_on_not_found** | **bool** |                                    | [optional] [default to true] |

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspaces**

> WorkspacesResponse get_workspaces()

Get a list of workspaces

Displays a list of all workspaces on the server.

### Example

```python
from __future__ import print_function
import time
import geoserver
from geoserver.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = geoserver.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = geoserver.WorkspacesApi(geoserver.ApiClient(configuration))

try:
    # Get a list of workspaces
    api_response = api_instance.get_workspaces()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->get_workspaces: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**WorkspacesResponse**](WorkspacesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_workspace**

> modify_workspace(body, workspace)

Update a workspace

takes the body of the post and modifies the workspace from it.

### Example

```python
from __future__ import print_function
import time
import geoserver
from geoserver.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = geoserver.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = geoserver.WorkspacesApi(geoserver.ApiClient(configuration))
body = geoserver.WorkspaceWrapper() # WorkspaceWrapper | The Workspace body information to upload.
workspace = 'workspace_example' # str | the name of the workspace to fetch

try:
    # Update a workspace
    api_instance.modify_workspace(body, workspace)
except ApiException as e:
    print("Exception when calling WorkspacesApi->modify_workspace: %s\n" % e)
```

### Parameters

| Name          | Type                                        | Description                               | Notes |
| ------------- | ------------------------------------------- | ----------------------------------------- | ----- |
| **body**      | [**WorkspaceWrapper**](WorkspaceWrapper.md) | The Workspace body information to upload. |
| **workspace** | **str**                                     | the name of the workspace to fetch        |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
