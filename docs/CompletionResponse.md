# CompletionResponse

A completion response from the model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**choices** | [**List[CompletionResponseChoicesInner]**](CompletionResponseChoicesInner.md) |  | [optional] 
**id** | **str** |  | [optional] 
**model** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.completion_response import CompletionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CompletionResponse from a JSON string
completion_response_instance = CompletionResponse.from_json(json)
# print the JSON string representation of the object
print(CompletionResponse.to_json())

# convert the object into a dict
completion_response_dict = completion_response_instance.to_dict()
# create an instance of CompletionResponse from a dict
completion_response_from_dict = CompletionResponse.from_dict(completion_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


