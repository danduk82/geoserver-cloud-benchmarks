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
from geoserver.api.workspaces_api import WorkspacesApi  # noqa: E501
from geoserver.rest import ApiException


class TestWorkspacesApi(unittest.TestCase):
    """WorkspacesApi unit test stubs"""

    def setUp(self):
        self.api = WorkspacesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_workspace(self):
        """Test case for create_workspace

        add a new workspace to GeoServer  # noqa: E501
        """
        pass

    def test_delete_workspace(self):
        """Test case for delete_workspace

        """
        pass

    def test_get_workspace(self):
        """Test case for get_workspace

        Retrieve a Workspace  # noqa: E501
        """
        pass

    def test_get_workspaces(self):
        """Test case for get_workspaces

        Get a list of workspaces  # noqa: E501
        """
        pass

    def test_modify_workspace(self):
        """Test case for modify_workspace

        Update a workspace  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
