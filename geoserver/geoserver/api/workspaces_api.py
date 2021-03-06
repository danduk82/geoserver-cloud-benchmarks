# coding: utf-8

"""
    GeoServer Workspace

    A workspace is a grouping of data stores. Similar to a namespace, it is used to group data that is related in some way.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from geoserver.api_client import ApiClient


class WorkspacesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_workspace(self, body, **kwargs):  # noqa: E501
        """add a new workspace to GeoServer  # noqa: E501

        Adds a new workspace to the server  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_workspace(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WorkspaceWrapper body: The Workspace body information to upload. (required)
        :param bool default: New workspace will be the used as the default. Allowed values are true or false,  The default value is false.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_workspace_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_workspace_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_workspace_with_http_info(self, body, **kwargs):  # noqa: E501
        """add a new workspace to GeoServer  # noqa: E501

        Adds a new workspace to the server  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_workspace_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WorkspaceWrapper body: The Workspace body information to upload. (required)
        :param bool default: New workspace will be the used as the default. Allowed values are true or false,  The default value is false.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'default']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_workspace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_workspace`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'default' in params:
            query_params.append(('default', params['default']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/workspaces', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_workspace(self, workspace, **kwargs):  # noqa: E501
        """delete_workspace  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_workspace(workspace, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workspace: the name of the workspace to fetch (required)
        :param bool recurse: delete workspace contents (default false)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_workspace_with_http_info(workspace, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_workspace_with_http_info(workspace, **kwargs)  # noqa: E501
            return data

    def delete_workspace_with_http_info(self, workspace, **kwargs):  # noqa: E501
        """delete_workspace  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_workspace_with_http_info(workspace, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workspace: the name of the workspace to fetch (required)
        :param bool recurse: delete workspace contents (default false)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workspace', 'recurse']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_workspace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workspace' is set
        if ('workspace' not in params or
                params['workspace'] is None):
            raise ValueError("Missing the required parameter `workspace` when calling `delete_workspace`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'workspace' in params:
            path_params['workspace'] = params['workspace']  # noqa: E501

        query_params = []
        if 'recurse' in params:
            query_params.append(('recurse', params['recurse']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/workspaces/{workspace}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_workspace(self, workspace, **kwargs):  # noqa: E501
        """Retrieve a Workspace  # noqa: E501

        Retrieves a single workspace definition.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_workspace(workspace, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workspace: the name of the workspace to fetch (required)
        :param bool quiet_on_not_found:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_workspace_with_http_info(workspace, **kwargs)  # noqa: E501
        else:
            (data) = self.get_workspace_with_http_info(workspace, **kwargs)  # noqa: E501
            return data

    def get_workspace_with_http_info(self, workspace, **kwargs):  # noqa: E501
        """Retrieve a Workspace  # noqa: E501

        Retrieves a single workspace definition.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_workspace_with_http_info(workspace, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workspace: the name of the workspace to fetch (required)
        :param bool quiet_on_not_found:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workspace', 'quiet_on_not_found']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workspace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workspace' is set
        if ('workspace' not in params or
                params['workspace'] is None):
            raise ValueError("Missing the required parameter `workspace` when calling `get_workspace`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'workspace' in params:
            path_params['workspace'] = params['workspace']  # noqa: E501

        query_params = []
        if 'quiet_on_not_found' in params:
            query_params.append(('quietOnNotFound', params['quiet_on_not_found']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/workspaces/{workspace}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_workspaces(self, **kwargs):  # noqa: E501
        """Get a list of workspaces  # noqa: E501

        Displays a list of all workspaces on the server.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_workspaces(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: WorkspacesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_workspaces_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_workspaces_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_workspaces_with_http_info(self, **kwargs):  # noqa: E501
        """Get a list of workspaces  # noqa: E501

        Displays a list of all workspaces on the server.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_workspaces_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: WorkspacesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workspaces" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/workspaces', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WorkspacesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def modify_workspace(self, body, workspace, **kwargs):  # noqa: E501
        """Update a workspace  # noqa: E501

        takes the body of the post and modifies the workspace from it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_workspace(body, workspace, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WorkspaceWrapper body: The Workspace body information to upload. (required)
        :param str workspace: the name of the workspace to fetch (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.modify_workspace_with_http_info(body, workspace, **kwargs)  # noqa: E501
        else:
            (data) = self.modify_workspace_with_http_info(body, workspace, **kwargs)  # noqa: E501
            return data

    def modify_workspace_with_http_info(self, body, workspace, **kwargs):  # noqa: E501
        """Update a workspace  # noqa: E501

        takes the body of the post and modifies the workspace from it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_workspace_with_http_info(body, workspace, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WorkspaceWrapper body: The Workspace body information to upload. (required)
        :param str workspace: the name of the workspace to fetch (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'workspace']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method modify_workspace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `modify_workspace`")  # noqa: E501
        # verify the required parameter 'workspace' is set
        if ('workspace' not in params or
                params['workspace'] is None):
            raise ValueError("Missing the required parameter `workspace` when calling `modify_workspace`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'workspace' in params:
            path_params['workspace'] = params['workspace']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/workspaces/{workspace}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
