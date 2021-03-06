# coding: utf-8

"""
    GeoServer Workspace

    A workspace is a grouping of data stores. Similar to a namespace, it is used to group data that is related in some way.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CoverageStoreResponseWrapper(object):
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
        'coverage_store': 'CoverageStoreResponse'
    }

    attribute_map = {
        'coverage_store': 'coverageStore'
    }

    def __init__(self, coverage_store=None):  # noqa: E501
        """CoverageStoreResponseWrapper - a model defined in Swagger"""  # noqa: E501
        self._coverage_store = None
        self.discriminator = None
        self.coverage_store = coverage_store

    @property
    def coverage_store(self):
        """Gets the coverage_store of this CoverageStoreResponseWrapper.  # noqa: E501


        :return: The coverage_store of this CoverageStoreResponseWrapper.  # noqa: E501
        :rtype: CoverageStoreResponse
        """
        return self._coverage_store

    @coverage_store.setter
    def coverage_store(self, coverage_store):
        """Sets the coverage_store of this CoverageStoreResponseWrapper.


        :param coverage_store: The coverage_store of this CoverageStoreResponseWrapper.  # noqa: E501
        :type: CoverageStoreResponse
        """
        if coverage_store is None:
            raise ValueError("Invalid value for `coverage_store`, must not be `None`")  # noqa: E501

        self._coverage_store = coverage_store

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
        if issubclass(CoverageStoreResponseWrapper, dict):
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
        if not isinstance(other, CoverageStoreResponseWrapper):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
