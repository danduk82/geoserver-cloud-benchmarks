# WFSInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gml** | [**WFSInfoGmlSettings**](WFSInfoGmlSettings.md) |  | [optional] 
**service_level** | [**WFSServiceLevel**](WFSServiceLevel.md) |  | [optional] 
**max_features** | **int** | Global cap on the number of features to allow when processing a request | [optional] 
**feature_bounding** | **bool** | Flag which determines if gml:bounds elements should be encoded at the feature level in GML output | [optional] 
**canonical_schema_location** | **bool** | Flag that determines the encoding of the WFS schemaLocation. True if the WFS schemaLocation should refer to the canonical location, false if the WFS schemaLocation should refer to a copy served by GeoServer. | [optional] 
**encode_feature_member** | **bool** | Flag that determines encoding of featureMember or featureMembers. True if the featureMember should be encoded False if the featureMembers should be encoded. | [optional] 
**hits_ignore_max_features** | **bool** | Flag that determines if WFS hit requests (counts) will ignore the maximum features limit for this server | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

