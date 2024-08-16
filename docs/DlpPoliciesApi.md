# dreamcatcher.DlpPoliciesApi

All URIs are relative to *http://localhost:4000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dreamcatcher_web_presidio_policy_controller_create**](DlpPoliciesApi.md#dreamcatcher_web_presidio_policy_controller_create) | **POST** /api/v1/endpoints/{endpoint_name}/policies/dlp | Create a DLP policy
[**dreamcatcher_web_presidio_policy_controller_delete**](DlpPoliciesApi.md#dreamcatcher_web_presidio_policy_controller_delete) | **DELETE** /api/v1/endpoints/{endpoint_name}/policies/dlp/{id} | Delete a DLP policy
[**dreamcatcher_web_presidio_policy_controller_scan**](DlpPoliciesApi.md#dreamcatcher_web_presidio_policy_controller_scan) | **POST** /api/v1/endpoints/{endpoint_name}/policies/dlp/{id}/scan | Scan content with a DLP policy
[**dreamcatcher_web_presidio_policy_controller_show**](DlpPoliciesApi.md#dreamcatcher_web_presidio_policy_controller_show) | **GET** /api/v1/endpoints/{endpoint_name}/policies/dlp/{id} | Get a DLP policy
[**dreamcatcher_web_presidio_policy_controller_update**](DlpPoliciesApi.md#dreamcatcher_web_presidio_policy_controller_update) | **PATCH** /api/v1/endpoints/{endpoint_name}/policies/dlp/{id} | Update a DLP policy
[**dreamcatcher_web_presidio_policy_controller_update__2**](DlpPoliciesApi.md#dreamcatcher_web_presidio_policy_controller_update__2) | **PUT** /api/v1/endpoints/{endpoint_name}/policies/dlp/{id} | Update a DLP policy


# **dreamcatcher_web_presidio_policy_controller_create**
> DlpPolicy dreamcatcher_web_presidio_policy_controller_create(endpoint_name, dlp_policy_params=dlp_policy_params)

Create a DLP policy

### Example

* Bearer Authentication (authorization):
```python
import time
import os
import dreamcatcher
from dreamcatcher.models.dlp_policy import DlpPolicy
from dreamcatcher.models.dlp_policy_params import DlpPolicyParams
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
with dreamcatcher.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dreamcatcher.DlpPoliciesApi(api_client)
    endpoint_name = 'demo-endpoint' # str | Endpoint name
    dlp_policy_params = dreamcatcher.DlpPolicyParams() # DlpPolicyParams | DLP policy params (optional)

    try:
        # Create a DLP policy
        api_response = api_instance.dreamcatcher_web_presidio_policy_controller_create(endpoint_name, dlp_policy_params=dlp_policy_params)
        print("The response of DlpPoliciesApi->dreamcatcher_web_presidio_policy_controller_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DlpPoliciesApi->dreamcatcher_web_presidio_policy_controller_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_name** | **str**| Endpoint name | 
 **dlp_policy_params** | [**DlpPolicyParams**](DlpPolicyParams.md)| DLP policy params | [optional] 

### Return type

[**DlpPolicy**](DlpPolicy.md)

### Authorization

[authorization](../README.md#authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Create DLP policy response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dreamcatcher_web_presidio_policy_controller_delete**
> dreamcatcher_web_presidio_policy_controller_delete(endpoint_name, id)

Delete a DLP policy

### Example

* Bearer Authentication (authorization):
```python
import time
import os
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
with dreamcatcher.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dreamcatcher.DlpPoliciesApi(api_client)
    endpoint_name = 'demo-endpoint' # str | Endpoint name
    id = 1 # int | DLP Policy ID

    try:
        # Delete a DLP policy
        api_instance.dreamcatcher_web_presidio_policy_controller_delete(endpoint_name, id)
    except Exception as e:
        print("Exception when calling DlpPoliciesApi->dreamcatcher_web_presidio_policy_controller_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_name** | **str**| Endpoint name | 
 **id** | **int**| DLP Policy ID | 

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

# **dreamcatcher_web_presidio_policy_controller_scan**
> DreamcatcherWebPresidioPolicyControllerScan200Response dreamcatcher_web_presidio_policy_controller_scan(endpoint_name, id, dreamcatcher_web_presidio_policy_controller_scan_request=dreamcatcher_web_presidio_policy_controller_scan_request)

Scan content with a DLP policy

### Example

* Bearer Authentication (authorization):
```python
import time
import os
import dreamcatcher
from dreamcatcher.models.dreamcatcher_web_presidio_policy_controller_scan200_response import DreamcatcherWebPresidioPolicyControllerScan200Response
from dreamcatcher.models.dreamcatcher_web_presidio_policy_controller_scan_request import DreamcatcherWebPresidioPolicyControllerScanRequest
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
with dreamcatcher.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dreamcatcher.DlpPoliciesApi(api_client)
    endpoint_name = 'demo-endpoint' # str | Endpoint name
    id = 1 # int | DLP Policy ID
    dreamcatcher_web_presidio_policy_controller_scan_request = dreamcatcher.DreamcatcherWebPresidioPolicyControllerScanRequest() # DreamcatcherWebPresidioPolicyControllerScanRequest | Content to scan (optional)

    try:
        # Scan content with a DLP policy
        api_response = api_instance.dreamcatcher_web_presidio_policy_controller_scan(endpoint_name, id, dreamcatcher_web_presidio_policy_controller_scan_request=dreamcatcher_web_presidio_policy_controller_scan_request)
        print("The response of DlpPoliciesApi->dreamcatcher_web_presidio_policy_controller_scan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DlpPoliciesApi->dreamcatcher_web_presidio_policy_controller_scan: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_name** | **str**| Endpoint name | 
 **id** | **int**| DLP Policy ID | 
 **dreamcatcher_web_presidio_policy_controller_scan_request** | [**DreamcatcherWebPresidioPolicyControllerScanRequest**](DreamcatcherWebPresidioPolicyControllerScanRequest.md)| Content to scan | [optional] 

### Return type

[**DreamcatcherWebPresidioPolicyControllerScan200Response**](DreamcatcherWebPresidioPolicyControllerScan200Response.md)

### Authorization

[authorization](../README.md#authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Scan DLP policy response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dreamcatcher_web_presidio_policy_controller_show**
> DlpPolicy dreamcatcher_web_presidio_policy_controller_show(endpoint_name, id)

Get a DLP policy

### Example

* Bearer Authentication (authorization):
```python
import time
import os
import dreamcatcher
from dreamcatcher.models.dlp_policy import DlpPolicy
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
with dreamcatcher.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dreamcatcher.DlpPoliciesApi(api_client)
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

# **dreamcatcher_web_presidio_policy_controller_update**
> DlpPolicy dreamcatcher_web_presidio_policy_controller_update(endpoint_name, id, dlp_policy_params=dlp_policy_params)

Update a DLP policy

### Example

* Bearer Authentication (authorization):
```python
import time
import os
import dreamcatcher
from dreamcatcher.models.dlp_policy import DlpPolicy
from dreamcatcher.models.dlp_policy_params import DlpPolicyParams
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
with dreamcatcher.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dreamcatcher.DlpPoliciesApi(api_client)
    endpoint_name = 'demo-endpoint' # str | Endpoint name
    id = 1 # int | DLP Policy ID
    dlp_policy_params = dreamcatcher.DlpPolicyParams() # DlpPolicyParams | DLP policy params (optional)

    try:
        # Update a DLP policy
        api_response = api_instance.dreamcatcher_web_presidio_policy_controller_update(endpoint_name, id, dlp_policy_params=dlp_policy_params)
        print("The response of DlpPoliciesApi->dreamcatcher_web_presidio_policy_controller_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DlpPoliciesApi->dreamcatcher_web_presidio_policy_controller_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_name** | **str**| Endpoint name | 
 **id** | **int**| DLP Policy ID | 
 **dlp_policy_params** | [**DlpPolicyParams**](DlpPolicyParams.md)| DLP policy params | [optional] 

### Return type

[**DlpPolicy**](DlpPolicy.md)

### Authorization

[authorization](../README.md#authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update DLP policy response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dreamcatcher_web_presidio_policy_controller_update__2**
> DlpPolicy dreamcatcher_web_presidio_policy_controller_update__2(endpoint_name, id, dlp_policy_params=dlp_policy_params)

Update a DLP policy

### Example

* Bearer Authentication (authorization):
```python
import time
import os
import dreamcatcher
from dreamcatcher.models.dlp_policy import DlpPolicy
from dreamcatcher.models.dlp_policy_params import DlpPolicyParams
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
with dreamcatcher.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dreamcatcher.DlpPoliciesApi(api_client)
    endpoint_name = 'demo-endpoint' # str | Endpoint name
    id = 1 # int | DLP Policy ID
    dlp_policy_params = dreamcatcher.DlpPolicyParams() # DlpPolicyParams | DLP policy params (optional)

    try:
        # Update a DLP policy
        api_response = api_instance.dreamcatcher_web_presidio_policy_controller_update__2(endpoint_name, id, dlp_policy_params=dlp_policy_params)
        print("The response of DlpPoliciesApi->dreamcatcher_web_presidio_policy_controller_update__2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DlpPoliciesApi->dreamcatcher_web_presidio_policy_controller_update__2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_name** | **str**| Endpoint name | 
 **id** | **int**| DLP Policy ID | 
 **dlp_policy_params** | [**DlpPolicyParams**](DlpPolicyParams.md)| DLP policy params | [optional] 

### Return type

[**DlpPolicy**](DlpPolicy.md)

### Authorization

[authorization](../README.md#authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update DLP policy response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

