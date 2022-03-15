# geoserver.CoveragestoresApi

All URIs are relative to *http://localhost:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_coverage_store**](CoveragestoresApi.md#create_coverage_store) | **POST** /workspaces/{workspace}/coveragestores | Add a new coverage store
[**delete_coverage_store**](CoveragestoresApi.md#delete_coverage_store) | **DELETE** /workspaces/{workspace}/coveragestores/{store} | Delete coverage store
[**get_coverage_store**](CoveragestoresApi.md#get_coverage_store) | **GET** /workspaces/{workspace}/coveragestores/{store} | Get a coverage store named {store} in the {workspace} workspace
[**get_coverage_stores**](CoveragestoresApi.md#get_coverage_stores) | **GET** /workspaces/{workspace}/coveragestores | Get a list of all coverage stores in {workspace}
[**modify_coverage_store**](CoveragestoresApi.md#modify_coverage_store) | **PUT** /workspaces/{workspace}/coveragestores/{store} | Modify a single coverage store.

# **create_coverage_store**
> str create_coverage_store(body, workspace)

Add a new coverage store

Adds a new coverage store entry to the server.

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
api_instance = geoserver.CoveragestoresApi(geoserver.ApiClient(configuration))
body = geoserver.CoverageStoreInfoWrapper() # CoverageStoreInfoWrapper | The coverage store body information to upload.
workspace = 'workspace_example' # str | The name of the worskpace containing the coverage stores.

try:
    # Add a new coverage store
    api_response = api_instance.create_coverage_store(body, workspace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoveragestoresApi->create_coverage_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CoverageStoreInfoWrapper**](CoverageStoreInfoWrapper.md)| The coverage store body information to upload. | 
 **workspace** | **str**| The name of the worskpace containing the coverage stores. | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_coverage_store**
> delete_coverage_store(workspace, store, purge=purge, recurse=recurse)

Delete coverage store

Deletes a coverage store

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
api_instance = geoserver.CoveragestoresApi(geoserver.ApiClient(configuration))
workspace = 'workspace_example' # str | The name of the worskpace containing the coverage stores.
store = 'store_example' # str | The name of the store to be retrieved
purge = geoserver.PurgeOption() # PurgeOption | The purge parameter specifies if and how the underlying raster data source is deleted. Allowable values for this parameter are \"none\", \"metadata\", \"all\". When set to \"none\" data and auxiliary files are preserved. When set to \"metadata\" delete only auxiliary files and metadata. It’s recommended when data files (such as granules) should not be deleted from disk. Finally, when set to \"all\" both data and auxiliary files are removed. (optional)
recurse = true # bool | The recurse controls recursive deletion. When set to true all resources contained in the store are also removed. The default value is \"false\". (optional)

try:
    # Delete coverage store
    api_instance.delete_coverage_store(workspace, store, purge=purge, recurse=recurse)
except ApiException as e:
    print("Exception when calling CoveragestoresApi->delete_coverage_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the worskpace containing the coverage stores. | 
 **store** | **str**| The name of the store to be retrieved | 
 **purge** | [**PurgeOption**](.md)| The purge parameter specifies if and how the underlying raster data source is deleted. Allowable values for this parameter are \&quot;none\&quot;, \&quot;metadata\&quot;, \&quot;all\&quot;. When set to \&quot;none\&quot; data and auxiliary files are preserved. When set to \&quot;metadata\&quot; delete only auxiliary files and metadata. It’s recommended when data files (such as granules) should not be deleted from disk. Finally, when set to \&quot;all\&quot; both data and auxiliary files are removed. | [optional] 
 **recurse** | **bool**| The recurse controls recursive deletion. When set to true all resources contained in the store are also removed. The default value is \&quot;false\&quot;. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coverage_store**
> CoverageStoreResponseWrapper get_coverage_store(workspace, store, quiet_on_not_found=quiet_on_not_found)

Get a coverage store named {store} in the {workspace} workspace

Displays a representation of the coverage store.

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
api_instance = geoserver.CoveragestoresApi(geoserver.ApiClient(configuration))
workspace = 'workspace_example' # str | The name of the worskpace containing the coverage stores.
store = 'store_example' # str | The name of the store to be retrieved
quiet_on_not_found = true # bool | When set to true, avoids to log an Exception when the coverage store is not present. Note that 404 status code will be returned anyway. (optional)

try:
    # Get a coverage store named {store} in the {workspace} workspace
    api_response = api_instance.get_coverage_store(workspace, store, quiet_on_not_found=quiet_on_not_found)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoveragestoresApi->get_coverage_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the worskpace containing the coverage stores. | 
 **store** | **str**| The name of the store to be retrieved | 
 **quiet_on_not_found** | **bool**| When set to true, avoids to log an Exception when the coverage store is not present. Note that 404 status code will be returned anyway. | [optional] 

### Return type

[**CoverageStoreResponseWrapper**](CoverageStoreResponseWrapper.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coverage_stores**
> object get_coverage_stores(workspace)

Get a list of all coverage stores in {workspace}

Displays a list of all styles on the server.

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
api_instance = geoserver.CoveragestoresApi(geoserver.ApiClient(configuration))
workspace = 'workspace_example' # str | The name of the worskpace containing the coverage stores.

try:
    # Get a list of all coverage stores in {workspace}
    api_response = api_instance.get_coverage_stores(workspace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoveragestoresApi->get_coverage_stores: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the worskpace containing the coverage stores. | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_coverage_store**
> modify_coverage_store(body, workspace, store)

Modify a single coverage store.

Modifies a single coverage store.

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
api_instance = geoserver.CoveragestoresApi(geoserver.ApiClient(configuration))
body = geoserver.CoverageStoreInfoWrapper() # CoverageStoreInfoWrapper | The coverage store body information to upload.
workspace = 'workspace_example' # str | The name of the worskpace containing the coverage stores.
store = 'store_example' # str | The name of the store to be retrieved

try:
    # Modify a single coverage store.
    api_instance.modify_coverage_store(body, workspace, store)
except ApiException as e:
    print("Exception when calling CoveragestoresApi->modify_coverage_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CoverageStoreInfoWrapper**](CoverageStoreInfoWrapper.md)| The coverage store body information to upload. | 
 **workspace** | **str**| The name of the worskpace containing the coverage stores. | 
 **store** | **str**| The name of the store to be retrieved | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

