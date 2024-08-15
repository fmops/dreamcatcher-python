# ShowEndpointResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_moderation_policies** | [**ContentModerationPolicy**](ContentModerationPolicy.md) |  | [optional] 
**dlp_policies** | [**DlpPolicy**](DlpPolicy.md) |  | [optional] 
**dlp_zsner_policies** | [**DlpZsnerPolicy**](DlpZsnerPolicy.md) |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from dreamcatcher.models.show_endpoint_response import ShowEndpointResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ShowEndpointResponse from a JSON string
show_endpoint_response_instance = ShowEndpointResponse.from_json(json)
# print the JSON string representation of the object
print(ShowEndpointResponse.to_json())

# convert the object into a dict
show_endpoint_response_dict = show_endpoint_response_instance.to_dict()
# create an instance of ShowEndpointResponse from a dict
show_endpoint_response_from_dict = ShowEndpointResponse.from_dict(show_endpoint_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


