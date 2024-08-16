# DlpZsnerPolicy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**anonymizer** | [**DlpPolicyAnonymizer**](DlpPolicyAnonymizer.md) |  | [optional] 
**entities** | [**List[DlpZsnerPolicyEntitiesInner]**](DlpZsnerPolicyEntitiesInner.md) |  | [optional] 
**id** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**response** | **str** |  | [optional] 
**score_threshold** | **float** |  | [optional] 

## Example

```python
from dreamcatcher.models.dlp_zsner_policy import DlpZsnerPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of DlpZsnerPolicy from a JSON string
dlp_zsner_policy_instance = DlpZsnerPolicy.from_json(json)
# print the JSON string representation of the object
print DlpZsnerPolicy.to_json()

# convert the object into a dict
dlp_zsner_policy_dict = dlp_zsner_policy_instance.to_dict()
# create an instance of DlpZsnerPolicy from a dict
dlp_zsner_policy_from_dict = DlpZsnerPolicy.from_dict(dlp_zsner_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


