# geoserver.LayersApi

All URIs are relative to _http://localhost:8080/geoserver/rest_

| Method                                                                  | HTTP request                                               | Description                          |
| ----------------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------ |
| [**create_layer**](LayersApi.md#create_layer)                           | **POST** /layers                                           | Create a new layer.                  |
| [**delete_layer**](LayersApi.md#delete_layer)                           | **DELETE** /layers/{qualifiedLayerName}                    | Delete layer                         |
| [**delete_layer_by_workspace**](LayersApi.md#delete_layer_by_workspace) | **DELETE** /workspaces/{workspaceName}/layers/{layerName}. | Delete layer                         |
| [**get_layer**](LayersApi.md#get_layer)                                 | **GET** /layers/{qualifiedLayerName}                       | Retrieve a layer                     |
| [**get_layer_by_workspace**](LayersApi.md#get_layer_by_workspace)       | **GET** /workspaces/{workspaceName}/layers/{layerName}.    | Retrieve a layer                     |
| [**get_layers**](LayersApi.md#get_layers)                               | **GET** /layers                                            | Get a list of layers                 |
| [**get_layers_by_workspace**](LayersApi.md#get_layers_by_workspace)     | **GET** /workspaces/{workspaceName}/layers                 | Get a list of layers in a workspace. |
| [**update_layer**](LayersApi.md#update_layer)                           | **PUT** /layers/{qualifiedLayerName}                       | Modify a layer.                      |
| [**update_layer_by_workspace**](LayersApi.md#update_layer_by_workspace) | **PUT** /workspaces/{workspaceName}/layers/{layerName}.    | Modify a layer.                      |

# **create_layer**

> create_layer(body)

Create a new layer.

Creates a new layer on the server.

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
api_instance = geoserver.LayersApi(geoserver.ApiClient(configuration))
body = geoserver.LayerInfoWrapper() # LayerInfoWrapper | The updated layer definition.

try:
    # Create a new layer.
    api_instance.create_layer(body)
except ApiException as e:
    print("Exception when calling LayersApi->create_layer: %s\n" % e)
```

### Parameters

| Name     | Type                                        | Description                   | Notes |
| -------- | ------------------------------------------- | ----------------------------- | ----- |
| **body** | [**LayerInfoWrapper**](LayerInfoWrapper.md) | The updated layer definition. |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_layer**

> delete_layer(qualified_layer_name, recurse=recurse)

Delete layer

Deletes a layer from the server.

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
api_instance = geoserver.LayersApi(geoserver.ApiClient(configuration))
qualified_layer_name = 'qualified_layer_name_example' # str | The name of the layer to retrieve, preferrably including namespace prefix (e.g. \"cite:roads\") to avoid ambiguities
recurse = false # bool | Recursively removes the layer from all layer groups which reference it. If this results in an empty layer group, also delete the layer group. Allowed values for this parameter are true or false. The default value is false. A request with 'recurse=false' will fail if any layer groups reference the layer. (optional) (default to false)

try:
    # Delete layer
    api_instance.delete_layer(qualified_layer_name, recurse=recurse)
except ApiException as e:
    print("Exception when calling LayersApi->delete_layer: %s\n" % e)
```

### Parameters

| Name                     | Type     | Description                                                                                                                                                                                                                                                                                                                     | Notes                         |
| ------------------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| **qualified_layer_name** | **str**  | The name of the layer to retrieve, preferrably including namespace prefix (e.g. \&quot;cite:roads\&quot;) to avoid ambiguities                                                                                                                                                                                                  |
| **recurse**              | **bool** | Recursively removes the layer from all layer groups which reference it. If this results in an empty layer group, also delete the layer group. Allowed values for this parameter are true or false. The default value is false. A request with &#x27;recurse&#x3D;false&#x27; will fail if any layer groups reference the layer. | [optional] [default to false] |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_layer_by_workspace**

> delete_layer_by_workspace(workspace_name, layer_name, recurse=recurse)

Delete layer

Deletes a layer from the server.

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
api_instance = geoserver.LayersApi(geoserver.ApiClient(configuration))
workspace_name = 'workspace_name_example' # str | The name of the workspace the layer is in.
layer_name = 'layer_name_example' # str | The name of the layer to retrieve, *without* workspace prefix, since it's given by the workspaceName parameter already. Request will fail otherwise.
recurse = false # bool | Recursively removes the layer from all layer groups which reference it. If this results in an empty layer group, also delete the layer group. Allowed values for this parameter are true or false. The default value is false. A request with 'recurse=false' will fail if any layer groups reference the layer. (optional) (default to false)

try:
    # Delete layer
    api_instance.delete_layer_by_workspace(workspace_name, layer_name, recurse=recurse)
except ApiException as e:
    print("Exception when calling LayersApi->delete_layer_by_workspace: %s\n" % e)
```

### Parameters

| Name               | Type     | Description                                                                                                                                                                                                                                                                                                                     | Notes                         |
| ------------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| **workspace_name** | **str**  | The name of the workspace the layer is in.                                                                                                                                                                                                                                                                                      |
| **layer_name**     | **str**  | The name of the layer to retrieve, _without_ workspace prefix, since it&#x27;s given by the workspaceName parameter already. Request will fail otherwise.                                                                                                                                                                       |
| **recurse**        | **bool** | Recursively removes the layer from all layer groups which reference it. If this results in an empty layer group, also delete the layer group. Allowed values for this parameter are true or false. The default value is false. A request with &#x27;recurse&#x3D;false&#x27; will fail if any layer groups reference the layer. | [optional] [default to false] |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_layer**

> LayerResponse get_layer(qualified_layer_name)

Retrieve a layer

Retrieves a single layer definition.

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
api_instance = geoserver.LayersApi(geoserver.ApiClient(configuration))
qualified_layer_name = 'qualified_layer_name_example' # str | The name of the layer to retrieve, preferrably including namespace prefix (e.g. \"cite:roads\") to avoid ambiguities

try:
    # Retrieve a layer
    api_response = api_instance.get_layer(qualified_layer_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayersApi->get_layer: %s\n" % e)
```

### Parameters

| Name                     | Type    | Description                                                                                                                    | Notes |
| ------------------------ | ------- | ------------------------------------------------------------------------------------------------------------------------------ | ----- |
| **qualified_layer_name** | **str** | The name of the layer to retrieve, preferrably including namespace prefix (e.g. \&quot;cite:roads\&quot;) to avoid ambiguities |

### Return type

[**LayerResponse**](LayerResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_layer_by_workspace**

> LayerResponse get_layer_by_workspace(workspace_name, layer_name, quiet_on_not_found=quiet_on_not_found)

Retrieve a layer

Retrieves a single layer definition.

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
api_instance = geoserver.LayersApi(geoserver.ApiClient(configuration))
workspace_name = 'workspace_name_example' # str | The name of the workspace the layer is in.
layer_name = 'layer_name_example' # str | The name of the layer to retrieve, *without* workspace prefix, since it's given by the workspaceName parameter already. Request will fail otherwise.
quiet_on_not_found = true # bool |  (optional) (default to true)

try:
    # Retrieve a layer
    api_response = api_instance.get_layer_by_workspace(workspace_name, layer_name, quiet_on_not_found=quiet_on_not_found)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayersApi->get_layer_by_workspace: %s\n" % e)
```

### Parameters

| Name                   | Type     | Description                                                                                                                                               | Notes                        |
| ---------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| **workspace_name**     | **str**  | The name of the workspace the layer is in.                                                                                                                |
| **layer_name**         | **str**  | The name of the layer to retrieve, _without_ workspace prefix, since it&#x27;s given by the workspaceName parameter already. Request will fail otherwise. |
| **quiet_on_not_found** | **bool** |                                                                                                                                                           | [optional] [default to true] |

### Return type

[**LayerResponse**](LayerResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_layers**

> Layers get_layers()

Get a list of layers

Displays a list of all layers on the server.

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
api_instance = geoserver.LayersApi(geoserver.ApiClient(configuration))

try:
    # Get a list of layers
    api_response = api_instance.get_layers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayersApi->get_layers: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**Layers**](Layers.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_layers_by_workspace**

> Layers get_layers_by_workspace(workspace_name)

Get a list of layers in a workspace.

Displays a list of all layers in the provided workspace.

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
api_instance = geoserver.LayersApi(geoserver.ApiClient(configuration))
workspace_name = 'workspace_name_example' # str | The name of the workspace to list layers in

try:
    # Get a list of layers in a workspace.
    api_response = api_instance.get_layers_by_workspace(workspace_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LayersApi->get_layers_by_workspace: %s\n" % e)
```

### Parameters

| Name               | Type    | Description                                 | Notes |
| ------------------ | ------- | ------------------------------------------- | ----- |
| **workspace_name** | **str** | The name of the workspace to list layers in |

### Return type

[**Layers**](Layers.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_layer**

> update_layer(body, qualified_layer_name)

Modify a layer.

Modifies an existing layer on the server.

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
api_instance = geoserver.LayersApi(geoserver.ApiClient(configuration))
body = geoserver.LayerInfoWrapper() # LayerInfoWrapper | The updated layer definition.
qualified_layer_name = 'qualified_layer_name_example' # str | The name of the layer to retrieve, preferrably including namespace prefix (e.g. \"cite:roads\") to avoid ambiguities

try:
    # Modify a layer.
    api_instance.update_layer(body, qualified_layer_name)
except ApiException as e:
    print("Exception when calling LayersApi->update_layer: %s\n" % e)
```

### Parameters

| Name                     | Type                                        | Description                                                                                                                    | Notes |
| ------------------------ | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ----- |
| **body**                 | [**LayerInfoWrapper**](LayerInfoWrapper.md) | The updated layer definition.                                                                                                  |
| **qualified_layer_name** | **str**                                     | The name of the layer to retrieve, preferrably including namespace prefix (e.g. \&quot;cite:roads\&quot;) to avoid ambiguities |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_layer_by_workspace**

> update_layer_by_workspace(body, workspace_name, layer_name)

Modify a layer.

Modifies an existing layer on the server.

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
api_instance = geoserver.LayersApi(geoserver.ApiClient(configuration))
body = geoserver.LayerInfoWrapper() # LayerInfoWrapper | The updated layer definition.
workspace_name = 'workspace_name_example' # str | The name of the workspace the layer is in.
layer_name = 'layer_name_example' # str | The name of the layer to retrieve, *without* workspace prefix, since it's given by the workspaceName parameter already. Request will fail otherwise.

try:
    # Modify a layer.
    api_instance.update_layer_by_workspace(body, workspace_name, layer_name)
except ApiException as e:
    print("Exception when calling LayersApi->update_layer_by_workspace: %s\n" % e)
```

### Parameters

| Name               | Type                                        | Description                                                                                                                                               | Notes |
| ------------------ | ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| **body**           | [**LayerInfoWrapper**](LayerInfoWrapper.md) | The updated layer definition.                                                                                                                             |
| **workspace_name** | **str**                                     | The name of the workspace the layer is in.                                                                                                                |
| **layer_name**     | **str**                                     | The name of the layer to retrieve, _without_ workspace prefix, since it&#x27;s given by the workspaceName parameter already. Request will fail otherwise. |

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
