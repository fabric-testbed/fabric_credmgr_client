#!/usr/bin/env python3
# MIT License
#
# Copyright (c) 2020 FABRIC Testbed
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
#
# Author: Komal Thareja (kthare10@renci.org)
import enum
import json
from datetime import datetime
from typing import Tuple, Any

from atomicwrites import atomic_write

from fabric_cm.credmgr import swagger_client
from fabric_cm.credmgr.swagger_client.rest import ApiException as CredMgrException


@enum.unique
class Status(enum.Enum):
    OK = 1
    INVALID_ARGUMENTS = 2
    FAILURE = 3

    def interpret(self, exception=None):
        interpretations = {
            1: "Success",
            2: "Invalid Arguments",
            3: "Failure"
          }
        if exception is None:
            return interpretations[self.value]
        else:
            return str(exception) + ". " + interpretations[self.value]


class CredmgrProxy:
    """
    Credential Manager Proxy
    """
    ID_TOKEN = "id_token"
    REFRESH_TOKEN = "refresh_token"
    TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
    CREATED_AT = "created_at"
    ERROR = "error"

    def __init__(self, credmgr_host: str):
        self.host = credmgr_host
        self.tokens_api = None
        if credmgr_host is not None:
            # create an instance of the API class
            configuration = swagger_client.configuration.Configuration()
            configuration.host = f"https://{credmgr_host}/"
            api_instance = swagger_client.ApiClient(configuration)
            self.tokens_api = swagger_client.TokensApi(api_client=api_instance)
            self.default_api = swagger_client.DefaultApi(api_client=api_instance)

    def refresh(self, project_name: str, scope: str, refresh_token: str,
                file_name: str = None) -> Tuple[Status, dict]:
        """
        Refresh token
        @param project_name project name
        @param scope scope
        @param refresh_token refresh token
        @param file_name File name
        @returns Tuple of Status, dictionary {id_token/error, refresh_token, created_at}. In case of failure, id token would be None
        @raises Exception in case of failure
        """
        try:
            body = swagger_client.Request(refresh_token)
            api_response = self.tokens_api.tokens_refresh_post(body=body,
                                                               project_name=project_name,
                                                               scope=scope)

            api_response_dict = api_response.to_dict()
            tokens_json = {self.ID_TOKEN: api_response_dict[self.ID_TOKEN],
                           self.REFRESH_TOKEN: api_response_dict[self.REFRESH_TOKEN],
                           self.CREATED_AT: datetime.strftime(datetime.utcnow(), self.TIME_FORMAT)}
            if file_name is not None:
                with atomic_write(file_name, overwrite=True) as f:
                    json.dump(tokens_json, f)
            return Status.OK, tokens_json
        except CredMgrException as e:
            message = str(e.body)
            tokens_json = {self.ERROR: e.body,
                           self.CREATED_AT: datetime.strftime(datetime.utcnow(), self.TIME_FORMAT)}
            if message is not None and self.REFRESH_TOKEN in message:
                refresh_token = message.split(f"{self.REFRESH_TOKEN}:")[1]
                refresh_token = refresh_token.strip()
                refresh_token = refresh_token.strip("\"")
                refresh_token = refresh_token.strip("\n")
                tokens_json[self.REFRESH_TOKEN] = refresh_token
            return Status.FAILURE, tokens_json

    def revoke(self, refresh_token: str) -> Tuple[Status, Any]:
        """
        Revoke token
        @param refresh_token refresh token
        @returns response
        @raises Exception in case of failure
        """
        try:
            body = swagger_client.Request(refresh_token)
            self.tokens_api.tokens_revoke_post(body=body)

            return Status.OK, None
        except CredMgrException as e:
            return Status.FAILURE, e.body

    def certs_get(self) -> Tuple[Status, Any]:
        """
        Return certificates
        """
        try:
            certs = self.default_api.certs_get()
            return Status.OK, certs
        except CredMgrException as e:
            return Status.FAILURE, e.body

    def version_get(self) -> Tuple[Status, Any]:
        """
        Return Version
        """
        try:
            version = self.default_api.version_get()
            return Status.OK, version
        except CredMgrException as e:
            return Status.FAILURE, e.body
