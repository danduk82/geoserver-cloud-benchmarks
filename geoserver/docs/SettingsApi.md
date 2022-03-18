# geoserver.SettingsApi

All URIs are relative to *http://localhost:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_local_settings**](SettingsApi.md#create_local_settings) | **POST** /workspaces/{workspace}/settings | Create workspace-specific settings
[**get_global_contact_info**](SettingsApi.md#get_global_contact_info) | **GET** /settings/contact | Get the global contact information
[**get_local_settings**](SettingsApi.md#get_local_settings) | **GET** /workspaces/{workspace}/settings | Get workspace-specific settings
[**get_settings**](SettingsApi.md#get_settings) | **GET** /settings | Get geoserver global settings
[**update_global_contact_info**](SettingsApi.md#update_global_contact_info) | **PUT** /settings/contact | Update contact settings
[**update_local_settings**](SettingsApi.md#update_local_settings) | **PUT** /workspaces/{workspace}/settings | Update workspace-specific settings
[**update_settings**](SettingsApi.md#update_settings) | **PUT** /settings | Update the global configuration

# **create_local_settings**
> create_local_settings(body, workspace)

Create workspace-specific settings

Create new workspace-specific settings on the server.

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
api_instance = geoserver.SettingsApi(geoserver.ApiClient(configuration))
body = geoserver.SettingsInfoWrapper() # SettingsInfoWrapper | The workspace-specific settings information to upload.
workspace = 'workspace_example' # str | The workspace name

try:
    # Create workspace-specific settings
    api_instance.create_local_settings(body, workspace)
except ApiException as e:
    print("Exception when calling SettingsApi->create_local_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SettingsInfoWrapper**](SettingsInfoWrapper.md)| The workspace-specific settings information to upload. | 
 **workspace** | **str**| The workspace name | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_global_contact_info**
> ContactInfoWrapper get_global_contact_info()

Get the global contact information

Displays a list of all global contact settings on the server. This is a subset of what is available at the /settings endpoint.

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
api_instance = geoserver.SettingsApi(geoserver.ApiClient(configuration))

try:
    # Get the global contact information
    api_response = api_instance.get_global_contact_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->get_global_contact_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ContactInfoWrapper**](ContactInfoWrapper.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_local_settings**
> SettingsInfoWrapper get_local_settings(workspace)

Get workspace-specific settings

Displays all workspace-specific settings.

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
api_instance = geoserver.SettingsApi(geoserver.ApiClient(configuration))
workspace = 'workspace_example' # str | The workspace name

try:
    # Get workspace-specific settings
    api_response = api_instance.get_local_settings(workspace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->get_local_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 

### Return type

[**SettingsInfoWrapper**](SettingsInfoWrapper.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings**
> GeoServerInfoWrapper get_settings()

Get geoserver global settings

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
api_instance = geoserver.SettingsApi(geoserver.ApiClient(configuration))

try:
    # Get geoserver global settings
    api_response = api_instance.get_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->get_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GeoServerInfoWrapper**](GeoServerInfoWrapper.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_global_contact_info**
> update_global_contact_info(body)

Update contact settings

Updates global contact settings on the server.

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
api_instance = geoserver.SettingsApi(geoserver.ApiClient(configuration))
body = geoserver.ContactInfoWrapper() # ContactInfoWrapper | The contact settings information to upload.

try:
    # Update contact settings
    api_instance.update_global_contact_info(body)
except ApiException as e:
    print("Exception when calling SettingsApi->update_global_contact_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ContactInfoWrapper**](ContactInfoWrapper.md)| The contact settings information to upload. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_local_settings**
> update_local_settings(body, workspace)

Update workspace-specific settings

Updates workspace-specific settings on the server.

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
api_instance = geoserver.SettingsApi(geoserver.ApiClient(configuration))
body = geoserver.SettingsInfoWrapper() # SettingsInfoWrapper | The workspace-specific settings information to upload.
workspace = 'workspace_example' # str | The workspace name

try:
    # Update workspace-specific settings
    api_instance.update_local_settings(body, workspace)
except ApiException as e:
    print("Exception when calling SettingsApi->update_local_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SettingsInfoWrapper**](SettingsInfoWrapper.md)| The workspace-specific settings information to upload. | 
 **workspace** | **str**| The workspace name | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_settings**
> update_settings(body)

Update the global configuration

Adds a new data store to the workspace.

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
api_instance = geoserver.SettingsApi(geoserver.ApiClient(configuration))
body = geoserver.GeoServerInfoWrapper() # GeoServerInfoWrapper | global settings upload request body

try:
    # Update the global configuration
    api_instance.update_settings(body)
except ApiException as e:
    print("Exception when calling SettingsApi->update_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GeoServerInfoWrapper**](GeoServerInfoWrapper.md)| global settings upload request body | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

