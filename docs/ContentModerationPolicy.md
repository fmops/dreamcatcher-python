# ContentModerationPolicy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**blocked_content_types** | **List[str]** |  | [optional] 
**id** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**score_threshold** | **float** |  | [optional] 

## Example

```python
from dreamcatcher.models.content_moderation_policy import ContentModerationPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ContentModerationPolicy from a JSON string
content_moderation_policy_instance = ContentModerationPolicy.from_json(json)
# print the JSON string representation of the object
print ContentModerationPolicy.to_json()

# convert the object into a dict
content_moderation_policy_dict = content_moderation_policy_instance.to_dict()
# create an instance of ContentModerationPolicy from a dict
content_moderation_policy_from_dict = ContentModerationPolicy.from_dict(content_moderation_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


