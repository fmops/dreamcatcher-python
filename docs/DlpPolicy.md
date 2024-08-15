# DlpPolicy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**anonymizer** | [**DlpPolicyAnonymizer**](DlpPolicyAnonymizer.md) |  | [optional] 
**entities** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**response** | **str** |  | [optional] 
**score_threshold** | **float** |  | [optional] 

## Example

```python
from dreamcatcher.models.dlp_policy import DlpPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of DlpPolicy from a JSON string
dlp_policy_instance = DlpPolicy.from_json(json)
# print the JSON string representation of the object
print DlpPolicy.to_json()

# convert the object into a dict
dlp_policy_dict = dlp_policy_instance.to_dict()
# create an instance of DlpPolicy from a dict
dlp_policy_from_dict = DlpPolicy.from_dict(dlp_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


