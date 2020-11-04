# swagger-client
This is Fabric Credential Manager API

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.1
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import fabric.credmgr.swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import fabric.credmgr.swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from fabric.credmgr.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # version
    api_response = api_instance.version_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->version_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://127.0.0.1:7000/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**version_get**](docs/DefaultApi.md#version_get) | **GET** /version | version
*TokensApi* | [**tokens_create_post**](docs/TokensApi.md#tokens_create_post) | **POST** /tokens/create | Generate tokens for an user
*TokensApi* | [**tokens_refresh_post**](docs/TokensApi.md#tokens_refresh_post) | **POST** /tokens/refresh | Refresh tokens for an user
*TokensApi* | [**tokens_revoke_post**](docs/TokensApi.md#tokens_revoke_post) | **POST** /tokens/revoke | Revoke a refresh token for an user

## Documentation For Models

 - [Request](docs/Request.md)
 - [Success](docs/Success.md)
 - [Version](docs/Version.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author

kthare10@unc.edu
