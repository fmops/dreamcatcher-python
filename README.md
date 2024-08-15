# openapi-client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 
- Package version: 1.0.0
- Generator version: 7.7.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import openapi_client
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
    except ApiException as e:
        print("Exception when calling DlpPoliciesApi->dreamcatcher_web_presidio_policy_controller_show: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:4000*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DlpPoliciesApi* | [**dreamcatcher_web_presidio_policy_controller_show**](docs/DlpPoliciesApi.md#dreamcatcher_web_presidio_policy_controller_show) | **GET** /api/v1/endpoints/{endpoint_name}/policies/dlp/{id} | Get a DLP policy
*DlpZsnerPoliciesApi* | [**dreamcatcher_web_zero_shot_ner_policy_controller_create**](docs/DlpZsnerPoliciesApi.md#dreamcatcher_web_zero_shot_ner_policy_controller_create) | **POST** /api/v1/endpoints/{endpoint_name}/policies/dlp_zsner | Create a DLP ZSNER policy
*DlpZsnerPoliciesApi* | [**dreamcatcher_web_zero_shot_ner_policy_controller_delete**](docs/DlpZsnerPoliciesApi.md#dreamcatcher_web_zero_shot_ner_policy_controller_delete) | **DELETE** /api/v1/endpoints/{endpoint_name}/policies/dlp_zsner/{id} | Delete a DLP ZSNER policy
*DlpZsnerPoliciesApi* | [**dreamcatcher_web_zero_shot_ner_policy_controller_scan**](docs/DlpZsnerPoliciesApi.md#dreamcatcher_web_zero_shot_ner_policy_controller_scan) | **POST** /api/v1/endpoints/{endpoint_name}/policies/dlp_zsner/{id}/scan | Scan content with a DLP ZSNER policy
*DlpZsnerPoliciesApi* | [**dreamcatcher_web_zero_shot_ner_policy_controller_show**](docs/DlpZsnerPoliciesApi.md#dreamcatcher_web_zero_shot_ner_policy_controller_show) | **GET** /api/v1/endpoints/{endpoint_name}/policies/dlp_zsner/{id} | Get a DLP ZSNER policy
*DlpZsnerPoliciesApi* | [**dreamcatcher_web_zero_shot_ner_policy_controller_update**](docs/DlpZsnerPoliciesApi.md#dreamcatcher_web_zero_shot_ner_policy_controller_update) | **PATCH** /api/v1/endpoints/{endpoint_name}/policies/dlp_zsner/{id} | Update a DLP ZSNER policy
*DlpZsnerPoliciesApi* | [**dreamcatcher_web_zero_shot_ner_policy_controller_update__2**](docs/DlpZsnerPoliciesApi.md#dreamcatcher_web_zero_shot_ner_policy_controller_update__2) | **PUT** /api/v1/endpoints/{endpoint_name}/policies/dlp_zsner/{id} | Update a DLP ZSNER policy
*EndpointsApi* | [**dreamcatcher_web_endpoint_controller_index**](docs/EndpointsApi.md#dreamcatcher_web_endpoint_controller_index) | **GET** /api/v1/endpoints | List endpoints
*EndpointsApi* | [**dreamcatcher_web_endpoint_controller_show**](docs/EndpointsApi.md#dreamcatcher_web_endpoint_controller_show) | **GET** /api/v1/endpoints/{id} | Get an endpoint
*OpenaiApi* | [**stubidity_open_ai_chat_completion_call**](docs/OpenaiApi.md#stubidity_open_ai_chat_completion_call) | **POST** /api/v1/stub/openai/v1/chat/completions | Chat completion
*OpenaiApi* | [**stubidity_open_ai_completion_call**](docs/OpenaiApi.md#stubidity_open_ai_completion_call) | **POST** /api/v1/stub/openai/v1/completions | Completion
*OpenaiApi* | [**stubidity_open_ai_embedding_call**](docs/OpenaiApi.md#stubidity_open_ai_embedding_call) | **POST** /api/v1/stub/openai/v1/embeddings | Embedding
*OpenaiApi* | [**stubidity_open_ai_embedding_call__2**](docs/OpenaiApi.md#stubidity_open_ai_embedding_call__2) | **POST** /api/v1/stub/openai/v1/engines/{model} | Embedding


## Documentation For Models

 - [ChatCompletionMessage](docs/ChatCompletionMessage.md)
 - [ChatCompletionResponse](docs/ChatCompletionResponse.md)
 - [ChatCompletionResponseChoicesInner](docs/ChatCompletionResponseChoicesInner.md)
 - [Completion](docs/Completion.md)
 - [CompletionResponse](docs/CompletionResponse.md)
 - [CompletionResponseChoicesInner](docs/CompletionResponseChoicesInner.md)
 - [ContentModerationPolicy](docs/ContentModerationPolicy.md)
 - [CreateChatCompletion](docs/CreateChatCompletion.md)
 - [DlpPolicy](docs/DlpPolicy.md)
 - [DlpPolicyAnonymizer](docs/DlpPolicyAnonymizer.md)
 - [DlpZsnerPolicy](docs/DlpZsnerPolicy.md)
 - [DlpZsnerPolicyAnonymizer](docs/DlpZsnerPolicyAnonymizer.md)
 - [DlpZsnerPolicyParams](docs/DlpZsnerPolicyParams.md)
 - [DlpZsnerPolicyParamsDlpZsnerPolicy](docs/DlpZsnerPolicyParamsDlpZsnerPolicy.md)
 - [DlpZsnerPolicyParamsDlpZsnerPolicyEntitiesInner](docs/DlpZsnerPolicyParamsDlpZsnerPolicyEntitiesInner.md)
 - [DreamcatcherWebZeroShotNERPolicyControllerScan200Response](docs/DreamcatcherWebZeroShotNERPolicyControllerScan200Response.md)
 - [DreamcatcherWebZeroShotNERPolicyControllerScanRequest](docs/DreamcatcherWebZeroShotNERPolicyControllerScanRequest.md)
 - [Embedding](docs/Embedding.md)
 - [EmbeddingResponseInner](docs/EmbeddingResponseInner.md)
 - [ListEndpointResponseInner](docs/ListEndpointResponseInner.md)
 - [ShowEndpointResponse](docs/ShowEndpointResponse.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="authorization"></a>
### authorization

- **Type**: Bearer authentication


## Author




