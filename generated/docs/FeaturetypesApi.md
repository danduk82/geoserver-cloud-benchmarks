# geoserver.FeaturetypesApi

All URIs are relative to *http://localhost:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_feature_type**](FeaturetypesApi.md#create_feature_type) | **POST** /workspaces/{workspaceName}/featuretypes | 
[**create_feature_type_on_store**](FeaturetypesApi.md#create_feature_type_on_store) | **POST** /workspaces/{workspaceName}/datastores/{storeName}/featuretypes | 
[**delete_feature_type**](FeaturetypesApi.md#delete_feature_type) | **DELETE** /workspaces/{workspaceName}/featuretypes/{featureTypeName} | 
[**delete_feature_type_by_store**](FeaturetypesApi.md#delete_feature_type_by_store) | **DELETE** /workspaces/{workspaceName}/datastores/{storeName}/featuretypes/{featureTypeName}. | 
[**get_feature_type**](FeaturetypesApi.md#get_feature_type) | **GET** /workspaces/{workspaceName}/datastores/{storeName}/featuretypes/{featureTypeName}. | 
[**get_feature_type_by_default_store**](FeaturetypesApi.md#get_feature_type_by_default_store) | **GET** /workspaces/{workspaceName}/featuretypes/{featureTypeName} | 
[**get_feature_types_by_store**](FeaturetypesApi.md#get_feature_types_by_store) | **GET** /workspaces/{workspaceName}/datastores/{storeName}/featuretypes | 
[**get_feature_types_by_workspace**](FeaturetypesApi.md#get_feature_types_by_workspace) | **GET** /workspaces/{workspaceName}/featuretypes | 
[**modify_feature_type**](FeaturetypesApi.md#modify_feature_type) | **PUT** /workspaces/{workspaceName}/featuretypes/{featureTypeName} | 
[**modify_feature_type_by_store**](FeaturetypesApi.md#modify_feature_type_by_store) | **PUT** /workspaces/{workspaceName}/datastores/{storeName}/featuretypes/{featureTypeName}. | 

# **create_feature_type**
> create_feature_type(body, workspace_name)



Create a new feature type, the feature type definition needs to reference a store. Note -  when creating a new feature type via POST, if no underlying dataset with the specified name exists an attempt will be made to create it. This will work only in cases where the underlying data format supports the creation of new types (such as a database). When creating a feature type in this manner the client should include all attribute information in the feature type representation. 

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
api_instance = geoserver.FeaturetypesApi(geoserver.ApiClient(configuration))
body = geoserver.FeatureTypeInfoWrapper() # FeatureTypeInfoWrapper | The body of the feature type to POST
workspace_name = 'workspace_name_example' # str | The name of the workspace

try:
    api_instance.create_feature_type(body, workspace_name)
except ApiException as e:
    print("Exception when calling FeaturetypesApi->create_feature_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FeatureTypeInfoWrapper**](FeatureTypeInfoWrapper.md)| The body of the feature type to POST | 
 **workspace_name** | **str**| The name of the workspace | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_feature_type_on_store**
> create_feature_type_on_store(body, workspace_name, store_name)



Create a new feature type. Note -  when creating a new feature type via POST, if no underlying dataset with the specified name exists an attempt will be made to create it. This will work only in cases where the underlying data format supports the creation of new types (such as a database). When creating a feature type in this manner the client should include all attribute information in the feature type representation. 

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
api_instance = geoserver.FeaturetypesApi(geoserver.ApiClient(configuration))
body = geoserver.FeatureTypeInfoWrapper() # FeatureTypeInfoWrapper | The body of the feature type to POST
workspace_name = 'workspace_name_example' # str | The name of the workspace
store_name = 'store_name_example' # str | The name of the datastore

try:
    api_instance.create_feature_type_on_store(body, workspace_name, store_name)
except ApiException as e:
    print("Exception when calling FeaturetypesApi->create_feature_type_on_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FeatureTypeInfoWrapper**](FeatureTypeInfoWrapper.md)| The body of the feature type to POST | 
 **workspace_name** | **str**| The name of the workspace | 
 **store_name** | **str**| The name of the datastore | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_feature_type**
> delete_feature_type(workspace_name, feature_type_name, recurse=recurse)



Delete a feature type in the default data store for the workspace (optionally recursively deleting layers).

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
api_instance = geoserver.FeaturetypesApi(geoserver.ApiClient(configuration))
workspace_name = 'workspace_name_example' # str | The name of the workspace
feature_type_name = 'feature_type_name_example' # str | The name of the feature type
recurse = false # bool | Recursively deletes all layers referenced by the specified featuretype. Allowed values for this parameter are true or false. The default value is false. A request with 'recurse=false' will fail if any layers reference the featuretype. (optional) (default to false)

try:
    api_instance.delete_feature_type(workspace_name, feature_type_name, recurse=recurse)
except ApiException as e:
    print("Exception when calling FeaturetypesApi->delete_feature_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the workspace | 
 **feature_type_name** | **str**| The name of the feature type | 
 **recurse** | **bool**| Recursively deletes all layers referenced by the specified featuretype. Allowed values for this parameter are true or false. The default value is false. A request with &#x27;recurse&#x3D;false&#x27; will fail if any layers reference the featuretype. | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_feature_type_by_store**
> delete_feature_type_by_store(workspace_name, store_name, feature_type_name, recurse=recurse)



Delete a feature type (optionally recursively deleting layers).

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
api_instance = geoserver.FeaturetypesApi(geoserver.ApiClient(configuration))
workspace_name = 'workspace_name_example' # str | The name of the workspace
store_name = 'store_name_example' # str | The name of the datastore
feature_type_name = 'feature_type_name_example' # str | The name of the feature type
recurse = false # bool | Recursively deletes all layers referenced by the specified featuretype. Allowed values for this parameter are true or false. The default value is false. A request with 'recurse=false' will fail if any layers reference the featuretype. (optional) (default to false)

try:
    api_instance.delete_feature_type_by_store(workspace_name, store_name, feature_type_name, recurse=recurse)
except ApiException as e:
    print("Exception when calling FeaturetypesApi->delete_feature_type_by_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the workspace | 
 **store_name** | **str**| The name of the datastore | 
 **feature_type_name** | **str**| The name of the feature type | 
 **recurse** | **bool**| Recursively deletes all layers referenced by the specified featuretype. Allowed values for this parameter are true or false. The default value is false. A request with &#x27;recurse&#x3D;false&#x27; will fail if any layers reference the featuretype. | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_type**
> FeatureTypeResponseWrapper get_feature_type(workspace_name, store_name, feature_type_name, quiet_on_not_found=quiet_on_not_found)



Get an individual feature type

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
api_instance = geoserver.FeaturetypesApi(geoserver.ApiClient(configuration))
workspace_name = 'workspace_name_example' # str | The name of the workspace
store_name = 'store_name_example' # str | The name of the datastore
feature_type_name = 'feature_type_name_example' # str | The name of the feature type
quiet_on_not_found = false # bool | Prevents logging an Exception when the feature type is not present. Note that 404 status code will be returned anyway. Defaults to \"false\". (optional) (default to false)

try:
    api_response = api_instance.get_feature_type(workspace_name, store_name, feature_type_name, quiet_on_not_found=quiet_on_not_found)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturetypesApi->get_feature_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the workspace | 
 **store_name** | **str**| The name of the datastore | 
 **feature_type_name** | **str**| The name of the feature type | 
 **quiet_on_not_found** | **bool**| Prevents logging an Exception when the feature type is not present. Note that 404 status code will be returned anyway. Defaults to \&quot;false\&quot;. | [optional] [default to false]

### Return type

[**FeatureTypeResponseWrapper**](FeatureTypeResponseWrapper.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_type_by_default_store**
> FeatureTypeResponseWrapper get_feature_type_by_default_store(workspace_name, feature_type_name, quiet_on_not_found=quiet_on_not_found)



Get an individual feature type in the default data store for the workspace

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
api_instance = geoserver.FeaturetypesApi(geoserver.ApiClient(configuration))
workspace_name = 'workspace_name_example' # str | The name of the workspace
feature_type_name = 'feature_type_name_example' # str | The name of the feature type
quiet_on_not_found = false # bool | Prevents logging an Exception when the feature type is not present. Note that 404 status code will be returned anyway. Defaults to \"false\". (optional) (default to false)

try:
    api_response = api_instance.get_feature_type_by_default_store(workspace_name, feature_type_name, quiet_on_not_found=quiet_on_not_found)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturetypesApi->get_feature_type_by_default_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the workspace | 
 **feature_type_name** | **str**| The name of the feature type | 
 **quiet_on_not_found** | **bool**| Prevents logging an Exception when the feature type is not present. Note that 404 status code will be returned anyway. Defaults to \&quot;false\&quot;. | [optional] [default to false]

### Return type

[**FeatureTypeResponseWrapper**](FeatureTypeResponseWrapper.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_types_by_store**
> FeatureTypeList get_feature_types_by_store(workspace_name, store_name, list=list, quiet_on_not_found=quiet_on_not_found)



Get a list of feature types for the workspace and datastore. 

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
api_instance = geoserver.FeaturetypesApi(geoserver.ApiClient(configuration))
workspace_name = 'workspace_name_example' # str | The name of the workspace
store_name = 'store_name_example' # str | The name of the datastore
list = 'list_example' # str | The list parameter is used to control the category of feature types that are returned. Must be one of \"configured\", \"available\", \"available_with_geom\", \"all\"  (optional)
quiet_on_not_found = true # bool |  (optional) (default to true)

try:
    api_response = api_instance.get_feature_types_by_store(workspace_name, store_name, list=list, quiet_on_not_found=quiet_on_not_found)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturetypesApi->get_feature_types_by_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the workspace | 
 **store_name** | **str**| The name of the datastore | 
 **list** | **str**| The list parameter is used to control the category of feature types that are returned. Must be one of \&quot;configured\&quot;, \&quot;available\&quot;, \&quot;available_with_geom\&quot;, \&quot;all\&quot;  | [optional] 
 **quiet_on_not_found** | **bool**|  | [optional] [default to true]

### Return type

[**FeatureTypeList**](FeatureTypeList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_types_by_workspace**
> FeatureTypeList get_feature_types_by_workspace(workspace_name, list=list)



Get a list of all feature types for all datastors in the workspace. 

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
api_instance = geoserver.FeaturetypesApi(geoserver.ApiClient(configuration))
workspace_name = 'workspace_name_example' # str | The name of the workspace
list = 'list_example' # str | The list parameter is used to control the category of feature types that are returned. Must be one of \"configured\", \"available\", \"available_with_geom\", \"all\"  (optional)

try:
    api_response = api_instance.get_feature_types_by_workspace(workspace_name, list=list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturetypesApi->get_feature_types_by_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_name** | **str**| The name of the workspace | 
 **list** | **str**| The list parameter is used to control the category of feature types that are returned. Must be one of \&quot;configured\&quot;, \&quot;available\&quot;, \&quot;available_with_geom\&quot;, \&quot;all\&quot;  | [optional] 

### Return type

[**FeatureTypeList**](FeatureTypeList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_feature_type**
> modify_feature_type(body, workspace_name, feature_type_name, recalculate=recalculate)



Update an individual feature type in the default data store for the workspace

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
api_instance = geoserver.FeaturetypesApi(geoserver.ApiClient(configuration))
body = geoserver.FeatureTypeInfoWrapper() # FeatureTypeInfoWrapper | The body of the feature type to POST
workspace_name = 'workspace_name_example' # str | The name of the workspace
feature_type_name = 'feature_type_name_example' # str | The name of the feature type
recalculate = ['recalculate_example'] # list[str] | Specifies whether to recalculate any bounding boxes for a feature type. Some properties of feature types are automatically recalculated when necessary. In particular, the native bounding box is recalculated when the projection or projection policy are changed, and the lat/lon bounding box is recalculated when the native bounding box is recalculated, or when a new native bounding box is explicitly provided in the request. (The native and lat/lon bounding boxes are not automatically recalculated when they are explicitly included in the request.) In addition, the client may explicitly request a fixed set of fields to calculate, by including a comma-separated list of their names in the recalculate parameter.  The empty parameter 'recalculate=' is useful avoid slow recalculation when operating against large datasets as 'recalculate=' avoids calculating any fields, regardless of any changes to projection, projection policy, etc. The nativebbox parameter 'recalculate=nativebbox' is used recalculates the native bounding box, while avoiding recalculating the lat/lon bounding box. Recalculate parameters can be used in together - 'recalculate=nativebbox,latlonbbox' can be used after a bulk import to  to recalculates both the native bounding box and the lat/lon bounding box. (optional)

try:
    api_instance.modify_feature_type(body, workspace_name, feature_type_name, recalculate=recalculate)
except ApiException as e:
    print("Exception when calling FeaturetypesApi->modify_feature_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FeatureTypeInfoWrapper**](FeatureTypeInfoWrapper.md)| The body of the feature type to POST | 
 **workspace_name** | **str**| The name of the workspace | 
 **feature_type_name** | **str**| The name of the feature type | 
 **recalculate** | [**list[str]**](str.md)| Specifies whether to recalculate any bounding boxes for a feature type. Some properties of feature types are automatically recalculated when necessary. In particular, the native bounding box is recalculated when the projection or projection policy are changed, and the lat/lon bounding box is recalculated when the native bounding box is recalculated, or when a new native bounding box is explicitly provided in the request. (The native and lat/lon bounding boxes are not automatically recalculated when they are explicitly included in the request.) In addition, the client may explicitly request a fixed set of fields to calculate, by including a comma-separated list of their names in the recalculate parameter.  The empty parameter &#x27;recalculate&#x3D;&#x27; is useful avoid slow recalculation when operating against large datasets as &#x27;recalculate&#x3D;&#x27; avoids calculating any fields, regardless of any changes to projection, projection policy, etc. The nativebbox parameter &#x27;recalculate&#x3D;nativebbox&#x27; is used recalculates the native bounding box, while avoiding recalculating the lat/lon bounding box. Recalculate parameters can be used in together - &#x27;recalculate&#x3D;nativebbox,latlonbbox&#x27; can be used after a bulk import to  to recalculates both the native bounding box and the lat/lon bounding box. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_feature_type_by_store**
> modify_feature_type_by_store(body, workspace_name, store_name, feature_type_name, recalculate=recalculate)



Update an individual feature type

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
api_instance = geoserver.FeaturetypesApi(geoserver.ApiClient(configuration))
body = geoserver.FeatureTypeInfoWrapper() # FeatureTypeInfoWrapper | The body of the feature type to POST
workspace_name = 'workspace_name_example' # str | The name of the workspace
store_name = 'store_name_example' # str | The name of the datastore
feature_type_name = 'feature_type_name_example' # str | The name of the feature type
recalculate = ['recalculate_example'] # list[str] | Specifies whether to recalculate any bounding boxes for a feature type. Some properties of feature types are automatically recalculated when necessary. In particular, the native bounding box is recalculated when the projection or projection policy are changed, and the lat/lon bounding box is recalculated when the native bounding box is recalculated, or when a new native bounding box is explicitly provided in the request. (The native and lat/lon bounding boxes are not automatically recalculated when they are explicitly included in the request.) In addition, the client may explicitly request a fixed set of fields to calculate, by including a comma-separated list of their names in the recalculate parameter.  The empty parameter 'recalculate=' is useful avoid slow recalculation when operating against large datasets as 'recalculate=' avoids calculating any fields, regardless of any changes to projection, projection policy, etc. The nativebbox parameter 'recalculate=nativebbox' is used recalculates the native bounding box, while avoiding recalculating the lat/lon bounding box. Recalculate parameters can be used in together - 'recalculate=nativebbox,latlonbbox' can be used after a bulk import to  to recalculates both the native bounding box and the lat/lon bounding box. (optional)

try:
    api_instance.modify_feature_type_by_store(body, workspace_name, store_name, feature_type_name, recalculate=recalculate)
except ApiException as e:
    print("Exception when calling FeaturetypesApi->modify_feature_type_by_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FeatureTypeInfoWrapper**](FeatureTypeInfoWrapper.md)| The body of the feature type to POST | 
 **workspace_name** | **str**| The name of the workspace | 
 **store_name** | **str**| The name of the datastore | 
 **feature_type_name** | **str**| The name of the feature type | 
 **recalculate** | [**list[str]**](str.md)| Specifies whether to recalculate any bounding boxes for a feature type. Some properties of feature types are automatically recalculated when necessary. In particular, the native bounding box is recalculated when the projection or projection policy are changed, and the lat/lon bounding box is recalculated when the native bounding box is recalculated, or when a new native bounding box is explicitly provided in the request. (The native and lat/lon bounding boxes are not automatically recalculated when they are explicitly included in the request.) In addition, the client may explicitly request a fixed set of fields to calculate, by including a comma-separated list of their names in the recalculate parameter.  The empty parameter &#x27;recalculate&#x3D;&#x27; is useful avoid slow recalculation when operating against large datasets as &#x27;recalculate&#x3D;&#x27; avoids calculating any fields, regardless of any changes to projection, projection policy, etc. The nativebbox parameter &#x27;recalculate&#x3D;nativebbox&#x27; is used recalculates the native bounding box, while avoiding recalculating the lat/lon bounding box. Recalculate parameters can be used in together - &#x27;recalculate&#x3D;nativebbox,latlonbbox&#x27; can be used after a bulk import to  to recalculates both the native bounding box and the lat/lon bounding box. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

