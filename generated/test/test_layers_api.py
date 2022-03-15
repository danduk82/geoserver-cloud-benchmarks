# coding: utf-8

"""
    GeoServer Workspace

    A workspace is a grouping of data stores. Similar to a namespace, it is used to group data that is related in some way.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import geoserver
from geoserver.api.layers_api import LayersApi  # noqa: E501
from geoserver.rest import ApiException


class TestLayersApi(unittest.TestCase):
    """LayersApi unit test stubs"""

    def setUp(self):
        self.api = LayersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_layer(self):
        """Test case for delete_layer

        Delete layer  # noqa: E501
        """
        pass

    def test_delete_layer_by_workspace(self):
        """Test case for delete_layer_by_workspace

        Delete layer  # noqa: E501
        """
        pass

    def test_get_layer(self):
        """Test case for get_layer

        Retrieve a layer  # noqa: E501
        """
        pass

    def test_get_layer_by_workspace(self):
        """Test case for get_layer_by_workspace

        Retrieve a layer  # noqa: E501
        """
        pass

    def test_get_layers(self):
        """Test case for get_layers

        Get a list of layers  # noqa: E501
        """
        pass

    def test_get_layers_by_workspace(self):
        """Test case for get_layers_by_workspace

        Get a list of layers in a workspace.  # noqa: E501
        """
        pass

    def test_update_layer(self):
        """Test case for update_layer

        Modify a layer.  # noqa: E501
        """
        pass

    def test_update_layer_by_workspace(self):
        """Test case for update_layer_by_workspace

        Modify a layer.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
