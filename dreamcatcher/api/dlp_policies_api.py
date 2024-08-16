# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing import overload, Optional, Union, Awaitable

from typing_extensions import Annotated
from pydantic import Field, StrictInt, StrictStr

from typing import Optional

from dreamcatcher.models.dlp_policy import DlpPolicy
from dreamcatcher.models.dlp_policy_params import DlpPolicyParams
from dreamcatcher.models.dreamcatcher_web_presidio_policy_controller_scan200_response import DreamcatcherWebPresidioPolicyControllerScan200Response
from dreamcatcher.models.dreamcatcher_web_presidio_policy_controller_scan_request import DreamcatcherWebPresidioPolicyControllerScanRequest

from dreamcatcher.api_client import ApiClient
from dreamcatcher.api_response import ApiResponse
from dreamcatcher.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class DlpPoliciesApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    async def dreamcatcher_web_presidio_policy_controller_create(self, endpoint_name : Annotated[StrictStr, Field(..., description="Endpoint name")], dlp_policy_params : Annotated[Optional[DlpPolicyParams], Field(description="DLP policy params")] = None, **kwargs) -> DlpPolicy:  # noqa: E501
        """Create a DLP policy  # noqa: E501


        :param endpoint_name: Endpoint name (required)
        :type endpoint_name: str
        :param dlp_policy_params: DLP policy params
        :type dlp_policy_params: DlpPolicyParams
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DlpPolicy
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the dreamcatcher_web_presidio_policy_controller_create_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return await self.dreamcatcher_web_presidio_policy_controller_create_with_http_info(endpoint_name, dlp_policy_params, **kwargs)  # noqa: E501

    @validate_arguments
    async def dreamcatcher_web_presidio_policy_controller_create_with_http_info(self, endpoint_name : Annotated[StrictStr, Field(..., description="Endpoint name")], dlp_policy_params : Annotated[Optional[DlpPolicyParams], Field(description="DLP policy params")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Create a DLP policy  # noqa: E501


        :param endpoint_name: Endpoint name (required)
        :type endpoint_name: str
        :param dlp_policy_params: DLP policy params
        :type dlp_policy_params: DlpPolicyParams
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(DlpPolicy, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'endpoint_name',
            'dlp_policy_params'
        ]
        _all_params.extend(
            [
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method dreamcatcher_web_presidio_policy_controller_create" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['endpoint_name'] is not None:
            _path_params['endpoint_name'] = _params['endpoint_name']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['dlp_policy_params'] is not None:
            _body_params = _params['dlp_policy_params']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['authorization']  # noqa: E501

        _response_types_map = {
            '200': "DlpPolicy",
        }

        return await self.api_client.call_api(
            '/api/v1/endpoints/{endpoint_name}/policies/dlp', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    async def dreamcatcher_web_presidio_policy_controller_delete(self, endpoint_name : Annotated[StrictStr, Field(..., description="Endpoint name")], id : Annotated[StrictInt, Field(..., description="DLP Policy ID")], **kwargs) -> None:  # noqa: E501
        """Delete a DLP policy  # noqa: E501


        :param endpoint_name: Endpoint name (required)
        :type endpoint_name: str
        :param id: DLP Policy ID (required)
        :type id: int
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the dreamcatcher_web_presidio_policy_controller_delete_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return await self.dreamcatcher_web_presidio_policy_controller_delete_with_http_info(endpoint_name, id, **kwargs)  # noqa: E501

    @validate_arguments
    async def dreamcatcher_web_presidio_policy_controller_delete_with_http_info(self, endpoint_name : Annotated[StrictStr, Field(..., description="Endpoint name")], id : Annotated[StrictInt, Field(..., description="DLP Policy ID")], **kwargs) -> ApiResponse:  # noqa: E501
        """Delete a DLP policy  # noqa: E501


        :param endpoint_name: Endpoint name (required)
        :type endpoint_name: str
        :param id: DLP Policy ID (required)
        :type id: int
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'endpoint_name',
            'id'
        ]
        _all_params.extend(
            [
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method dreamcatcher_web_presidio_policy_controller_delete" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['endpoint_name'] is not None:
            _path_params['endpoint_name'] = _params['endpoint_name']

        if _params['id'] is not None:
            _path_params['id'] = _params['id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # authentication setting
        _auth_settings = ['authorization']  # noqa: E501

        _response_types_map = {}

        return await self.api_client.call_api(
            '/api/v1/endpoints/{endpoint_name}/policies/dlp/{id}', 'DELETE',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    async def dreamcatcher_web_presidio_policy_controller_scan(self, endpoint_name : Annotated[StrictStr, Field(..., description="Endpoint name")], id : Annotated[StrictInt, Field(..., description="DLP Policy ID")], dreamcatcher_web_presidio_policy_controller_scan_request : Annotated[Optional[DreamcatcherWebPresidioPolicyControllerScanRequest], Field(description="Content to scan")] = None, **kwargs) -> DreamcatcherWebPresidioPolicyControllerScan200Response:  # noqa: E501
        """Scan content with a DLP policy  # noqa: E501


        :param endpoint_name: Endpoint name (required)
        :type endpoint_name: str
        :param id: DLP Policy ID (required)
        :type id: int
        :param dreamcatcher_web_presidio_policy_controller_scan_request: Content to scan
        :type dreamcatcher_web_presidio_policy_controller_scan_request: DreamcatcherWebPresidioPolicyControllerScanRequest
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DreamcatcherWebPresidioPolicyControllerScan200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the dreamcatcher_web_presidio_policy_controller_scan_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return await self.dreamcatcher_web_presidio_policy_controller_scan_with_http_info(endpoint_name, id, dreamcatcher_web_presidio_policy_controller_scan_request, **kwargs)  # noqa: E501

    @validate_arguments
    async def dreamcatcher_web_presidio_policy_controller_scan_with_http_info(self, endpoint_name : Annotated[StrictStr, Field(..., description="Endpoint name")], id : Annotated[StrictInt, Field(..., description="DLP Policy ID")], dreamcatcher_web_presidio_policy_controller_scan_request : Annotated[Optional[DreamcatcherWebPresidioPolicyControllerScanRequest], Field(description="Content to scan")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Scan content with a DLP policy  # noqa: E501


        :param endpoint_name: Endpoint name (required)
        :type endpoint_name: str
        :param id: DLP Policy ID (required)
        :type id: int
        :param dreamcatcher_web_presidio_policy_controller_scan_request: Content to scan
        :type dreamcatcher_web_presidio_policy_controller_scan_request: DreamcatcherWebPresidioPolicyControllerScanRequest
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(DreamcatcherWebPresidioPolicyControllerScan200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'endpoint_name',
            'id',
            'dreamcatcher_web_presidio_policy_controller_scan_request'
        ]
        _all_params.extend(
            [
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method dreamcatcher_web_presidio_policy_controller_scan" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['endpoint_name'] is not None:
            _path_params['endpoint_name'] = _params['endpoint_name']

        if _params['id'] is not None:
            _path_params['id'] = _params['id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['dreamcatcher_web_presidio_policy_controller_scan_request'] is not None:
            _body_params = _params['dreamcatcher_web_presidio_policy_controller_scan_request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['authorization']  # noqa: E501

        _response_types_map = {
            '200': "DreamcatcherWebPresidioPolicyControllerScan200Response",
        }

        return await self.api_client.call_api(
            '/api/v1/endpoints/{endpoint_name}/policies/dlp/{id}/scan', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    async def dreamcatcher_web_presidio_policy_controller_show(self, endpoint_name : Annotated[StrictStr, Field(..., description="Endpoint name")], id : Annotated[StrictInt, Field(..., description="DLP Policy ID")], **kwargs) -> DlpPolicy:  # noqa: E501
        """Get a DLP policy  # noqa: E501


        :param endpoint_name: Endpoint name (required)
        :type endpoint_name: str
        :param id: DLP Policy ID (required)
        :type id: int
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DlpPolicy
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the dreamcatcher_web_presidio_policy_controller_show_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return await self.dreamcatcher_web_presidio_policy_controller_show_with_http_info(endpoint_name, id, **kwargs)  # noqa: E501

    @validate_arguments
    async def dreamcatcher_web_presidio_policy_controller_show_with_http_info(self, endpoint_name : Annotated[StrictStr, Field(..., description="Endpoint name")], id : Annotated[StrictInt, Field(..., description="DLP Policy ID")], **kwargs) -> ApiResponse:  # noqa: E501
        """Get a DLP policy  # noqa: E501


        :param endpoint_name: Endpoint name (required)
        :type endpoint_name: str
        :param id: DLP Policy ID (required)
        :type id: int
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(DlpPolicy, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'endpoint_name',
            'id'
        ]
        _all_params.extend(
            [
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method dreamcatcher_web_presidio_policy_controller_show" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['endpoint_name'] is not None:
            _path_params['endpoint_name'] = _params['endpoint_name']

        if _params['id'] is not None:
            _path_params['id'] = _params['id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['authorization']  # noqa: E501

        _response_types_map = {
            '200': "DlpPolicy",
        }

        return await self.api_client.call_api(
            '/api/v1/endpoints/{endpoint_name}/policies/dlp/{id}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    async def dreamcatcher_web_presidio_policy_controller_update(self, endpoint_name : Annotated[StrictStr, Field(..., description="Endpoint name")], id : Annotated[StrictInt, Field(..., description="DLP Policy ID")], dlp_policy_params : Annotated[Optional[DlpPolicyParams], Field(description="DLP policy params")] = None, **kwargs) -> DlpPolicy:  # noqa: E501
        """Update a DLP policy  # noqa: E501


        :param endpoint_name: Endpoint name (required)
        :type endpoint_name: str
        :param id: DLP Policy ID (required)
        :type id: int
        :param dlp_policy_params: DLP policy params
        :type dlp_policy_params: DlpPolicyParams
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DlpPolicy
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the dreamcatcher_web_presidio_policy_controller_update_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return await self.dreamcatcher_web_presidio_policy_controller_update_with_http_info(endpoint_name, id, dlp_policy_params, **kwargs)  # noqa: E501

    @validate_arguments
    async def dreamcatcher_web_presidio_policy_controller_update_with_http_info(self, endpoint_name : Annotated[StrictStr, Field(..., description="Endpoint name")], id : Annotated[StrictInt, Field(..., description="DLP Policy ID")], dlp_policy_params : Annotated[Optional[DlpPolicyParams], Field(description="DLP policy params")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Update a DLP policy  # noqa: E501


        :param endpoint_name: Endpoint name (required)
        :type endpoint_name: str
        :param id: DLP Policy ID (required)
        :type id: int
        :param dlp_policy_params: DLP policy params
        :type dlp_policy_params: DlpPolicyParams
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(DlpPolicy, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'endpoint_name',
            'id',
            'dlp_policy_params'
        ]
        _all_params.extend(
            [
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method dreamcatcher_web_presidio_policy_controller_update" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['endpoint_name'] is not None:
            _path_params['endpoint_name'] = _params['endpoint_name']

        if _params['id'] is not None:
            _path_params['id'] = _params['id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['dlp_policy_params'] is not None:
            _body_params = _params['dlp_policy_params']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['authorization']  # noqa: E501

        _response_types_map = {
            '200': "DlpPolicy",
        }

        return await self.api_client.call_api(
            '/api/v1/endpoints/{endpoint_name}/policies/dlp/{id}', 'PATCH',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    async def dreamcatcher_web_presidio_policy_controller_update__2(self, endpoint_name : Annotated[StrictStr, Field(..., description="Endpoint name")], id : Annotated[StrictInt, Field(..., description="DLP Policy ID")], dlp_policy_params : Annotated[Optional[DlpPolicyParams], Field(description="DLP policy params")] = None, **kwargs) -> DlpPolicy:  # noqa: E501
        """Update a DLP policy  # noqa: E501


        :param endpoint_name: Endpoint name (required)
        :type endpoint_name: str
        :param id: DLP Policy ID (required)
        :type id: int
        :param dlp_policy_params: DLP policy params
        :type dlp_policy_params: DlpPolicyParams
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DlpPolicy
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the dreamcatcher_web_presidio_policy_controller_update__2_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return await self.dreamcatcher_web_presidio_policy_controller_update__2_with_http_info(endpoint_name, id, dlp_policy_params, **kwargs)  # noqa: E501

    @validate_arguments
    async def dreamcatcher_web_presidio_policy_controller_update__2_with_http_info(self, endpoint_name : Annotated[StrictStr, Field(..., description="Endpoint name")], id : Annotated[StrictInt, Field(..., description="DLP Policy ID")], dlp_policy_params : Annotated[Optional[DlpPolicyParams], Field(description="DLP policy params")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Update a DLP policy  # noqa: E501


        :param endpoint_name: Endpoint name (required)
        :type endpoint_name: str
        :param id: DLP Policy ID (required)
        :type id: int
        :param dlp_policy_params: DLP policy params
        :type dlp_policy_params: DlpPolicyParams
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(DlpPolicy, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'endpoint_name',
            'id',
            'dlp_policy_params'
        ]
        _all_params.extend(
            [
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method dreamcatcher_web_presidio_policy_controller_update__2" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['endpoint_name'] is not None:
            _path_params['endpoint_name'] = _params['endpoint_name']

        if _params['id'] is not None:
            _path_params['id'] = _params['id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['dlp_policy_params'] is not None:
            _body_params = _params['dlp_policy_params']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['authorization']  # noqa: E501

        _response_types_map = {
            '200': "DlpPolicy",
        }

        return await self.api_client.call_api(
            '/api/v1/endpoints/{endpoint_name}/policies/dlp/{id}', 'PUT',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
