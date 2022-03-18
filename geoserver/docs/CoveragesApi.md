# geoserver.CoveragesApi

All URIs are relative to *http://localhost:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_coverage_at_store**](CoveragesApi.md#create_coverage_at_store) | **POST** /workspaces/{workspace}/coveragestores/{store}/coverages | 
[**create_coverage_at_workspace**](CoveragesApi.md#create_coverage_at_workspace) | **POST** /workspaces/{workspace}/coverages | 
[**delete_coverage**](CoveragesApi.md#delete_coverage) | **DELETE** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage} | 
[**find_coverage_by_store**](CoveragesApi.md#find_coverage_by_store) | **GET** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage} | 
[**find_coverages_by_store**](CoveragesApi.md#find_coverages_by_store) | **GET** /workspaces/{workspace}/coveragestores/{store}/coverages | 
[**find_coverages_by_workspace**](CoveragesApi.md#find_coverages_by_workspace) | **GET** /workspaces/{workspace}/coverages | 
[**get_coverage_at_workspace**](CoveragesApi.md#get_coverage_at_workspace) | **GET** /workspaces/{workspace}/coverages/{coverage} | 
[**update_coverage**](CoveragesApi.md#update_coverage) | **PUT** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage} | 

# **create_coverage_at_store**
> create_coverage_at_store(body, workspace, store)



Create a new coverage, the underlying data store must exists.

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
api_instance = geoserver.CoveragesApi(geoserver.ApiClient(configuration))
body = geoserver.CoverageInfoWrapper() # CoverageInfoWrapper | The body of the coverage to POST
workspace = 'workspace_example' # str | The name of the workspace
store = 'store_example' # str | The name of the coverage data store

try:
    api_instance.create_coverage_at_store(body, workspace, store)
except ApiException as e:
    print("Exception when calling CoveragesApi->create_coverage_at_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CoverageInfoWrapper**](CoverageInfoWrapper.md)| The body of the coverage to POST | 
 **workspace** | **str**| The name of the workspace | 
 **store** | **str**| The name of the coverage data store | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_coverage_at_workspace**
> create_coverage_at_workspace(body, workspace)



Create a new coverage, the coverage definition needs to reference a store.

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
api_instance = geoserver.CoveragesApi(geoserver.ApiClient(configuration))
body = geoserver.CoverageInfoWrapper() # CoverageInfoWrapper | The body of the coverage to POST
workspace = 'workspace_example' # str | The name of the workspace

try:
    api_instance.create_coverage_at_workspace(body, workspace)
except ApiException as e:
    print("Exception when calling CoveragesApi->create_coverage_at_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CoverageInfoWrapper**](CoverageInfoWrapper.md)| The body of the coverage to POST | 
 **workspace** | **str**| The name of the workspace | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_coverage**
> delete_coverage(workspace, store, coverage, recurse=recurse)



Delete a coverage (optionally recursively deleting layers).

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
api_instance = geoserver.CoveragesApi(geoserver.ApiClient(configuration))
workspace = 'workspace_example' # str | The name of the workspace
store = 'store_example' # str | The name of the coverage datastore
coverage = 'coverage_example' # str | The name of the coverage
recurse = false # bool | The recurse controls recursive deletion. When set to true all stores containing the resource are also removed. (optional) (default to false)

try:
    api_instance.delete_coverage(workspace, store, coverage, recurse=recurse)
except ApiException as e:
    print("Exception when calling CoveragesApi->delete_coverage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the workspace | 
 **store** | **str**| The name of the coverage datastore | 
 **coverage** | **str**| The name of the coverage | 
 **recurse** | **bool**| The recurse controls recursive deletion. When set to true all stores containing the resource are also removed. | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_coverage_by_store**
> CoverageResponseWrapper find_coverage_by_store(workspace, store, coverage, quiet_on_not_found=quiet_on_not_found)



Get an individual coverage.

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
api_instance = geoserver.CoveragesApi(geoserver.ApiClient(configuration))
workspace = 'workspace_example' # str | The name of the workspace
store = 'store_example' # str | The name of the coverage datastore
coverage = 'coverage_example' # str | The name of the coverage
quiet_on_not_found = false # bool | The quietOnNotFound parameter avoids to log an Exception when the coverage is not present. Note that 404 status code will be returned anyway. (optional) (default to false)

try:
    api_response = api_instance.find_coverage_by_store(workspace, store, coverage, quiet_on_not_found=quiet_on_not_found)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoveragesApi->find_coverage_by_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the workspace | 
 **store** | **str**| The name of the coverage datastore | 
 **coverage** | **str**| The name of the coverage | 
 **quiet_on_not_found** | **bool**| The quietOnNotFound parameter avoids to log an Exception when the coverage is not present. Note that 404 status code will be returned anyway. | [optional] [default to false]

### Return type

[**CoverageResponseWrapper**](CoverageResponseWrapper.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_coverages_by_store**
> object find_coverages_by_store(workspace, store, list=list)



Get the coverages available for the provided workspace and data store.

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
api_instance = geoserver.CoveragesApi(geoserver.ApiClient(configuration))
workspace = 'workspace_example' # str | The name of the workspace
store = 'store_example' # str | The name of the coverage data store
list = 'list_example' # str | If the list parameter value is equal to \"all\" all the coverages available in the data source (even the non published ones) will be returned. (optional)

try:
    api_response = api_instance.find_coverages_by_store(workspace, store, list=list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoveragesApi->find_coverages_by_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the workspace | 
 **store** | **str**| The name of the coverage data store | 
 **list** | **str**| If the list parameter value is equal to \&quot;all\&quot; all the coverages available in the data source (even the non published ones) will be returned. | [optional] 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_coverages_by_workspace**
> object find_coverages_by_workspace(workspace, list=list)



Get the coverages available for the provided workspace.

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
api_instance = geoserver.CoveragesApi(geoserver.ApiClient(configuration))
workspace = 'workspace_example' # str | The name of the workspace
list = 'list_example' # str | If the list parameter value is equal to \"all\" all the coverages available in the data source (even the non published ones) will be returned. (optional)

try:
    api_response = api_instance.find_coverages_by_workspace(workspace, list=list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoveragesApi->find_coverages_by_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the workspace | 
 **list** | **str**| If the list parameter value is equal to \&quot;all\&quot; all the coverages available in the data source (even the non published ones) will be returned. | [optional] 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coverage_at_workspace**
> CoverageResponseWrapper get_coverage_at_workspace(workspace, coverage, quiet_on_not_found=quiet_on_not_found)



Get an individual coverage.

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
api_instance = geoserver.CoveragesApi(geoserver.ApiClient(configuration))
workspace = 'workspace_example' # str | The name of the workspace
coverage = 'coverage_example' # str | The name of the coverage
quiet_on_not_found = true # bool | The quietOnNotFound parameter avoids to log an Exception when the coverage is not present. Note that 404 status code will be returned anyway. (optional) (default to true)

try:
    api_response = api_instance.get_coverage_at_workspace(workspace, coverage, quiet_on_not_found=quiet_on_not_found)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoveragesApi->get_coverage_at_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the workspace | 
 **coverage** | **str**| The name of the coverage | 
 **quiet_on_not_found** | **bool**| The quietOnNotFound parameter avoids to log an Exception when the coverage is not present. Note that 404 status code will be returned anyway. | [optional] [default to true]

### Return type

[**CoverageResponseWrapper**](CoverageResponseWrapper.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_coverage**
> update_coverage(body, workspace, store, coverage, calculate=calculate)



Update an individual coverage

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
api_instance = geoserver.CoveragesApi(geoserver.ApiClient(configuration))
body = geoserver.CoverageInfoWrapper() # CoverageInfoWrapper | The body of the coverage to POST
workspace = 'workspace_example' # str | The name of the workspace
store = 'store_example' # str | The name of the coverage datastore
coverage = 'coverage_example' # str | The name of the coverage
calculate = ['calculate_example'] # list[str] | Comma-seperated list of optional fields to calculate. Optional fields include: \"nativebbox\", \"latlonbbox\". (optional)

try:
    api_instance.update_coverage(body, workspace, store, coverage, calculate=calculate)
except ApiException as e:
    print("Exception when calling CoveragesApi->update_coverage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CoverageInfoWrapper**](CoverageInfoWrapper.md)| The body of the coverage to POST | 
 **workspace** | **str**| The name of the workspace | 
 **store** | **str**| The name of the coverage datastore | 
 **coverage** | **str**| The name of the coverage | 
 **calculate** | [**list[str]**](str.md)| Comma-seperated list of optional fields to calculate. Optional fields include: \&quot;nativebbox\&quot;, \&quot;latlonbbox\&quot;. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

