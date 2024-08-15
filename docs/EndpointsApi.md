# dreamcatcher.EndpointsApi

All URIs are relative to *http://localhost:4000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dreamcatcher_web_endpoint_controller_index**](EndpointsApi.md#dreamcatcher_web_endpoint_controller_index) | **GET** /api/v1/endpoints | List endpoints
[**dreamcatcher_web_endpoint_controller_show**](EndpointsApi.md#dreamcatcher_web_endpoint_controller_show) | **GET** /api/v1/endpoints/{id} | Get an endpoint


# **dreamcatcher_web_endpoint_controller_index**
> List[ListEndpointResponseInner] dreamcatcher_web_endpoint_controller_index()

List endpoints

### Example

* Bearer Authentication (authorization):
```python
import time
import os
import dreamcatcher
from dreamcatcher.models.list_endpoint_response_inner import ListEndpointResponseInner
from dreamcatcher.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4000
# See configuration.py for a list of all supported configuration parameters.
configuration = dreamcatcher.Configuration(
    host = "http://localhost:4000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authorization
configuration = dreamcatcher.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dreamcatcher.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dreamcatcher.EndpointsApi(api_client)

    try:
        # List endpoints
        api_response = await api_instance.dreamcatcher_web_endpoint_controller_index()
        print("The response of EndpointsApi->dreamcatcher_web_endpoint_controller_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->dreamcatcher_web_endpoint_controller_index: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[ListEndpointResponseInner]**](ListEndpointResponseInner.md)

### Authorization

[authorization](../README.md#authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List endpoints response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dreamcatcher_web_endpoint_controller_show**
> ShowEndpointResponse dreamcatcher_web_endpoint_controller_show(id)

Get an endpoint

### Example

* Bearer Authentication (authorization):
```python
import time
import os
import dreamcatcher
from dreamcatcher.models.show_endpoint_response import ShowEndpointResponse
from dreamcatcher.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4000
# See configuration.py for a list of all supported configuration parameters.
configuration = dreamcatcher.Configuration(
    host = "http://localhost:4000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authorization
configuration = dreamcatcher.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with dreamcatcher.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dreamcatcher.EndpointsApi(api_client)
    id = 'demo-endpoint' # str | Endpoint name

    try:
        # Get an endpoint
        api_response = await api_instance.dreamcatcher_web_endpoint_controller_show(id)
        print("The response of EndpointsApi->dreamcatcher_web_endpoint_controller_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->dreamcatcher_web_endpoint_controller_show: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Endpoint name | 

### Return type

[**ShowEndpointResponse**](ShowEndpointResponse.md)

### Authorization

[authorization](../README.md#authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Show endpoint response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

