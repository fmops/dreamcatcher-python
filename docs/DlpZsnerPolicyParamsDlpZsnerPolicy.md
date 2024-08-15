# DlpZsnerPolicyParamsDlpZsnerPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**anonymizer** | [**DlpPolicyAnonymizer**](DlpPolicyAnonymizer.md) |  | [optional] 
**entities** | [**List[DlpZsnerPolicyParamsDlpZsnerPolicyEntitiesInner]**](DlpZsnerPolicyParamsDlpZsnerPolicyEntitiesInner.md) |  | [optional] 
**name** | **str** |  | [optional] 
**response** | **str** |  | [optional] 
**score_threshold** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.dlp_zsner_policy_params_dlp_zsner_policy import DlpZsnerPolicyParamsDlpZsnerPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of DlpZsnerPolicyParamsDlpZsnerPolicy from a JSON string
dlp_zsner_policy_params_dlp_zsner_policy_instance = DlpZsnerPolicyParamsDlpZsnerPolicy.from_json(json)
# print the JSON string representation of the object
print(DlpZsnerPolicyParamsDlpZsnerPolicy.to_json())

# convert the object into a dict
dlp_zsner_policy_params_dlp_zsner_policy_dict = dlp_zsner_policy_params_dlp_zsner_policy_instance.to_dict()
# create an instance of DlpZsnerPolicyParamsDlpZsnerPolicy from a dict
dlp_zsner_policy_params_dlp_zsner_policy_from_dict = DlpZsnerPolicyParamsDlpZsnerPolicy.from_dict(dlp_zsner_policy_params_dlp_zsner_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


