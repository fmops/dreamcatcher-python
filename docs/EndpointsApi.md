# dreamcatcher.EndpointsApi

All URIs are relative to *http://localhost:4000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dreamcatcher_web_endpoint_controller_index**](EndpointsApi.md#dreamcatcher_web_endpoint_controller_index) | **GET** /api/v1/endpoints | List endpoints
[**dreamcatcher_web_endpoint_controller_invoke_chat_completions**](EndpointsApi.md#dreamcatcher_web_endpoint_controller_invoke_chat_completions) | **POST** /api/v1/endpoints/{endpoint_name}/openai/v1/chat/completions | Invoke a chat completion
[**dreamcatcher_web_endpoint_controller_invoke_completions**](EndpointsApi.md#dreamcatcher_web_endpoint_controller_invoke_completions) | **POST** /api/v1/endpoints/{endpoint_name}/openai/v1/completions | Invoke a completion
[**dreamcatcher_web_endpoint_controller_models**](EndpointsApi.md#dreamcatcher_web_endpoint_controller_models) | **GET** /api/v1/endpoints/{endpoint_name}/openai/v1/models | Lists upstreams (ie models) for an endpoint
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

# **dreamcatcher_web_endpoint_controller_invoke_chat_completions**
> ChatCompletionResponse dreamcatcher_web_endpoint_controller_invoke_chat_completions(endpoint_name, create_chat_completion=create_chat_completion)

Invoke a chat completion

### Example

* Bearer Authentication (authorization):
```python
import time
import os
import dreamcatcher
from dreamcatcher.models.chat_completion_response import ChatCompletionResponse
from dreamcatcher.models.create_chat_completion import CreateChatCompletion
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
    endpoint_name = 'demo-endpoint' # str | Endpoint name
    create_chat_completion = dreamcatcher.CreateChatCompletion() # CreateChatCompletion | Chat completion params (optional)

    try:
        # Invoke a chat completion
        api_response = await api_instance.dreamcatcher_web_endpoint_controller_invoke_chat_completions(endpoint_name, create_chat_completion=create_chat_completion)
        print("The response of EndpointsApi->dreamcatcher_web_endpoint_controller_invoke_chat_completions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->dreamcatcher_web_endpoint_controller_invoke_chat_completions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_name** | **str**| Endpoint name | 
 **create_chat_completion** | [**CreateChatCompletion**](CreateChatCompletion.md)| Chat completion params | [optional] 

### Return type

[**ChatCompletionResponse**](ChatCompletionResponse.md)

### Authorization

[authorization](../README.md#authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Chat completion response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dreamcatcher_web_endpoint_controller_invoke_completions**
> CompletionResponse dreamcatcher_web_endpoint_controller_invoke_completions(endpoint_name, completion=completion)

Invoke a completion

### Example

* Bearer Authentication (authorization):
```python
import time
import os
import dreamcatcher
from dreamcatcher.models.completion import Completion
from dreamcatcher.models.completion_response import CompletionResponse
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
    endpoint_name = 'demo-endpoint' # str | Endpoint name
    completion = dreamcatcher.Completion() # Completion | Completion params (optional)

    try:
        # Invoke a completion
        api_response = await api_instance.dreamcatcher_web_endpoint_controller_invoke_completions(endpoint_name, completion=completion)
        print("The response of EndpointsApi->dreamcatcher_web_endpoint_controller_invoke_completions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->dreamcatcher_web_endpoint_controller_invoke_completions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_name** | **str**| Endpoint name | 
 **completion** | [**Completion**](Completion.md)| Completion params | [optional] 

### Return type

[**CompletionResponse**](CompletionResponse.md)

### Authorization

[authorization](../README.md#authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Completion response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dreamcatcher_web_endpoint_controller_models**
> ListModelsResponse dreamcatcher_web_endpoint_controller_models(endpoint_name)

Lists upstreams (ie models) for an endpoint

### Example

* Bearer Authentication (authorization):
```python
import time
import os
import dreamcatcher
from dreamcatcher.models.list_models_response import ListModelsResponse
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
    endpoint_name = 'demo-endpoint' # str | Endpoint name

    try:
        # Lists upstreams (ie models) for an endpoint
        api_response = await api_instance.dreamcatcher_web_endpoint_controller_models(endpoint_name)
        print("The response of EndpointsApi->dreamcatcher_web_endpoint_controller_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->dreamcatcher_web_endpoint_controller_models: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_name** | **str**| Endpoint name | 

### Return type

[**ListModelsResponse**](ListModelsResponse.md)

### Authorization

[authorization](../README.md#authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List models response |  -  |

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

