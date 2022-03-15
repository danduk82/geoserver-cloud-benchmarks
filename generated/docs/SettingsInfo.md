# SettingsInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**title** | **str** | The title of the settings instance | [optional] 
**charset** | **str** | The default character set | [optional] 
**num_decimals** | **int** | A cap on the number of decimals to use when encoding floating point numbers | [optional] 
**online_resource** | **str** | Provider web site (used for default contact information, or service provider information if user has not filled in contact details. | [optional] 
**proxy_base_url** | **str** | The url of a proxy in front of the GeoServer instance. This value is used when a reference back to the GeoServer instance must be made in a response. | [optional] 
**schema_base_url** | **str** | The base url to use when including a reference to an xml schema document in a response. | [optional] 
**verbose** | **bool** | When set to false GeoServer will also take step so to strip out some formating and produce more condensed output. | [optional] 
**local_workspace_includes_prefix** | **bool** | If true local workspace should keep the namespace prefixes in getCapabilities etc... | [optional] 
**show_created_time_columns_in_admin_list** | **bool** | Set whether or not a local workspace should keep namespace prefixes in the getCapabilities | [optional] 
**show_modified_time_columns_in_admin_list** | **bool** |  | [optional] 
**contact** | [**ContactInfo**](ContactInfo.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

