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

class GmlSettings(object):
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
        'srs_name_style': 'list[SrsNameStyle]',
        'override_gml_attributes': 'bool'
    }

    attribute_map = {
        'srs_name_style': 'srsNameStyle',
        'override_gml_attributes': 'overrideGMLAttributes'
    }

    def __init__(self, srs_name_style=None, override_gml_attributes=None):  # noqa: E501
        """GmlSettings - a model defined in Swagger"""  # noqa: E501
        self._srs_name_style = None
        self._override_gml_attributes = None
        self.discriminator = None
        if srs_name_style is not None:
            self.srs_name_style = srs_name_style
        if override_gml_attributes is not None:
            self.override_gml_attributes = override_gml_attributes

    @property
    def srs_name_style(self):
        """Gets the srs_name_style of this GmlSettings.  # noqa: E501


        :return: The srs_name_style of this GmlSettings.  # noqa: E501
        :rtype: list[SrsNameStyle]
        """
        return self._srs_name_style

    @srs_name_style.setter
    def srs_name_style(self, srs_name_style):
        """Sets the srs_name_style of this GmlSettings.


        :param srs_name_style: The srs_name_style of this GmlSettings.  # noqa: E501
        :type: list[SrsNameStyle]
        """

        self._srs_name_style = srs_name_style

    @property
    def override_gml_attributes(self):
        """Gets the override_gml_attributes of this GmlSettings.  # noqa: E501

        Controls how attributes are handled with regard to attributes defined in the schema of AbstractFeatureType, name, description, etc... When set this flag will cause the attributes to be redefined in the application schema namespace.  # noqa: E501

        :return: The override_gml_attributes of this GmlSettings.  # noqa: E501
        :rtype: bool
        """
        return self._override_gml_attributes

    @override_gml_attributes.setter
    def override_gml_attributes(self, override_gml_attributes):
        """Sets the override_gml_attributes of this GmlSettings.

        Controls how attributes are handled with regard to attributes defined in the schema of AbstractFeatureType, name, description, etc... When set this flag will cause the attributes to be redefined in the application schema namespace.  # noqa: E501

        :param override_gml_attributes: The override_gml_attributes of this GmlSettings.  # noqa: E501
        :type: bool
        """

        self._override_gml_attributes = override_gml_attributes

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
        if issubclass(GmlSettings, dict):
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
        if not isinstance(other, GmlSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
