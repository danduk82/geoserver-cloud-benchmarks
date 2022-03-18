# FeatureTypeInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**store** | [**DataStoreInfo**](DataStoreInfo.md) |  | [optional] 
**cql_filter** | **str** | The ECQL string used as default feature type filter | [optional] 
**max_features** | **int** | A cap on the number of features that a query against this type can return. | [optional] 
**num_decimals** | **int** | The number of decimal places to use when encoding floating point numbers from data of this feature type. | [optional] 
**pad_with_zeros** | **bool** |  | [optional] 
**forced_decimal** | **bool** |  | [optional] 
**response_srs** | **list[str]** | The srs codes that the WFS service will advertise in the capabilities document for this feature type (overriding the global WFS settings). | [optional] 
**overriding_service_srs** | **bool** | True if this feature type info is overriding the WFS global SRS list | [optional] 
**skip_number_matched** | **bool** | True if this feature type info is overriding the counting of numberMatched. | [optional] 
**circular_arc_present** | **bool** |  | [optional] 
**encode_measures** | **bool** |  | [optional] 
**linearization_tolerance** | **float** | Tolerance used to linearize this feature type, as an absolute value expressed in the geometries own CRS | [optional] 
**attributes** | [**list[AttributeTypeInfo]**](AttributeTypeInfo.md) | The attributes that the feature type exposes. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

