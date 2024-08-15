# dreamcatcher.OpenaiApi

All URIs are relative to *http://localhost:4000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stubidity_open_ai_chat_completion_call**](OpenaiApi.md#stubidity_open_ai_chat_completion_call) | **POST** /api/v1/stub/openai/v1/chat/completions | Chat completion
[**stubidity_open_ai_completion_call**](OpenaiApi.md#stubidity_open_ai_completion_call) | **POST** /api/v1/stub/openai/v1/completions | Completion
[**stubidity_open_ai_embedding_call**](OpenaiApi.md#stubidity_open_ai_embedding_call) | **POST** /api/v1/stub/openai/v1/embeddings | Embedding
[**stubidity_open_ai_embedding_call__2**](OpenaiApi.md#stubidity_open_ai_embedding_call__2) | **POST** /api/v1/stub/openai/v1/engines/{model} | Embedding


# **stubidity_open_ai_chat_completion_call**
> ChatCompletionResponse stubidity_open_ai_chat_completion_call(create_chat_completion=create_chat_completion)

Chat completion

### Example

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


# Enter a context with an instance of the API client
async with dreamcatcher.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dreamcatcher.OpenaiApi(api_client)
    create_chat_completion = dreamcatcher.CreateChatCompletion() # CreateChatCompletion | Chat completion params (optional)

    try:
        # Chat completion
        api_response = await api_instance.stubidity_open_ai_chat_completion_call(create_chat_completion=create_chat_completion)
        print("The response of OpenaiApi->stubidity_open_ai_chat_completion_call:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenaiApi->stubidity_open_ai_chat_completion_call: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_chat_completion** | [**CreateChatCompletion**](CreateChatCompletion.md)| Chat completion params | [optional] 

### Return type

[**ChatCompletionResponse**](ChatCompletionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Chat completion response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stubidity_open_ai_completion_call**
> CompletionResponse stubidity_open_ai_completion_call(completion=completion)

Completion

### Example

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


# Enter a context with an instance of the API client
async with dreamcatcher.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dreamcatcher.OpenaiApi(api_client)
    completion = dreamcatcher.Completion() # Completion | Completion params (optional)

    try:
        # Completion
        api_response = await api_instance.stubidity_open_ai_completion_call(completion=completion)
        print("The response of OpenaiApi->stubidity_open_ai_completion_call:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenaiApi->stubidity_open_ai_completion_call: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **completion** | [**Completion**](Completion.md)| Completion params | [optional] 

### Return type

[**CompletionResponse**](CompletionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Completion response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stubidity_open_ai_embedding_call**
> List[EmbeddingResponseInner] stubidity_open_ai_embedding_call(embedding=embedding)

Embedding

### Example

```python
import time
import os
import dreamcatcher
from dreamcatcher.models.embedding import Embedding
from dreamcatcher.models.embedding_response_inner import EmbeddingResponseInner
from dreamcatcher.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4000
# See configuration.py for a list of all supported configuration parameters.
configuration = dreamcatcher.Configuration(
    host = "http://localhost:4000"
)


# Enter a context with an instance of the API client
async with dreamcatcher.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dreamcatcher.OpenaiApi(api_client)
    embedding = dreamcatcher.Embedding() # Embedding | Embedding params (optional)

    try:
        # Embedding
        api_response = await api_instance.stubidity_open_ai_embedding_call(embedding=embedding)
        print("The response of OpenaiApi->stubidity_open_ai_embedding_call:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenaiApi->stubidity_open_ai_embedding_call: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **embedding** | [**Embedding**](Embedding.md)| Embedding params | [optional] 

### Return type

[**List[EmbeddingResponseInner]**](EmbeddingResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Embedding response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stubidity_open_ai_embedding_call__2**
> List[EmbeddingResponseInner] stubidity_open_ai_embedding_call__2(embedding=embedding)

Embedding

### Example

```python
import time
import os
import dreamcatcher
from dreamcatcher.models.embedding import Embedding
from dreamcatcher.models.embedding_response_inner import EmbeddingResponseInner
from dreamcatcher.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4000
# See configuration.py for a list of all supported configuration parameters.
configuration = dreamcatcher.Configuration(
    host = "http://localhost:4000"
)


# Enter a context with an instance of the API client
async with dreamcatcher.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dreamcatcher.OpenaiApi(api_client)
    embedding = dreamcatcher.Embedding() # Embedding | Embedding params (optional)

    try:
        # Embedding
        api_response = await api_instance.stubidity_open_ai_embedding_call__2(embedding=embedding)
        print("The response of OpenaiApi->stubidity_open_ai_embedding_call__2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenaiApi->stubidity_open_ai_embedding_call__2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **embedding** | [**Embedding**](Embedding.md)| Embedding params | [optional] 

### Return type

[**List[EmbeddingResponseInner]**](EmbeddingResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Embedding response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

