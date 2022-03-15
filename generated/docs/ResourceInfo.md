# ResourceInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the resource. This name corresponds to the \&quot;published\&quot; name of the resource. | [optional] 
**native_name** | **str** | The native name of the resource. This name corresponds to the physical resource that feature type is derived from -- a shapefile name, a database table, etc... | 
**namespace** | [**NamespaceInfo**](NamespaceInfo.md) |  | [optional] 
**title** | **str** | The title of the resource. | [optional] 
**abstract** | **str** | the abstract for the resource. | [optional] 
**description** | **str** | A description of the resource. This is usually something that is to be displayed in a user interface. | [optional] 
**enabled** | **bool** | A flag indicating if the resource is enabled or not. | [optional] 
**alias** | **list[str]** | A set of aliases or alternative names that the resource is also known by. | [optional] 
**data_links** | [**list[DataLinkInfo]**](DataLinkInfo.md) | A collection of data links for the resource. | [optional] 
**disabled_services** | **list[str]** | a list of disabled services names for this resource (e.g. [WMS, WCS]) | [optional] 
**keywords** | [**list[KeywordInfo]**](KeywordInfo.md) | A collection of keywords associated with the resource. | [optional] 
**lat_lon_bounding_box** | [**EnvelopeInfo**](EnvelopeInfo.md) |  | [optional] 
**native_bounding_box** | [**EnvelopeInfo**](EnvelopeInfo.md) |  | [optional] 
**metadatalinks** | [**list[MetadataLinkInfo]**](MetadataLinkInfo.md) |  | [optional] 
**native_crs** | **str** | The native coordinate reference system object of the resource, in WKT format | [optional] 
**srs** | **str** | Returns the identifier of coordinate reference system of the resource. | [optional] 
**projection_policy** | [**ProjectionPolicy**](ProjectionPolicy.md) |  | [optional] 
**advertised** | **bool** | true if the resource existence should be advertised (true by default, unless otherwise set) | [optional] 
**service_configuration** | **bool** | true if the resource will configure services access, false otherwise | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

