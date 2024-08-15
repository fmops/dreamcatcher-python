# dreamcatcher.DlpZsnerPoliciesApi

All URIs are relative to *http://localhost:4000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dreamcatcher_web_zero_shot_ner_policy_controller_create**](DlpZsnerPoliciesApi.md#dreamcatcher_web_zero_shot_ner_policy_controller_create) | **POST** /api/v1/endpoints/{endpoint_name}/policies/dlp_zsner | Create a DLP ZSNER policy
[**dreamcatcher_web_zero_shot_ner_policy_controller_delete**](DlpZsnerPoliciesApi.md#dreamcatcher_web_zero_shot_ner_policy_controller_delete) | **DELETE** /api/v1/endpoints/{endpoint_name}/policies/dlp_zsner/{id} | Delete a DLP ZSNER policy
[**dreamcatcher_web_zero_shot_ner_policy_controller_scan**](DlpZsnerPoliciesApi.md#dreamcatcher_web_zero_shot_ner_policy_controller_scan) | **POST** /api/v1/endpoints/{endpoint_name}/policies/dlp/{id}/scan | Scan content with a DLP ZSNER policy
[**dreamcatcher_web_zero_shot_ner_policy_controller_scan__2**](DlpZsnerPoliciesApi.md#dreamcatcher_web_zero_shot_ner_policy_controller_scan__2) | **POST** /api/v1/endpoints/{endpoint_name}/policies/dlp_zsner/{id}/scan | Scan content with a DLP ZSNER policy
[**dreamcatcher_web_zero_shot_ner_policy_controller_show**](DlpZsnerPoliciesApi.md#dreamcatcher_web_zero_shot_ner_policy_controller_show) | **GET** /api/v1/endpoints/{endpoint_name}/policies/dlp_zsner/{id} | Get a DLP ZSNER policy
[**dreamcatcher_web_zero_shot_ner_policy_controller_update**](DlpZsnerPoliciesApi.md#dreamcatcher_web_zero_shot_ner_policy_controller_update) | **PATCH** /api/v1/endpoints/{endpoint_name}/policies/dlp_zsner/{id} | Update a DLP ZSNER policy
[**dreamcatcher_web_zero_shot_ner_policy_controller_update__2**](DlpZsnerPoliciesApi.md#dreamcatcher_web_zero_shot_ner_policy_controller_update__2) | **PUT** /api/v1/endpoints/{endpoint_name}/policies/dlp_zsner/{id} | Update a DLP ZSNER policy


# **dreamcatcher_web_zero_shot_ner_policy_controller_create**
> DlpZsnerPolicy dreamcatcher_web_zero_shot_ner_policy_controller_create(endpoint_name, dlp_zsner_policy_params=dlp_zsner_policy_params)

Create a DLP ZSNER policy

### Example

* Bearer Authentication (authorization):

```python
import dreamcatcher
from dreamcatcher.models.dlp_zsner_policy import DlpZsnerPolicy
from dreamcatcher.models.dlp_zsner_policy_params import DlpZsnerPolicyParams
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
    api_instance = dreamcatcher.DlpZsnerPoliciesApi(api_client)
    endpoint_name = 'demo-endpoint' # str | Endpoint name
    dlp_zsner_policy_params = dreamcatcher.DlpZsnerPolicyParams() # DlpZsnerPolicyParams | DLP ZSNER policy params (optional)

    try:
        # Create a DLP ZSNER policy
        api_response = await api_instance.dreamcatcher_web_zero_shot_ner_policy_controller_create(endpoint_name, dlp_zsner_policy_params=dlp_zsner_policy_params)
        print("The response of DlpZsnerPoliciesApi->dreamcatcher_web_zero_shot_ner_policy_controller_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DlpZsnerPoliciesApi->dreamcatcher_web_zero_shot_ner_policy_controller_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_name** | **str**| Endpoint name | 
 **dlp_zsner_policy_params** | [**DlpZsnerPolicyParams**](DlpZsnerPolicyParams.md)| DLP ZSNER policy params | [optional] 

### Return type

[**DlpZsnerPolicy**](DlpZsnerPolicy.md)

### Authorization

[authorization](../README.md#authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Create DLP ZSNER policy response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dreamcatcher_web_zero_shot_ner_policy_controller_delete**
> dreamcatcher_web_zero_shot_ner_policy_controller_delete(endpoint_name, id)

Delete a DLP ZSNER policy

### Example

* Bearer Authentication (authorization):

```python
import dreamcatcher
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
    api_instance = dreamcatcher.DlpZsnerPoliciesApi(api_client)
    endpoint_name = 'demo-endpoint' # str | Endpoint name
    id = 1 # int | DLP ZSNER Policy ID

    try:
        # Delete a DLP ZSNER policy
        await api_instance.dreamcatcher_web_zero_shot_ner_policy_controller_delete(endpoint_name, id)
    except Exception as e:
        print("Exception when calling DlpZsnerPoliciesApi->dreamcatcher_web_zero_shot_ner_policy_controller_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_name** | **str**| Endpoint name | 
 **id** | **int**| DLP ZSNER Policy ID | 

### Return type

void (empty response body)

### Authorization

[authorization](../README.md#authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dreamcatcher_web_zero_shot_ner_policy_controller_scan**
> DreamcatcherWebZeroShotNERPolicyControllerScan200Response dreamcatcher_web_zero_shot_ner_policy_controller_scan(endpoint_name, id, dreamcatcher_web_zero_shot_ner_policy_controller_scan_request=dreamcatcher_web_zero_shot_ner_policy_controller_scan_request)

Scan content with a DLP ZSNER policy

### Example

* Bearer Authentication (authorization):

```python
import dreamcatcher
from dreamcatcher.models.dreamcatcher_web_zero_shot_ner_policy_controller_scan200_response import DreamcatcherWebZeroShotNERPolicyControllerScan200Response
from dreamcatcher.models.dreamcatcher_web_zero_shot_ner_policy_controller_scan_request import DreamcatcherWebZeroShotNERPolicyControllerScanRequest
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
    api_instance = dreamcatcher.DlpZsnerPoliciesApi(api_client)
    endpoint_name = 'demo-endpoint' # str | Endpoint name
    id = 1 # int | DLP ZSNER Policy ID
    dreamcatcher_web_zero_shot_ner_policy_controller_scan_request = dreamcatcher.DreamcatcherWebZeroShotNERPolicyControllerScanRequest() # DreamcatcherWebZeroShotNERPolicyControllerScanRequest | Content to scan (optional)

    try:
        # Scan content with a DLP ZSNER policy
        api_response = await api_instance.dreamcatcher_web_zero_shot_ner_policy_controller_scan(endpoint_name, id, dreamcatcher_web_zero_shot_ner_policy_controller_scan_request=dreamcatcher_web_zero_shot_ner_policy_controller_scan_request)
        print("The response of DlpZsnerPoliciesApi->dreamcatcher_web_zero_shot_ner_policy_controller_scan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DlpZsnerPoliciesApi->dreamcatcher_web_zero_shot_ner_policy_controller_scan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_name** | **str**| Endpoint name | 
 **id** | **int**| DLP ZSNER Policy ID | 
 **dreamcatcher_web_zero_shot_ner_policy_controller_scan_request** | [**DreamcatcherWebZeroShotNERPolicyControllerScanRequest**](DreamcatcherWebZeroShotNERPolicyControllerScanRequest.md)| Content to scan | [optional] 

### Return type

[**DreamcatcherWebZeroShotNERPolicyControllerScan200Response**](DreamcatcherWebZeroShotNERPolicyControllerScan200Response.md)

### Authorization

[authorization](../README.md#authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Scan DLP ZSNER policy response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dreamcatcher_web_zero_shot_ner_policy_controller_scan__2**
> DreamcatcherWebZeroShotNERPolicyControllerScan200Response dreamcatcher_web_zero_shot_ner_policy_controller_scan__2(endpoint_name, id, dreamcatcher_web_zero_shot_ner_policy_controller_scan_request=dreamcatcher_web_zero_shot_ner_policy_controller_scan_request)

Scan content with a DLP ZSNER policy

### Example

* Bearer Authentication (authorization):

```python
import dreamcatcher
from dreamcatcher.models.dreamcatcher_web_zero_shot_ner_policy_controller_scan200_response import DreamcatcherWebZeroShotNERPolicyControllerScan200Response
from dreamcatcher.models.dreamcatcher_web_zero_shot_ner_policy_controller_scan_request import DreamcatcherWebZeroShotNERPolicyControllerScanRequest
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
    api_instance = dreamcatcher.DlpZsnerPoliciesApi(api_client)
    endpoint_name = 'demo-endpoint' # str | Endpoint name
    id = 1 # int | DLP ZSNER Policy ID
    dreamcatcher_web_zero_shot_ner_policy_controller_scan_request = dreamcatcher.DreamcatcherWebZeroShotNERPolicyControllerScanRequest() # DreamcatcherWebZeroShotNERPolicyControllerScanRequest | Content to scan (optional)

    try:
        # Scan content with a DLP ZSNER policy
        api_response = await api_instance.dreamcatcher_web_zero_shot_ner_policy_controller_scan__2(endpoint_name, id, dreamcatcher_web_zero_shot_ner_policy_controller_scan_request=dreamcatcher_web_zero_shot_ner_policy_controller_scan_request)
        print("The response of DlpZsnerPoliciesApi->dreamcatcher_web_zero_shot_ner_policy_controller_scan__2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DlpZsnerPoliciesApi->dreamcatcher_web_zero_shot_ner_policy_controller_scan__2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_name** | **str**| Endpoint name | 
 **id** | **int**| DLP ZSNER Policy ID | 
 **dreamcatcher_web_zero_shot_ner_policy_controller_scan_request** | [**DreamcatcherWebZeroShotNERPolicyControllerScanRequest**](DreamcatcherWebZeroShotNERPolicyControllerScanRequest.md)| Content to scan | [optional] 

### Return type

[**DreamcatcherWebZeroShotNERPolicyControllerScan200Response**](DreamcatcherWebZeroShotNERPolicyControllerScan200Response.md)

### Authorization

[authorization](../README.md#authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Scan DLP ZSNER policy response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dreamcatcher_web_zero_shot_ner_policy_controller_show**
> DlpZsnerPolicy dreamcatcher_web_zero_shot_ner_policy_controller_show(endpoint_name, id)

Get a DLP ZSNER policy

### Example

* Bearer Authentication (authorization):

```python
import dreamcatcher
from dreamcatcher.models.dlp_zsner_policy import DlpZsnerPolicy
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
    api_instance = dreamcatcher.DlpZsnerPoliciesApi(api_client)
    endpoint_name = 'demo-endpoint' # str | Endpoint name
    id = 1 # int | DLP ZSNER Policy ID

    try:
        # Get a DLP ZSNER policy
        api_response = await api_instance.dreamcatcher_web_zero_shot_ner_policy_controller_show(endpoint_name, id)
        print("The response of DlpZsnerPoliciesApi->dreamcatcher_web_zero_shot_ner_policy_controller_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DlpZsnerPoliciesApi->dreamcatcher_web_zero_shot_ner_policy_controller_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_name** | **str**| Endpoint name | 
 **id** | **int**| DLP ZSNER Policy ID | 

### Return type

[**DlpZsnerPolicy**](DlpZsnerPolicy.md)

### Authorization

[authorization](../README.md#authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Show DLP ZSNER policy response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dreamcatcher_web_zero_shot_ner_policy_controller_update**
> DlpZsnerPolicy dreamcatcher_web_zero_shot_ner_policy_controller_update(endpoint_name, id, dlp_zsner_policy_params=dlp_zsner_policy_params)

Update a DLP ZSNER policy

### Example

* Bearer Authentication (authorization):

```python
import dreamcatcher
from dreamcatcher.models.dlp_zsner_policy import DlpZsnerPolicy
from dreamcatcher.models.dlp_zsner_policy_params import DlpZsnerPolicyParams
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
    api_instance = dreamcatcher.DlpZsnerPoliciesApi(api_client)
    endpoint_name = 'demo-endpoint' # str | Endpoint name
    id = 1 # int | DLP ZSNER Policy ID
    dlp_zsner_policy_params = dreamcatcher.DlpZsnerPolicyParams() # DlpZsnerPolicyParams | DLP ZSNER policy params (optional)

    try:
        # Update a DLP ZSNER policy
        api_response = await api_instance.dreamcatcher_web_zero_shot_ner_policy_controller_update(endpoint_name, id, dlp_zsner_policy_params=dlp_zsner_policy_params)
        print("The response of DlpZsnerPoliciesApi->dreamcatcher_web_zero_shot_ner_policy_controller_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DlpZsnerPoliciesApi->dreamcatcher_web_zero_shot_ner_policy_controller_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_name** | **str**| Endpoint name | 
 **id** | **int**| DLP ZSNER Policy ID | 
 **dlp_zsner_policy_params** | [**DlpZsnerPolicyParams**](DlpZsnerPolicyParams.md)| DLP ZSNER policy params | [optional] 

### Return type

[**DlpZsnerPolicy**](DlpZsnerPolicy.md)

### Authorization

[authorization](../README.md#authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update DLP ZSNER policy response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dreamcatcher_web_zero_shot_ner_policy_controller_update__2**
> DlpZsnerPolicy dreamcatcher_web_zero_shot_ner_policy_controller_update__2(endpoint_name, id, dlp_zsner_policy_params=dlp_zsner_policy_params)

Update a DLP ZSNER policy

### Example

* Bearer Authentication (authorization):

```python
import dreamcatcher
from dreamcatcher.models.dlp_zsner_policy import DlpZsnerPolicy
from dreamcatcher.models.dlp_zsner_policy_params import DlpZsnerPolicyParams
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
    api_instance = dreamcatcher.DlpZsnerPoliciesApi(api_client)
    endpoint_name = 'demo-endpoint' # str | Endpoint name
    id = 1 # int | DLP ZSNER Policy ID
    dlp_zsner_policy_params = dreamcatcher.DlpZsnerPolicyParams() # DlpZsnerPolicyParams | DLP ZSNER policy params (optional)

    try:
        # Update a DLP ZSNER policy
        api_response = await api_instance.dreamcatcher_web_zero_shot_ner_policy_controller_update__2(endpoint_name, id, dlp_zsner_policy_params=dlp_zsner_policy_params)
        print("The response of DlpZsnerPoliciesApi->dreamcatcher_web_zero_shot_ner_policy_controller_update__2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DlpZsnerPoliciesApi->dreamcatcher_web_zero_shot_ner_policy_controller_update__2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_name** | **str**| Endpoint name | 
 **id** | **int**| DLP ZSNER Policy ID | 
 **dlp_zsner_policy_params** | [**DlpZsnerPolicyParams**](DlpZsnerPolicyParams.md)| DLP ZSNER policy params | [optional] 

### Return type

[**DlpZsnerPolicy**](DlpZsnerPolicy.md)

### Authorization

[authorization](../README.md#authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update DLP ZSNER policy response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

