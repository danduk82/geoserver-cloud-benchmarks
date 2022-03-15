# CoverageInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**store** | [**CoverageStoreInfo**](CoverageStoreInfo.md) |  | [optional] 
**native_coverage_name** | **str** | the native coverage name (used to pick up a specific coverage from within a reader) | [optional] 
**native_format** | **str** | The native format name of the coverage | [optional] 
**supported_formats** | **list[str]** | The supported formats for the coverage | [optional] 
**request_srs** | **list[str]** | The collection of identifiers of the crs&#x27;s the coverage supports in a request. | [optional] 
**response_srs** | **list[str]** | The collection of identifiers of the crs&#x27;s the coverage supports in a response. | [optional] 
**default_interpolation_method** | **str** | Default resampling (interpolation) method that will be used for this coverage. | [optional] 
**interpolation_methods** | **list[str]** | available interporlations methods for this coverage | [optional] 
**parameters** | **dict(str, object)** |  | [optional] 
**dimensions** | [**list[CoverageDimensionInfo]**](CoverageDimensionInfo.md) | raster dimensions | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

