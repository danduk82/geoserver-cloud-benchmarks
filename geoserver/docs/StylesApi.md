# geoserver.StylesApi

All URIs are relative to *http://localhost:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_style_to_layer**](StylesApi.md#add_style_to_layer) | **POST** /layers/{layer}/styles | Add a new style
[**create_style**](StylesApi.md#create_style) | **POST** /styles | Add a new style
[**create_style_by_workspace**](StylesApi.md#create_style_by_workspace) | **POST** /workspaces/{workspace}/styles | Add a new style to a given workspace
[**delete_style**](StylesApi.md#delete_style) | **DELETE** /styles/{style} | Delete style
[**delete_style_by_workspace**](StylesApi.md#delete_style_by_workspace) | **DELETE** /workspaces/{workspace}/styles/{style} | Delete style in a given workspace
[**get_style**](StylesApi.md#get_style) | **GET** /styles/{style} | Retrieve a style
[**get_style_by_workspace**](StylesApi.md#get_style_by_workspace) | **GET** /workspaces/{workspace}/styles/{style} | Retrieve a style from a given workspace
[**get_styles**](StylesApi.md#get_styles) | **GET** /styles | Get a list of styles
[**get_styles_by_layer**](StylesApi.md#get_styles_by_layer) | **GET** /layers/{layer}/styles | Get a list of layer alternate styles
[**get_styles_by_workspace**](StylesApi.md#get_styles_by_workspace) | **GET** /workspaces/{workspace}/styles | Get a list of styles in a given workspace
[**upload_style**](StylesApi.md#upload_style) | **PUT** /styles/{style} | Modify a single style
[**upload_style_by_workspace**](StylesApi.md#upload_style_by_workspace) | **PUT** /workspaces/{workspace}/styles/{style} | Modify a single style in a given workspace

# **add_style_to_layer**
> add_style_to_layer(body, layer, default=default)

Add a new style

Adds a new style entry to the layer. The style named in styleBody must alread exist, and will not be altered by this request.

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
api_instance = geoserver.StylesApi(geoserver.ApiClient(configuration))
body = geoserver.StyleInfoPost() # StyleInfoPost | Style body information naming an existing style to add to the layer
layer = 'layer_example' # str | Name of the layer to manage styles for
default = false # bool | Whether to make this the default style for the layer. (optional) (default to false)

try:
    # Add a new style
    api_instance.add_style_to_layer(body, layer, default=default)
except ApiException as e:
    print("Exception when calling StylesApi->add_style_to_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StyleInfoPost**](StyleInfoPost.md)| Style body information naming an existing style to add to the layer | 
 **layer** | **str**| Name of the layer to manage styles for | 
 **default** | **bool**| Whether to make this the default style for the layer. | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_style**
> str create_style(body, name=name)

Add a new style

Adds a new style entry to the server. Using POST with the `application/xml` or `application/json` content only adds the style info to the catalog and does not upload style content. PUT to `/styles/{style}` to upload the style in this case. Use POST with a style file (`application/vnd.ogc.sld+xml` or `application/vnd.ogc.sld+xml` for SLD; additional style types are added by extensions) to generate a style info and upload the style all at once. Then seperately PUT the style info at `/styles/{style}` to make any desired changes to the generated catalog entry. You can also use POST with a ZIP file to upload a SLD 1.0 (`application/vnd.ogc.sld+xml`) file and any associated icon files, and then separately PUT the style info at /styles/{style}. POST with a ZIP file does not support any other style types. 

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
api_instance = geoserver.StylesApi(geoserver.ApiClient(configuration))
body = geoserver.StyleInfoWrapper() # StyleInfoWrapper | The StyleInfo body of a request.
name = 'name_example' # str | The name of the style. Used only when POSTing a style file or ZIP bundle, to determine the name of the style in the catalog. Generated from the filename if not provided. (optional)

try:
    # Add a new style
    api_response = api_instance.create_style(body, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StylesApi->create_style: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StyleInfoWrapper**](StyleInfoWrapper.md)| The StyleInfo body of a request. | 
 **name** | **str**| The name of the style. Used only when POSTing a style file or ZIP bundle, to determine the name of the style in the catalog. Generated from the filename if not provided. | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/zip
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_style_by_workspace**
> str create_style_by_workspace(body, workspace, name=name)

Add a new style to a given workspace

Adds a new style entry to the server. Using POST with the `application/xml` or `application/json` content only adds the style info to the catalog and does not upload style content. PUT to `/workspaces/{workspace}/styles/{style}` to upload the style in this case. Use POST with a style file (`application/vnd.ogc.sld+xml` or `application/vnd.ogc.sld+xml` for SLD; additional style types are added by extensions) to generate a style info and upload the style all at once. Then seperately PUT the style info at `/workspaces/{workspace}/styles/{style}` to make any desired changes to the generated catalog entry. You can also use POST with a ZIP file to upload a SLD 1.0 (`application/vnd.ogc.sld+xml`) file and any associated icon files, and then separately PUT the style info at /workspaces/{workspace}/styles/{style}. POST with a ZIP file does not support any other style types.

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
api_instance = geoserver.StylesApi(geoserver.ApiClient(configuration))
body = geoserver.StyleInfoWrapper() # StyleInfoWrapper | The StyleInfo body of a request.
workspace = 'workspace_example' # str | Name of workspace
name = 'name_example' # str | The name of the style. Used only when POSTing a style file or ZIP bundle, to determine the name of the style in the catalog. Generated from the filename if not provided. (optional)

try:
    # Add a new style to a given workspace
    api_response = api_instance.create_style_by_workspace(body, workspace, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StylesApi->create_style_by_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StyleInfoWrapper**](StyleInfoWrapper.md)| The StyleInfo body of a request. | 
 **workspace** | **str**| Name of workspace | 
 **name** | **str**| The name of the style. Used only when POSTing a style file or ZIP bundle, to determine the name of the style in the catalog. Generated from the filename if not provided. | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/zip
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_style**
> delete_style(style, purge=purge, recurse=recurse)

Delete style

Deletes a style.

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
api_instance = geoserver.StylesApi(geoserver.ApiClient(configuration))
style = 'style_example' # str | Name of the style to retrieve.
purge = false # bool | Specifies whether the underlying file containing the style should be deleted on disk. (optional) (default to false)
recurse = false # bool | Removes references to the specified style in existing layers. (optional) (default to false)

try:
    # Delete style
    api_instance.delete_style(style, purge=purge, recurse=recurse)
except ApiException as e:
    print("Exception when calling StylesApi->delete_style: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **style** | **str**| Name of the style to retrieve. | 
 **purge** | **bool**| Specifies whether the underlying file containing the style should be deleted on disk. | [optional] [default to false]
 **recurse** | **bool**| Removes references to the specified style in existing layers. | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_style_by_workspace**
> delete_style_by_workspace(workspace, style, purge=purge, recurse=recurse)

Delete style in a given workspace

Deletes a style in a given workspace.

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
api_instance = geoserver.StylesApi(geoserver.ApiClient(configuration))
workspace = 'workspace_example' # str | Name of the workspace for style definitions
style = 'style_example' # str | Name of the style to retrieve.
purge = false # bool | Specifies whether the underlying file containing the style should be deleted on disk. (optional) (default to false)
recurse = false # bool | Removes references to the specified style in existing layers. (optional) (default to false)

try:
    # Delete style in a given workspace
    api_instance.delete_style_by_workspace(workspace, style, purge=purge, recurse=recurse)
except ApiException as e:
    print("Exception when calling StylesApi->delete_style_by_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Name of the workspace for style definitions | 
 **style** | **str**| Name of the style to retrieve. | 
 **purge** | **bool**| Specifies whether the underlying file containing the style should be deleted on disk. | [optional] [default to false]
 **recurse** | **bool**| Removes references to the specified style in existing layers. | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_style**
> StyleInfoWrapper get_style(style)

Retrieve a style

Retrieves a single style. Used to both request the style info and the style defintion body, depending on the media type requested. The media type can be specified either by using the \"Accept:\" header or by appending an extension to the endpoint. For example, a style info can be requested in XML format using \"/styles/{style}.xml\" or \"Accept: application/xml\". (Also available: \"{style}.json\",  \"Accept: application/json\" \"{style}.html\", and \"Accept: text/html\"). The style definition body can be requested by either appending the file extension of the style file (e.g., \"{style}.sld\" or \"{style}.css\") or by specifying the correct media type for the style definition in the \"Accept\" header. Below are common style formats and the corresponding media types that can be used in the Accept header to request the style definition body. - application/vnd.ogc.sld+xml for SLD 1.0.0 SLDs - application/vnd.ogc.se+xml for SLD 1.1.0 SLDs - application/vnd.geoserver.geocss+css for css styles - application/vnd.geoserver.ysld+yaml for ysld styles - application/vnd.geoserver.mbstyle+json for mb styles 

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
api_instance = geoserver.StylesApi(geoserver.ApiClient(configuration))
style = 'style_example' # str | Name of the style to retrieve.

try:
    # Retrieve a style
    api_response = api_instance.get_style(style)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StylesApi->get_style: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **style** | **str**| Name of the style to retrieve. | 

### Return type

[**StyleInfoWrapper**](StyleInfoWrapper.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, application/vnd.ogc.sld+xml, application/vnd.ogc.se+xml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_style_by_workspace**
> StyleInfoWrapper get_style_by_workspace(workspace, style, quiet_on_not_found=quiet_on_not_found)

Retrieve a style from a given workspace

Retrieves a single style. Used to both request the style info and the style defintion body, depending on the media type requested. The media type can be specified either by using the \"Accept:\" header or by appending an extension to the endpoint. For example, a style info can be requested in XML format using \"/styles/{style}.xml\" or \"Accept: application/xml\". (Also available: \"{style}.json\", \"Accept: application/json\" \"{style}.html\", and \"Accept: text/html\"). The style definition body can be requested by either appending the file extension of the style file (e.g., \"{style}.sld\" or \"{style}.css\") or by specifying the correct media type for the style definition in the \"Accept\" header. Below are common style formats and the corresponding media types that can be used in the Accept header to request the style definition body. - application/vnd.ogc.sld+xml for SLD 1.0.0 SLDs - application/vnd.ogc.se+xml for SLD 1.1.0 SLDs - application/vnd.geoserver.geocss+css for css styles - application/vnd.geoserver.ysld+yaml for ysld styles - application/vnd.geoserver.mbstyle+json for mb styles 

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
api_instance = geoserver.StylesApi(geoserver.ApiClient(configuration))
workspace = 'workspace_example' # str | Name of the workspace for style definitions
style = 'style_example' # str | Name of the style to retrieve.
quiet_on_not_found = true # bool |  (optional) (default to true)

try:
    # Retrieve a style from a given workspace
    api_response = api_instance.get_style_by_workspace(workspace, style, quiet_on_not_found=quiet_on_not_found)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StylesApi->get_style_by_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Name of the workspace for style definitions | 
 **style** | **str**| Name of the style to retrieve. | 
 **quiet_on_not_found** | **bool**|  | [optional] [default to true]

### Return type

[**StyleInfoWrapper**](StyleInfoWrapper.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, application/vnd.ogc.sld+xml, application/vnd.ogc.se+xml, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_styles**
> StyleListWrapper get_styles()

Get a list of styles

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
api_instance = geoserver.StylesApi(geoserver.ApiClient(configuration))

try:
    # Get a list of styles
    api_response = api_instance.get_styles()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StylesApi->get_styles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StyleListWrapper**](StyleListWrapper.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_styles_by_layer**
> StyleList get_styles_by_layer(layer)

Get a list of layer alternate styles

Displays a list of all alternate styles for a given layer. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/layers/{layer}/styles.xml\" for XML).

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
api_instance = geoserver.StylesApi(geoserver.ApiClient(configuration))
layer = 'layer_example' # str | Name of the layer to manage styles for

try:
    # Get a list of layer alternate styles
    api_response = api_instance.get_styles_by_layer(layer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StylesApi->get_styles_by_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer** | **str**| Name of the layer to manage styles for | 

### Return type

[**StyleList**](StyleList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_styles_by_workspace**
> StyleListWrapper get_styles_by_workspace(workspace)

Get a list of styles in a given workspace

Displays a list of all styles in a given workspace. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/workspaces/{workspace}/styles.xml\" for XML).

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
api_instance = geoserver.StylesApi(geoserver.ApiClient(configuration))
workspace = 'workspace_example' # str | Name of workspace

try:
    # Get a list of styles in a given workspace
    api_response = api_instance.get_styles_by_workspace(workspace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StylesApi->get_styles_by_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Name of workspace | 

### Return type

[**StyleListWrapper**](StyleListWrapper.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_style**
> upload_style(body, style, raw=raw)

Modify a single style

Modifies a single style. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example `/styles/{style}.xml` for XML). Using PUT with the `application/xml` or `application/json` content modifies the style info in the catalog and does not alter the style content. Using PUT with any other format will modify the content of the style. You can also use PUT with a ZIP file to upload a SLD 1.0 (`application/vnd.ogc.sld+xml`) file and any associated icon files

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
api_instance = geoserver.StylesApi(geoserver.ApiClient(configuration))
body = geoserver.Object() # Object | The style body of a request.
style = 'style_example' # str | Name of the style to retrieve.
raw = false # bool | When set to \"true\", will forgo parsing and encoding of the uploaded style content, and instead the style will be streamed directly to the GeoServer configuration. Use this setting if the content and formatting of the style is to be preserved exactly. May result in an invalid and unusable style if the payload is malformed. Allowable values are \"true\" or \"false\" (default). Only used when uploading a style file. (optional) (default to false)

try:
    # Modify a single style
    api_instance.upload_style(body, style, raw=raw)
except ApiException as e:
    print("Exception when calling StylesApi->upload_style: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Object**| The style body of a request. | 
 **style** | **str**| Name of the style to retrieve. | 
 **raw** | **bool**| When set to \&quot;true\&quot;, will forgo parsing and encoding of the uploaded style content, and instead the style will be streamed directly to the GeoServer configuration. Use this setting if the content and formatting of the style is to be preserved exactly. May result in an invalid and unusable style if the payload is malformed. Allowable values are \&quot;true\&quot; or \&quot;false\&quot; (default). Only used when uploading a style file. | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.geoserver.mbstyle+json, application/vnd.ogc.sld+xml, application/vnd.ogc.se+xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_style_by_workspace**
> upload_style_by_workspace(body, workspace, style, raw=raw)

Modify a single style in a given workspace

Modifies a single style in a given workspace. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example `/workspaces/{workspace}/styles/{style}.xml` for XML). Using PUT with the `application/xml` or `application/json` content modifies the style info in the catalog and does not alter the style content. Using PUT with any other format will modify the content of the style. You can also use PUT with a ZIP file to upload a SLD 1.0 (`application/vnd.ogc.sld+xml`) file and any associated icon files 

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
api_instance = geoserver.StylesApi(geoserver.ApiClient(configuration))
body = geoserver.Object() # Object | The style body of a request.
workspace = 'workspace_example' # str | Name of the workspace for style definitions
style = 'style_example' # str | Name of the style to retrieve.
raw = true # bool | When set to \"true\", will forgo parsing and encoding of the uploaded style content, and instead the style will be streamed directly to the GeoServer configuration. Use this setting if the content and formatting of the style is to be preserved exactly. May result in an invalid and unusable style if the payload is malformed. Allowable values are \"true\" or \"false\" (default). Only used when uploading a style file. (optional)

try:
    # Modify a single style in a given workspace
    api_instance.upload_style_by_workspace(body, workspace, style, raw=raw)
except ApiException as e:
    print("Exception when calling StylesApi->upload_style_by_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Object**| The style body of a request. | 
 **workspace** | **str**| Name of the workspace for style definitions | 
 **style** | **str**| Name of the style to retrieve. | 
 **raw** | **bool**| When set to \&quot;true\&quot;, will forgo parsing and encoding of the uploaded style content, and instead the style will be streamed directly to the GeoServer configuration. Use this setting if the content and formatting of the style is to be preserved exactly. May result in an invalid and unusable style if the payload is malformed. Allowable values are \&quot;true\&quot; or \&quot;false\&quot; (default). Only used when uploading a style file. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.geoserver.mbstyle+json, application/vnd.ogc.sld+xml, application/vnd.ogc.se+xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

