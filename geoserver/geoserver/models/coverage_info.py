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
from geoserver.models.resource_info import ResourceInfo  # noqa: F401,E501

class CoverageInfo(ResourceInfo):
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
        'store': 'CoverageStoreInfo',
        'native_coverage_name': 'str',
        'native_format': 'str',
        'supported_formats': 'list[str]',
        'request_srs': 'list[str]',
        'response_srs': 'list[str]',
        'default_interpolation_method': 'str',
        'interpolation_methods': 'list[str]',
        'parameters': 'dict(str, object)',
        'dimensions': 'list[CoverageDimensionInfo]'
    }
    if hasattr(ResourceInfo, "swagger_types"):
        swagger_types.update(ResourceInfo.swagger_types)

    attribute_map = {
        'store': 'store',
        'native_coverage_name': 'nativeCoverageName',
        'native_format': 'nativeFormat',
        'supported_formats': 'supportedFormats',
        'request_srs': 'requestSRS',
        'response_srs': 'responseSRS',
        'default_interpolation_method': 'defaultInterpolationMethod',
        'interpolation_methods': 'interpolationMethods',
        'parameters': 'parameters',
        'dimensions': 'dimensions'
    }
    if hasattr(ResourceInfo, "attribute_map"):
        attribute_map.update(ResourceInfo.attribute_map)

    def __init__(self, store=None, native_coverage_name=None, native_format=None, supported_formats=None, request_srs=None, response_srs=None, default_interpolation_method=None, interpolation_methods=None, parameters=None, dimensions=None, *args, **kwargs):  # noqa: E501
        """CoverageInfo - a model defined in Swagger"""  # noqa: E501
        self._store = None
        self._native_coverage_name = None
        self._native_format = None
        self._supported_formats = None
        self._request_srs = None
        self._response_srs = None
        self._default_interpolation_method = None
        self._interpolation_methods = None
        self._parameters = None
        self._dimensions = None
        self.discriminator = None
        if store is not None:
            self.store = store
        if native_coverage_name is not None:
            self.native_coverage_name = native_coverage_name
        if native_format is not None:
            self.native_format = native_format
        if supported_formats is not None:
            self.supported_formats = supported_formats
        if request_srs is not None:
            self.request_srs = request_srs
        if response_srs is not None:
            self.response_srs = response_srs
        if default_interpolation_method is not None:
            self.default_interpolation_method = default_interpolation_method
        if interpolation_methods is not None:
            self.interpolation_methods = interpolation_methods
        if parameters is not None:
            self.parameters = parameters
        if dimensions is not None:
            self.dimensions = dimensions
        ResourceInfo.__init__(self, *args, **kwargs)

    @property
    def store(self):
        """Gets the store of this CoverageInfo.  # noqa: E501


        :return: The store of this CoverageInfo.  # noqa: E501
        :rtype: CoverageStoreInfo
        """
        return self._store

    @store.setter
    def store(self, store):
        """Sets the store of this CoverageInfo.


        :param store: The store of this CoverageInfo.  # noqa: E501
        :type: CoverageStoreInfo
        """

        self._store = store

    @property
    def native_coverage_name(self):
        """Gets the native_coverage_name of this CoverageInfo.  # noqa: E501

        the native coverage name (used to pick up a specific coverage from within a reader)  # noqa: E501

        :return: The native_coverage_name of this CoverageInfo.  # noqa: E501
        :rtype: str
        """
        return self._native_coverage_name

    @native_coverage_name.setter
    def native_coverage_name(self, native_coverage_name):
        """Sets the native_coverage_name of this CoverageInfo.

        the native coverage name (used to pick up a specific coverage from within a reader)  # noqa: E501

        :param native_coverage_name: The native_coverage_name of this CoverageInfo.  # noqa: E501
        :type: str
        """

        self._native_coverage_name = native_coverage_name

    @property
    def native_format(self):
        """Gets the native_format of this CoverageInfo.  # noqa: E501

        The native format name of the coverage  # noqa: E501

        :return: The native_format of this CoverageInfo.  # noqa: E501
        :rtype: str
        """
        return self._native_format

    @native_format.setter
    def native_format(self, native_format):
        """Sets the native_format of this CoverageInfo.

        The native format name of the coverage  # noqa: E501

        :param native_format: The native_format of this CoverageInfo.  # noqa: E501
        :type: str
        """

        self._native_format = native_format

    @property
    def supported_formats(self):
        """Gets the supported_formats of this CoverageInfo.  # noqa: E501

        The supported formats for the coverage  # noqa: E501

        :return: The supported_formats of this CoverageInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._supported_formats

    @supported_formats.setter
    def supported_formats(self, supported_formats):
        """Sets the supported_formats of this CoverageInfo.

        The supported formats for the coverage  # noqa: E501

        :param supported_formats: The supported_formats of this CoverageInfo.  # noqa: E501
        :type: list[str]
        """

        self._supported_formats = supported_formats

    @property
    def request_srs(self):
        """Gets the request_srs of this CoverageInfo.  # noqa: E501

        The collection of identifiers of the crs's the coverage supports in a request.  # noqa: E501

        :return: The request_srs of this CoverageInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._request_srs

    @request_srs.setter
    def request_srs(self, request_srs):
        """Sets the request_srs of this CoverageInfo.

        The collection of identifiers of the crs's the coverage supports in a request.  # noqa: E501

        :param request_srs: The request_srs of this CoverageInfo.  # noqa: E501
        :type: list[str]
        """

        self._request_srs = request_srs

    @property
    def response_srs(self):
        """Gets the response_srs of this CoverageInfo.  # noqa: E501

        The collection of identifiers of the crs's the coverage supports in a response.  # noqa: E501

        :return: The response_srs of this CoverageInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._response_srs

    @response_srs.setter
    def response_srs(self, response_srs):
        """Sets the response_srs of this CoverageInfo.

        The collection of identifiers of the crs's the coverage supports in a response.  # noqa: E501

        :param response_srs: The response_srs of this CoverageInfo.  # noqa: E501
        :type: list[str]
        """

        self._response_srs = response_srs

    @property
    def default_interpolation_method(self):
        """Gets the default_interpolation_method of this CoverageInfo.  # noqa: E501

        Default resampling (interpolation) method that will be used for this coverage.  # noqa: E501

        :return: The default_interpolation_method of this CoverageInfo.  # noqa: E501
        :rtype: str
        """
        return self._default_interpolation_method

    @default_interpolation_method.setter
    def default_interpolation_method(self, default_interpolation_method):
        """Sets the default_interpolation_method of this CoverageInfo.

        Default resampling (interpolation) method that will be used for this coverage.  # noqa: E501

        :param default_interpolation_method: The default_interpolation_method of this CoverageInfo.  # noqa: E501
        :type: str
        """

        self._default_interpolation_method = default_interpolation_method

    @property
    def interpolation_methods(self):
        """Gets the interpolation_methods of this CoverageInfo.  # noqa: E501

        available interporlations methods for this coverage  # noqa: E501

        :return: The interpolation_methods of this CoverageInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._interpolation_methods

    @interpolation_methods.setter
    def interpolation_methods(self, interpolation_methods):
        """Sets the interpolation_methods of this CoverageInfo.

        available interporlations methods for this coverage  # noqa: E501

        :param interpolation_methods: The interpolation_methods of this CoverageInfo.  # noqa: E501
        :type: list[str]
        """

        self._interpolation_methods = interpolation_methods

    @property
    def parameters(self):
        """Gets the parameters of this CoverageInfo.  # noqa: E501


        :return: The parameters of this CoverageInfo.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this CoverageInfo.


        :param parameters: The parameters of this CoverageInfo.  # noqa: E501
        :type: dict(str, object)
        """

        self._parameters = parameters

    @property
    def dimensions(self):
        """Gets the dimensions of this CoverageInfo.  # noqa: E501

        raster dimensions  # noqa: E501

        :return: The dimensions of this CoverageInfo.  # noqa: E501
        :rtype: list[CoverageDimensionInfo]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this CoverageInfo.

        raster dimensions  # noqa: E501

        :param dimensions: The dimensions of this CoverageInfo.  # noqa: E501
        :type: list[CoverageDimensionInfo]
        """

        self._dimensions = dimensions

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
        if issubclass(CoverageInfo, dict):
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
        if not isinstance(other, CoverageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
