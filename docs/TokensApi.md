# swagger_client.TokensApi

All URIs are relative to *http://127.0.0.1:7000/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tokens_create_post**](TokensApi.md#tokens_create_post) | **POST** /tokens/create | Generate tokens for an user
[**tokens_refresh_post**](TokensApi.md#tokens_refresh_post) | **POST** /tokens/refresh | Refresh tokens for an user
[**tokens_revoke_post**](TokensApi.md#tokens_revoke_post) | **POST** /tokens/revoke | Revoke a refresh token for an user

# **tokens_create_post**
> Success tokens_create_post(project_name=project_name, scope=scope)

Generate tokens for an user

Request to generate tokens for an user 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from fabric.credmgr.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TokensApi()
project_name = 'all' # str | Project Name (optional) (default to all)
scope = 'all' # str | Scope for which token is requested (optional) (default to all)

try:
    # Generate tokens for an user
    api_response = api_instance.tokens_create_post(project_name=project_name, scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokensApi->tokens_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| Project Name | [optional] [default to all]
 **scope** | **str**| Scope for which token is requested | [optional] [default to all]

### Return type

[**Success**](Success.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tokens_refresh_post**
> Success tokens_refresh_post(body=body, project_name=project_name, scope=scope)

Refresh tokens for an user

Request to refresh OAuth tokens for an user 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from fabric.credmgr.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TokensApi()
body = swagger_client.Request() # Request |  (optional)
project_name = 'all' # str | Project Name (optional) (default to all)
scope = 'all' # str | Scope for which token is requested (optional) (default to all)

try:
    # Refresh tokens for an user
    api_response = api_instance.tokens_refresh_post(body=body, project_name=project_name, scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokensApi->tokens_refresh_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Request**](Request.md)|  | [optional] 
 **project_name** | **str**| Project Name | [optional] [default to all]
 **scope** | **str**| Scope for which token is requested | [optional] [default to all]

### Return type

[**Success**](Success.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tokens_revoke_post**
> tokens_revoke_post(body=body)

Revoke a refresh token for an user

Request to revoke a refresh token for an user 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from fabric.credmgr.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TokensApi()
body = swagger_client.Request() # Request |  (optional)

try:
    # Revoke a refresh token for an user
    api_instance.tokens_revoke_post(body=body)
except ApiException as e:
    print("Exception when calling TokensApi->tokens_revoke_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Request**](Request.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

