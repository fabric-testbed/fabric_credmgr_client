# coding: utf-8

"""
    Fabric Credential Manager API

    This is Fabric Credential Manager API  # noqa: E501

    OpenAPI spec version: 1.0.1
    Contact: kthare10@unc.edu
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

from fabric.credmgr.swagger_client.api.tokens_api import TokensApi  # noqa: E501


class TestTokensApi(unittest.TestCase):
    """TokensApi unit test stubs"""

    def setUp(self):
        self.api = TokensApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_tokens_create_post(self):
        """Test case for tokens_create_post

        Generate tokens for an user  # noqa: E501
        """
        pass

    def test_tokens_refresh_post(self):
        """Test case for tokens_refresh_post

        Refresh tokens for an user  # noqa: E501
        """
        pass

    def test_tokens_revoke_post(self):
        """Test case for tokens_revoke_post

        Revoke a refresh token for an user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
