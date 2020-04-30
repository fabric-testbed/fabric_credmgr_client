# fabric_credmgr.DefaultApi

All URIs are relative to *https://virtserver.swaggerhub.com/kthare10/credmgr/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_post**](DefaultApi.md#create_post) | **POST** /create | Generate OAuth tokens for an user
[**create_with_id_token_post**](DefaultApi.md#create_with_id_token_post) | **POST** /createWithIdToken | Generate OAuth tokens for an user provided CILogon ID Token
[**get_get**](DefaultApi.md#get_get) | **GET** /get | get tokens for an user
[**refresh_post**](DefaultApi.md#refresh_post) | **POST** /refresh | Refresh OAuth tokens for an user
[**revoke_post**](DefaultApi.md#revoke_post) | **POST** /revoke | Revoke a refresh token for an user


# **create_post**
> CredMgrResponse create_post(project_name=project_name, scope=scope)

Generate OAuth tokens for an user

Request to generate OAuth tokens for an user 

### Example
```python
from __future__ import print_function
import time
import fabric_credmgr
from fabric_credmgr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fabric_credmgr.DefaultApi()
project_name = 'all' # str |  (optional) (default to all)
scope = 'all' # str |  (optional) (default to all)

try:
    # Generate OAuth tokens for an user
    api_response = api_instance.create_post(project_name=project_name, scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | [optional] [default to all]
 **scope** | **str**|  | [optional] [default to all]

### Return type

[**CredMgrResponse**](CredMgrResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_with_id_token_post**
> CredMgrResponse create_with_id_token_post(string, project_name=project_name, scope=scope)

Generate OAuth tokens for an user provided CILogon ID Token

Request to generate OAuth tokens for an user provided CILogon ID Token 

### Example
```python
from __future__ import print_function
import time
import fabric_credmgr
from fabric_credmgr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fabric_credmgr.DefaultApi()
string = fabric_credmgr.CreateRequest() # CreateRequest | 
project_name = 'all' # str |  (optional) (default to all)
scope = 'all' # str |  (optional) (default to all)

try:
    # Generate OAuth tokens for an user provided CILogon ID Token
    api_response = api_instance.create_with_id_token_post(string, project_name=project_name, scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_with_id_token_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **string** | [**CreateRequest**](CreateRequest.md)|  | 
 **project_name** | **str**|  | [optional] [default to all]
 **scope** | **str**|  | [optional] [default to all]

### Return type

[**CredMgrResponse**](CredMgrResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_get**
> CredMgrResponse get_get(user_id)

get tokens for an user

Request to get tokens for an user 

### Example
```python
from __future__ import print_function
import time
import fabric_credmgr
from fabric_credmgr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fabric_credmgr.DefaultApi()
user_id = 'user_id_example' # str | 

try:
    # get tokens for an user
    api_response = api_instance.get_get(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**CredMgrResponse**](CredMgrResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_post**
> CredMgrResponse refresh_post(string, project_name=project_name, scope=scope)

Refresh OAuth tokens for an user

Request to refresh OAuth tokens for an user 

### Example
```python
from __future__ import print_function
import time
import fabric_credmgr
from fabric_credmgr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fabric_credmgr.DefaultApi()
string = fabric_credmgr.RefreshRevokeRequest() # RefreshRevokeRequest | 
project_name = 'all' # str |  (optional) (default to all)
scope = 'all' # str |  (optional) (default to all)

try:
    # Refresh OAuth tokens for an user
    api_response = api_instance.refresh_post(string, project_name=project_name, scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->refresh_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **string** | [**RefreshRevokeRequest**](RefreshRevokeRequest.md)|  | 
 **project_name** | **str**|  | [optional] [default to all]
 **scope** | **str**|  | [optional] [default to all]

### Return type

[**CredMgrResponse**](CredMgrResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_post**
> CredMgrResponse revoke_post(string)

Revoke a refresh token for an user

Request to revoke a refresh token for an user 

### Example
```python
from __future__ import print_function
import time
import fabric_credmgr
from fabric_credmgr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = fabric_credmgr.DefaultApi()
string = fabric_credmgr.RefreshRevokeRequest() # RefreshRevokeRequest | 

try:
    # Revoke a refresh token for an user
    api_response = api_instance.revoke_post(string)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->revoke_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **string** | [**RefreshRevokeRequest**](RefreshRevokeRequest.md)|  | 

### Return type

[**CredMgrResponse**](CredMgrResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

