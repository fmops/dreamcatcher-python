# CreateChatCompletion

Creates a model response for the given chat conversation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**List[ChatCompletionMessage]**](ChatCompletionMessage.md) |  | 
**model** | **str** |  | 
**stream** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.create_chat_completion import CreateChatCompletion

# TODO update the JSON string below
json = "{}"
# create an instance of CreateChatCompletion from a JSON string
create_chat_completion_instance = CreateChatCompletion.from_json(json)
# print the JSON string representation of the object
print(CreateChatCompletion.to_json())

# convert the object into a dict
create_chat_completion_dict = create_chat_completion_instance.to_dict()
# create an instance of CreateChatCompletion from a dict
create_chat_completion_from_dict = CreateChatCompletion.from_dict(create_chat_completion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


