# geoserver.NamespacesApi

All URIs are relative to *http://localhost:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_namespace**](NamespacesApi.md#add_namespace) | **POST** /namespaces | Add a new namespace to GeoServer
[**delete_namespace**](NamespacesApi.md#delete_namespace) | **DELETE** /namespaces/{namespacePrefix} | Delete a namespace
[**get_namespace**](NamespacesApi.md#get_namespace) | **GET** /namespaces/{namespacePrefix} | Retrieve a namespace
[**get_namespaces**](NamespacesApi.md#get_namespaces) | **GET** /namespaces | Get a list of namespaces
[**modify_namespace**](NamespacesApi.md#modify_namespace) | **PUT** /namespaces/{namespacePrefix} | Update a namespace

# **add_namespace**
> str add_namespace(body)

Add a new namespace to GeoServer

Adds a new namespace to the server

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
api_instance = geoserver.NamespacesApi(geoserver.ApiClient(configuration))
body = geoserver.NamespaceWrapper() # NamespaceWrapper | The Namespace body information to upload.

try:
    # Add a new namespace to GeoServer
    api_response = api_instance.add_namespace(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespacesApi->add_namespace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NamespaceWrapper**](NamespaceWrapper.md)| The Namespace body information to upload. | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespace**
> delete_namespace(namespace_prefix)

Delete a namespace

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
api_instance = geoserver.NamespacesApi(geoserver.ApiClient(configuration))
namespace_prefix = 'namespace_prefix_example' # str | The name of the namespace to fetch, or \"default\" to get the default namespace.

try:
    # Delete a namespace
    api_instance.delete_namespace(namespace_prefix)
except ApiException as e:
    print("Exception when calling NamespacesApi->delete_namespace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_prefix** | **str**| The name of the namespace to fetch, or \&quot;default\&quot; to get the default namespace. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespace**
> NamespaceWrapper get_namespace(namespace_prefix, quiet_on_not_found=quiet_on_not_found)

Retrieve a namespace

Retrieves a single namespace definition.

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
api_instance = geoserver.NamespacesApi(geoserver.ApiClient(configuration))
namespace_prefix = 'namespace_prefix_example' # str | The name of the namespace to fetch, or \"default\" to get the default namespace.
quiet_on_not_found = true # bool |  (optional) (default to true)

try:
    # Retrieve a namespace
    api_response = api_instance.get_namespace(namespace_prefix, quiet_on_not_found=quiet_on_not_found)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespacesApi->get_namespace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_prefix** | **str**| The name of the namespace to fetch, or \&quot;default\&quot; to get the default namespace. | 
 **quiet_on_not_found** | **bool**|  | [optional] [default to true]

### Return type

[**NamespaceWrapper**](NamespaceWrapper.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaces**
> NamespacesResponse get_namespaces()

Get a list of namespaces

Displays a list of all namespaces on the server.

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
api_instance = geoserver.NamespacesApi(geoserver.ApiClient(configuration))

try:
    # Get a list of namespaces
    api_response = api_instance.get_namespaces()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespacesApi->get_namespaces: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NamespacesResponse**](NamespacesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_namespace**
> modify_namespace(body, namespace_prefix)

Update a namespace

Takes the body of the put and modifies the namespace from it.

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
api_instance = geoserver.NamespacesApi(geoserver.ApiClient(configuration))
body = geoserver.NamespaceWrapper() # NamespaceWrapper | The Namespace body information to upload.
namespace_prefix = 'namespace_prefix_example' # str | The name of the namespace to fetch, or \"default\" to get the default namespace.

try:
    # Update a namespace
    api_instance.modify_namespace(body, namespace_prefix)
except ApiException as e:
    print("Exception when calling NamespacesApi->modify_namespace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NamespaceWrapper**](NamespaceWrapper.md)| The Namespace body information to upload. | 
 **namespace_prefix** | **str**| The name of the namespace to fetch, or \&quot;default\&quot; to get the default namespace. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

