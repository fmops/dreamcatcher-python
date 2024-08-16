# ListModelsResponseDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **float** |  | [optional] 
**id** | **str** |  | [optional] 
**object** | **str** |  | [optional] 
**owned_by** | **str** |  | [optional] 

## Example

```python
from dreamcatcher.models.list_models_response_data_inner import ListModelsResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListModelsResponseDataInner from a JSON string
list_models_response_data_inner_instance = ListModelsResponseDataInner.from_json(json)
# print the JSON string representation of the object
print ListModelsResponseDataInner.to_json()

# convert the object into a dict
list_models_response_data_inner_dict = list_models_response_data_inner_instance.to_dict()
# create an instance of ListModelsResponseDataInner from a dict
list_models_response_data_inner_from_dict = ListModelsResponseDataInner.from_dict(list_models_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


