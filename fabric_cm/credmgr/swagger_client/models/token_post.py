# coding: utf-8

"""
    Fabric Credential Manager API

    This is Fabric Credential Manager API  # noqa: E501

    OpenAPI spec version: 1.0.2
    Contact: kthare10@unc.edu
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class TokenPost(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'str',
        'token': 'str'
    }

    attribute_map = {
        'type': 'type',
        'token': 'token'
    }

    def __init__(self, type=None, token=None):  # noqa: E501
        """TokenPost - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._token = None
        self.discriminator = None
        self.type = type
        self.token = token

    @property
    def type(self):
        """Gets the type of this TokenPost.  # noqa: E501

        Token Type  # noqa: E501

        :return: The type of this TokenPost.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TokenPost.

        Token Type  # noqa: E501

        :param type: The type of this TokenPost.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["identity", "refresh"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def token(self):
        """Gets the token of this TokenPost.  # noqa: E501

        Refresh Token or Token Hash  # noqa: E501

        :return: The token of this TokenPost.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this TokenPost.

        Refresh Token or Token Hash  # noqa: E501

        :param token: The token of this TokenPost.  # noqa: E501
        :type: str
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(TokenPost, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TokenPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
