# DlpPolicyParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dlp_policy** | [**DlpPolicy**](DlpPolicy.md) |  | [optional] 

## Example

```python
from dreamcatcher.models.dlp_policy_params import DlpPolicyParams

# TODO update the JSON string below
json = "{}"
# create an instance of DlpPolicyParams from a JSON string
dlp_policy_params_instance = DlpPolicyParams.from_json(json)
# print the JSON string representation of the object
print DlpPolicyParams.to_json()

# convert the object into a dict
dlp_policy_params_dict = dlp_policy_params_instance.to_dict()
# create an instance of DlpPolicyParams from a dict
dlp_policy_params_from_dict = DlpPolicyParams.from_dict(dlp_policy_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


