# Completion

A request to complete with the model.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** |  | 
**prompt** | **str** |  | 
**stream** | **bool** |  | [optional] 

## Example

```python
from dreamcatcher.models.completion import Completion

# TODO update the JSON string below
json = "{}"
# create an instance of Completion from a JSON string
completion_instance = Completion.from_json(json)
# print the JSON string representation of the object
print Completion.to_json()

# convert the object into a dict
completion_dict = completion_instance.to_dict()
# create an instance of Completion from a dict
completion_from_dict = Completion.from_dict(completion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


