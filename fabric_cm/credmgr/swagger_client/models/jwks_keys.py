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

class JwksKeys(object):
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
        'kty': 'str',
        'e': 'str',
        'n': 'str',
        'use': 'str',
        'alg': 'str',
        'kid': 'str'
    }

    attribute_map = {
        'kty': 'kty',
        'e': 'e',
        'n': 'n',
        'use': 'use',
        'alg': 'alg',
        'kid': 'kid'
    }

    def __init__(self, kty=None, e=None, n=None, use=None, alg=None, kid=None):  # noqa: E501
        """JwksKeys - a model defined in Swagger"""  # noqa: E501
        self._kty = None
        self._e = None
        self._n = None
        self._use = None
        self._alg = None
        self._kid = None
        self.discriminator = None
        if kty is not None:
            self.kty = kty
        if e is not None:
            self.e = e
        if n is not None:
            self.n = n
        if use is not None:
            self.use = use
        if alg is not None:
            self.alg = alg
        if kid is not None:
            self.kid = kid

    @property
    def kty(self):
        """Gets the kty of this JwksKeys.  # noqa: E501

        Key Type  # noqa: E501

        :return: The kty of this JwksKeys.  # noqa: E501
        :rtype: str
        """
        return self._kty

    @kty.setter
    def kty(self, kty):
        """Sets the kty of this JwksKeys.

        Key Type  # noqa: E501

        :param kty: The kty of this JwksKeys.  # noqa: E501
        :type: str
        """

        self._kty = kty

    @property
    def e(self):
        """Gets the e of this JwksKeys.  # noqa: E501

        Exponent Parameter  # noqa: E501

        :return: The e of this JwksKeys.  # noqa: E501
        :rtype: str
        """
        return self._e

    @e.setter
    def e(self, e):
        """Sets the e of this JwksKeys.

        Exponent Parameter  # noqa: E501

        :param e: The e of this JwksKeys.  # noqa: E501
        :type: str
        """

        self._e = e

    @property
    def n(self):
        """Gets the n of this JwksKeys.  # noqa: E501

        Modulus Parameter  # noqa: E501

        :return: The n of this JwksKeys.  # noqa: E501
        :rtype: str
        """
        return self._n

    @n.setter
    def n(self, n):
        """Sets the n of this JwksKeys.

        Modulus Parameter  # noqa: E501

        :param n: The n of this JwksKeys.  # noqa: E501
        :type: str
        """

        self._n = n

    @property
    def use(self):
        """Gets the use of this JwksKeys.  # noqa: E501

        Public Key Use Parameter  # noqa: E501

        :return: The use of this JwksKeys.  # noqa: E501
        :rtype: str
        """
        return self._use

    @use.setter
    def use(self, use):
        """Sets the use of this JwksKeys.

        Public Key Use Parameter  # noqa: E501

        :param use: The use of this JwksKeys.  # noqa: E501
        :type: str
        """

        self._use = use

    @property
    def alg(self):
        """Gets the alg of this JwksKeys.  # noqa: E501

        Algorithm Parameter  # noqa: E501

        :return: The alg of this JwksKeys.  # noqa: E501
        :rtype: str
        """
        return self._alg

    @alg.setter
    def alg(self, alg):
        """Sets the alg of this JwksKeys.

        Algorithm Parameter  # noqa: E501

        :param alg: The alg of this JwksKeys.  # noqa: E501
        :type: str
        """

        self._alg = alg

    @property
    def kid(self):
        """Gets the kid of this JwksKeys.  # noqa: E501

        Key Id Header Parameter  # noqa: E501

        :return: The kid of this JwksKeys.  # noqa: E501
        :rtype: str
        """
        return self._kid

    @kid.setter
    def kid(self, kid):
        """Sets the kid of this JwksKeys.

        Key Id Header Parameter  # noqa: E501

        :param kid: The kid of this JwksKeys.  # noqa: E501
        :type: str
        """

        self._kid = kid

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
        if issubclass(JwksKeys, dict):
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
        if not isinstance(other, JwksKeys):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
