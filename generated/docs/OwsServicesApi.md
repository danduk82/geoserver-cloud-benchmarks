# geoserver.OwsServicesApi

All URIs are relative to *http://localhost:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_local_wcs_settings**](OwsServicesApi.md#delete_local_wcs_settings) | **DELETE** /services/wcs/workspaces/{workspace}/settings | 
[**delete_local_wfs_settings**](OwsServicesApi.md#delete_local_wfs_settings) | **DELETE** /services/wfs/workspaces/{workspace}/settings | 
[**delete_local_wms_settings**](OwsServicesApi.md#delete_local_wms_settings) | **DELETE** /services/wms/workspaces/{workspace}/settings | 
[**delete_local_wmts_settings**](OwsServicesApi.md#delete_local_wmts_settings) | **DELETE** /services/wmts/workspaces/{workspace}/settings | 
[**get_local_wcs_settings**](OwsServicesApi.md#get_local_wcs_settings) | **GET** /services/wcs/workspaces/{workspace}/settings | 
[**get_local_wfs_settings**](OwsServicesApi.md#get_local_wfs_settings) | **GET** /services/wfs/workspaces/{workspace}/settings | 
[**get_local_wms_settings**](OwsServicesApi.md#get_local_wms_settings) | **GET** /services/wms/workspaces/{workspace}/settings | 
[**get_local_wmts_settings**](OwsServicesApi.md#get_local_wmts_settings) | **GET** /services/wmts/workspaces/{workspace}/settings | 
[**get_wcs_settings**](OwsServicesApi.md#get_wcs_settings) | **GET** /services/wcs/settings | 
[**get_wfs_settings**](OwsServicesApi.md#get_wfs_settings) | **GET** /services/wfs/settings | 
[**get_wms_settings**](OwsServicesApi.md#get_wms_settings) | **GET** /services/wms/settings | 
[**get_wmts_settings**](OwsServicesApi.md#get_wmts_settings) | **GET** /services/wmts/settings | 
[**update_local_wcs_settings**](OwsServicesApi.md#update_local_wcs_settings) | **PUT** /services/wcs/workspaces/{workspace}/settings | 
[**update_local_wfs_settings**](OwsServicesApi.md#update_local_wfs_settings) | **PUT** /services/wfs/workspaces/{workspace}/settings | 
[**update_local_wms_settings**](OwsServicesApi.md#update_local_wms_settings) | **PUT** /services/wms/workspaces/{workspace}/settings | 
[**update_local_wmts_settings**](OwsServicesApi.md#update_local_wmts_settings) | **PUT** /services/wmts/workspaces/{workspace}/settings | 
[**update_wcs_settings**](OwsServicesApi.md#update_wcs_settings) | **PUT** /services/wcs/settings | 
[**update_wfs_settings**](OwsServicesApi.md#update_wfs_settings) | **PUT** /services/wfs/settings | 
[**update_wms_settings**](OwsServicesApi.md#update_wms_settings) | **PUT** /services/wms/settings | 
[**update_wmts_settings**](OwsServicesApi.md#update_wmts_settings) | **PUT** /services/wmts/settings | 

# **delete_local_wcs_settings**
> delete_local_wcs_settings(workspace)



Deletes a workspace-specific WCS setting.

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
api_instance = geoserver.OwsServicesApi(geoserver.ApiClient(configuration))
workspace = 'workspace_example' # str | The workspace name

try:
    api_instance.delete_local_wcs_settings(workspace)
except ApiException as e:
    print("Exception when calling OwsServicesApi->delete_local_wcs_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_local_wfs_settings**
> delete_local_wfs_settings(workspace)



Deletes a workspace-specific WFS setting.

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
api_instance = geoserver.OwsServicesApi(geoserver.ApiClient(configuration))
workspace = 'workspace_example' # str | The workspace name

try:
    api_instance.delete_local_wfs_settings(workspace)
except ApiException as e:
    print("Exception when calling OwsServicesApi->delete_local_wfs_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_local_wms_settings**
> delete_local_wms_settings(workspace)



Deletes a workspace-specific WMS setting.

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
api_instance = geoserver.OwsServicesApi(geoserver.ApiClient(configuration))
workspace = 'workspace_example' # str | The workspace name

try:
    api_instance.delete_local_wms_settings(workspace)
except ApiException as e:
    print("Exception when calling OwsServicesApi->delete_local_wms_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_local_wmts_settings**
> delete_local_wmts_settings(workspace)



Deletes a workspace-specific WMTS setting.

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
api_instance = geoserver.OwsServicesApi(geoserver.ApiClient(configuration))
workspace = 'workspace_example' # str | The workspace name

try:
    api_instance.delete_local_wmts_settings(workspace)
except ApiException as e:
    print("Exception when calling OwsServicesApi->delete_local_wmts_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_local_wcs_settings**
> WCSInfoWrapper get_local_wcs_settings(workspace)



Retrieves Web Coverage Service settings for a given workspace.

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
api_instance = geoserver.OwsServicesApi(geoserver.ApiClient(configuration))
workspace = 'workspace_example' # str | The workspace name

try:
    api_response = api_instance.get_local_wcs_settings(workspace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OwsServicesApi->get_local_wcs_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 

### Return type

[**WCSInfoWrapper**](WCSInfoWrapper.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_local_wfs_settings**
> WFSInfoWrapper get_local_wfs_settings(workspace)



Retrieves Web Feature Service settings for a given workspace.

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
api_instance = geoserver.OwsServicesApi(geoserver.ApiClient(configuration))
workspace = 'workspace_example' # str | The workspace name

try:
    api_response = api_instance.get_local_wfs_settings(workspace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OwsServicesApi->get_local_wfs_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 

### Return type

[**WFSInfoWrapper**](WFSInfoWrapper.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_local_wms_settings**
> WMSInfoWrapper get_local_wms_settings(workspace)



Retrieves Web Map Service settings for a given workspace.

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
api_instance = geoserver.OwsServicesApi(geoserver.ApiClient(configuration))
workspace = 'workspace_example' # str | The workspace name

try:
    api_response = api_instance.get_local_wms_settings(workspace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OwsServicesApi->get_local_wms_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 

### Return type

[**WMSInfoWrapper**](WMSInfoWrapper.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_local_wmts_settings**
> WMTSInfoWrapper get_local_wmts_settings(workspace)



Retrieves Web Map Service settings for a given workspace.

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
api_instance = geoserver.OwsServicesApi(geoserver.ApiClient(configuration))
workspace = 'workspace_example' # str | The workspace name

try:
    api_response = api_instance.get_local_wmts_settings(workspace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OwsServicesApi->get_local_wmts_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 

### Return type

[**WMTSInfoWrapper**](WMTSInfoWrapper.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wcs_settings**
> WCSInfoWrapper get_wcs_settings()



Retrieves Web Coverage Service global settings..

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
api_instance = geoserver.OwsServicesApi(geoserver.ApiClient(configuration))

try:
    api_response = api_instance.get_wcs_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OwsServicesApi->get_wcs_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WCSInfoWrapper**](WCSInfoWrapper.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wfs_settings**
> WFSInfoWrapper get_wfs_settings()



Retrieves Web Feature Service global settings..

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
api_instance = geoserver.OwsServicesApi(geoserver.ApiClient(configuration))

try:
    api_response = api_instance.get_wfs_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OwsServicesApi->get_wfs_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WFSInfoWrapper**](WFSInfoWrapper.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wms_settings**
> WMSInfoWrapper get_wms_settings()



Retrieves Web Map Service global settings..

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
api_instance = geoserver.OwsServicesApi(geoserver.ApiClient(configuration))

try:
    api_response = api_instance.get_wms_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OwsServicesApi->get_wms_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WMSInfoWrapper**](WMSInfoWrapper.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wmts_settings**
> WMTSInfoWrapper get_wmts_settings()



Retrieves Web Map Tile Service global settings..

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
api_instance = geoserver.OwsServicesApi(geoserver.ApiClient(configuration))

try:
    api_response = api_instance.get_wmts_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OwsServicesApi->get_wmts_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WMTSInfoWrapper**](WMTSInfoWrapper.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_local_wcs_settings**
> update_local_wcs_settings(body, workspace)



Edits a workspace-specific WCS setting.

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
api_instance = geoserver.OwsServicesApi(geoserver.ApiClient(configuration))
body = geoserver.WCSInfoWrapper() # WCSInfoWrapper | Body of the WCS settings
workspace = 'workspace_example' # str | The workspace name

try:
    api_instance.update_local_wcs_settings(body, workspace)
except ApiException as e:
    print("Exception when calling OwsServicesApi->update_local_wcs_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WCSInfoWrapper**](WCSInfoWrapper.md)| Body of the WCS settings | 
 **workspace** | **str**| The workspace name | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_local_wfs_settings**
> update_local_wfs_settings(body, workspace)



Edits a workspace-specific WFS setting.

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
api_instance = geoserver.OwsServicesApi(geoserver.ApiClient(configuration))
body = geoserver.WFSInfoWrapper() # WFSInfoWrapper | Body of the WFS settings
workspace = 'workspace_example' # str | The workspace name

try:
    api_instance.update_local_wfs_settings(body, workspace)
except ApiException as e:
    print("Exception when calling OwsServicesApi->update_local_wfs_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WFSInfoWrapper**](WFSInfoWrapper.md)| Body of the WFS settings | 
 **workspace** | **str**| The workspace name | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_local_wms_settings**
> update_local_wms_settings(body, workspace)



Edits a workspace-specific WMS setting.

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
api_instance = geoserver.OwsServicesApi(geoserver.ApiClient(configuration))
body = geoserver.WMSInfoWrapper() # WMSInfoWrapper | Body of the WMS settings
workspace = 'workspace_example' # str | The workspace name

try:
    api_instance.update_local_wms_settings(body, workspace)
except ApiException as e:
    print("Exception when calling OwsServicesApi->update_local_wms_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WMSInfoWrapper**](WMSInfoWrapper.md)| Body of the WMS settings | 
 **workspace** | **str**| The workspace name | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_local_wmts_settings**
> update_local_wmts_settings(body, workspace)



Edits a workspace-specific WMTS setting.

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
api_instance = geoserver.OwsServicesApi(geoserver.ApiClient(configuration))
body = geoserver.WMTSInfoWrapper() # WMTSInfoWrapper | Body of the WMTS settings
workspace = 'workspace_example' # str | The workspace name

try:
    api_instance.update_local_wmts_settings(body, workspace)
except ApiException as e:
    print("Exception when calling OwsServicesApi->update_local_wmts_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WMTSInfoWrapper**](WMTSInfoWrapper.md)| Body of the WMTS settings | 
 **workspace** | **str**| The workspace name | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_wcs_settings**
> update_wcs_settings(body)



Edits a global WCS setting.

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
api_instance = geoserver.OwsServicesApi(geoserver.ApiClient(configuration))
body = geoserver.WCSInfoWrapper() # WCSInfoWrapper | Body of the WCS settings

try:
    api_instance.update_wcs_settings(body)
except ApiException as e:
    print("Exception when calling OwsServicesApi->update_wcs_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WCSInfoWrapper**](WCSInfoWrapper.md)| Body of the WCS settings | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_wfs_settings**
> update_wfs_settings(body)



Edits a global WFS setting.

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
api_instance = geoserver.OwsServicesApi(geoserver.ApiClient(configuration))
body = geoserver.WFSInfoWrapper() # WFSInfoWrapper | Body of the WFS settings

try:
    api_instance.update_wfs_settings(body)
except ApiException as e:
    print("Exception when calling OwsServicesApi->update_wfs_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WFSInfoWrapper**](WFSInfoWrapper.md)| Body of the WFS settings | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_wms_settings**
> update_wms_settings(body)



Edits a global WMS setting.

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
api_instance = geoserver.OwsServicesApi(geoserver.ApiClient(configuration))
body = geoserver.WMSInfoWrapper() # WMSInfoWrapper | Body of the WMS settings

try:
    api_instance.update_wms_settings(body)
except ApiException as e:
    print("Exception when calling OwsServicesApi->update_wms_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WMSInfoWrapper**](WMSInfoWrapper.md)| Body of the WMS settings | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_wmts_settings**
> update_wmts_settings(body)



Edits a global WMTS setting.

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
api_instance = geoserver.OwsServicesApi(geoserver.ApiClient(configuration))
body = geoserver.WMTSInfoWrapper() # WMTSInfoWrapper | Body of the WMTS settings

try:
    api_instance.update_wmts_settings(body)
except ApiException as e:
    print("Exception when calling OwsServicesApi->update_wmts_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WMTSInfoWrapper**](WMTSInfoWrapper.md)| Body of the WMTS settings | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

