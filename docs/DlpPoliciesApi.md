# openapi_client.DlpPoliciesApi

All URIs are relative to *http://localhost:4000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dreamcatcher_web_presidio_policy_controller_show**](DlpPoliciesApi.md#dreamcatcher_web_presidio_policy_controller_show) | **GET** /api/v1/endpoints/{endpoint_name}/policies/dlp/{id} | Get a DLP policy


# **dreamcatcher_web_presidio_policy_controller_show**
> DlpPolicy dreamcatcher_web_presidio_policy_controller_show(endpoint_name, id)

Get a DLP policy

### Example

* Bearer Authentication (authorization):

```python
import openapi_client
from openapi_client.models.dlp_policy import DlpPolicy
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:4000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authorization
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DlpPoliciesApi(api_client)
    endpoint_name = 'demo-endpoint' # str | Endpoint name
    id = 1 # int | DLP Policy ID

    try:
        # Get a DLP policy
        api_response = api_instance.dreamcatcher_web_presidio_policy_controller_show(endpoint_name, id)
        print("The response of DlpPoliciesApi->dreamcatcher_web_presidio_policy_controller_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DlpPoliciesApi->dreamcatcher_web_presidio_policy_controller_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_name** | **str**| Endpoint name | 
 **id** | **int**| DLP Policy ID | 

### Return type

[**DlpPolicy**](DlpPolicy.md)

### Authorization

[authorization](../README.md#authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Show DLP policy response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

