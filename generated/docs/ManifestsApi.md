# geoserver.ManifestsApi

All URIs are relative to *http://localhost:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_component_versions**](ManifestsApi.md#get_component_versions) | **GET** /about/version | 

# **get_component_versions**
> VersionResponse get_component_versions(manifest=manifest, key=key, value=value)



This endpoint shows only the details for the high-level components: GeoServer, GeoTools, and GeoWebCache. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/about/manifest.xml\" for XML).

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
api_instance = geoserver.ManifestsApi(geoserver.ApiClient(configuration))
manifest = 'manifest_example' # str | The manifest parameter is used to filter over resulting resource (manifest) names attribute using Java regular expressions. (optional)
key = 'key_example' # str | Only return manifest entries with this key in their properties. It can be optionally combined with the value parameter. (optional)
value = 'value_example' # str | Only return manifest entries that have this value for the provided key parameter. (optional)

try:
    api_response = api_instance.get_component_versions(manifest=manifest, key=key, value=value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManifestsApi->get_component_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manifest** | **str**| The manifest parameter is used to filter over resulting resource (manifest) names attribute using Java regular expressions. | [optional] 
 **key** | **str**| Only return manifest entries with this key in their properties. It can be optionally combined with the value parameter. | [optional] 
 **value** | **str**| Only return manifest entries that have this value for the provided key parameter. | [optional] 

### Return type

[**VersionResponse**](VersionResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

