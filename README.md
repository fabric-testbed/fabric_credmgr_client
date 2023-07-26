[![PyPI](https://img.shields.io/pypi/v/fabric_credmgr_client?style=plastic)](https://pypi.org/project/fabric_credmgr_client/)

# Fabric Credential Manager Client
This is Fabric Credential Manager API

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.1
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 3.9+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/fabric-testbed/fabric_credmgr.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/fabric-testbed/fabric_credmgr.git`)

Then import the package:
```python
import fabric_cm.credmgr.credmgr_proxy 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
from fabric_cm.credmgr.credmgr_proxy import CredmgrProxy
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from fabric_cm.credmgr.credmgr_proxy import CredmgrProxy
from fabric_cm.credmgr.swagger_client.rest import ApiException

credmgr_proxy = CredmgrProxy(credmgr_host="https://dev-2.fabric-testbed.net/")
try:
    version = credmgr_proxy.version_get()
    print(version)
except ApiException as e:
    print("Exception when calling CredmgrProxy->version_get: %s\n" % e)

try:
    version = credmgr_proxy.certs_get()
    print(version)
except ApiException as e:
    print("Exception when calling CredmgrProxy->certs_get: %s\n" % e)


try:
    version = credmgr_proxy.refresh(project_id='12345', scope='all', refresh_token='TOKEN')
    print(version)
except ApiException as e:
    print("Exception when calling CredmgrProxy->refresh: %s\n" % e)

try:
    version = credmgr_proxy.revoke(refresh_token='TOKEN')
    print(version)
except ApiException as e:
    print("Exception when calling CredmgrProxy->revoke: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://127.0.0.1:7000/credmgr/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**certs_get**](docs/DefaultApi.md#certs_get) | **GET** /certs | Return Public Keys to verify signature of the tokens
*TokensApi* | [**tokens_create_post**](docs/TokensApi.md#tokens_create_post) | **POST** /tokens/create | Generate tokens for an user
*TokensApi* | [**tokens_get**](docs/TokensApi.md#tokens_get) | **GET** /tokens | Get tokens
*TokensApi* | [**tokens_refresh_post**](docs/TokensApi.md#tokens_refresh_post) | **POST** /tokens/refresh | Refresh tokens for an user
*TokensApi* | [**tokens_revoke_list_get**](docs/TokensApi.md#tokens_revoke_list_get) | **GET** /tokens/revoke_list | Get token revoke list i.e. list of revoked identity token hashes
*TokensApi* | [**tokens_revoke_post**](docs/TokensApi.md#tokens_revoke_post) | **POST** /tokens/revoke | Revoke a token for an user
*TokensApi* | [**tokens_revokes_post**](docs/TokensApi.md#tokens_revokes_post) | **POST** /tokens/revokes | Revoke a token
*TokensApi* | [**tokens_validate_post**](docs/TokensApi.md#tokens_validate_post) | **POST** /tokens/validate | Validate an identity token issued by Credential Manager
*VersionApi* | [**version_get**](docs/VersionApi.md#version_get) | **GET** /version | Version

## Documentation For Models

 - [DecodedToken](docs/DecodedToken.md)
 - [Jwks](docs/Jwks.md)
 - [JwksKeys](docs/JwksKeys.md)
 - [Request](docs/Request.md)
 - [RevokeList](docs/RevokeList.md)
 - [Status200OkNoContent](docs/Status200OkNoContent.md)
 - [Status200OkNoContentData](docs/Status200OkNoContentData.md)
 - [Status200OkPaginated](docs/Status200OkPaginated.md)
 - [Status200OkSingle](docs/Status200OkSingle.md)
 - [Status400BadRequest](docs/Status400BadRequest.md)
 - [Status400BadRequestErrors](docs/Status400BadRequestErrors.md)
 - [Status401Unauthorized](docs/Status401Unauthorized.md)
 - [Status401UnauthorizedErrors](docs/Status401UnauthorizedErrors.md)
 - [Status403Forbidden](docs/Status403Forbidden.md)
 - [Status403ForbiddenErrors](docs/Status403ForbiddenErrors.md)
 - [Status404NotFound](docs/Status404NotFound.md)
 - [Status404NotFoundErrors](docs/Status404NotFoundErrors.md)
 - [Status500InternalServerError](docs/Status500InternalServerError.md)
 - [Status500InternalServerErrorErrors](docs/Status500InternalServerErrorErrors.md)
 - [Token](docs/Token.md)
 - [TokenPost](docs/TokenPost.md)
 - [Tokens](docs/Tokens.md)
 - [Version](docs/Version.md)
 - [VersionData](docs/VersionData.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author

kthare10@unc.edu
