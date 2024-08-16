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
from pydantic import Field, StrictStr

from typing import List, Optional

from dreamcatcher.models.chat_completion_response import ChatCompletionResponse
from dreamcatcher.models.completion import Completion
from dreamcatcher.models.completion_response import CompletionResponse
from dreamcatcher.models.create_chat_completion import CreateChatCompletion
from dreamcatcher.models.list_endpoint_response_inner import ListEndpointResponseInner
from dreamcatcher.models.list_models_response import ListModelsResponse
from dreamcatcher.models.show_endpoint_response import ShowEndpointResponse

from dreamcatcher.api_client import ApiClient
from dreamcatcher.api_response import ApiResponse
from dreamcatcher.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class EndpointsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    async def dreamcatcher_web_endpoint_controller_index(self, **kwargs) -> List[ListEndpointResponseInner]:  # noqa: E501
        """List endpoints  # noqa: E501


        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[ListEndpointResponseInner]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the dreamcatcher_web_endpoint_controller_index_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return await self.dreamcatcher_web_endpoint_controller_index_with_http_info(**kwargs)  # noqa: E501

    @validate_arguments
    async def dreamcatcher_web_endpoint_controller_index_with_http_info(self, **kwargs) -> ApiResponse:  # noqa: E501
        """List endpoints  # noqa: E501


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
        :rtype: tuple(List[ListEndpointResponseInner], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
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
                    " to method dreamcatcher_web_endpoint_controller_index" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

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
            '200': "List[ListEndpointResponseInner]",
        }

        return await self.api_client.call_api(
            '/api/v1/endpoints', 'GET',
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
    async def dreamcatcher_web_endpoint_controller_invoke_chat_completions(self, endpoint_name : Annotated[StrictStr, Field(..., description="Endpoint name")], create_chat_completion : Annotated[Optional[CreateChatCompletion], Field(description="Chat completion params")] = None, **kwargs) -> ChatCompletionResponse:  # noqa: E501
        """Invoke a chat completion  # noqa: E501


        :param endpoint_name: Endpoint name (required)
        :type endpoint_name: str
        :param create_chat_completion: Chat completion params
        :type create_chat_completion: CreateChatCompletion
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ChatCompletionResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the dreamcatcher_web_endpoint_controller_invoke_chat_completions_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return await self.dreamcatcher_web_endpoint_controller_invoke_chat_completions_with_http_info(endpoint_name, create_chat_completion, **kwargs)  # noqa: E501

    @validate_arguments
    async def dreamcatcher_web_endpoint_controller_invoke_chat_completions_with_http_info(self, endpoint_name : Annotated[StrictStr, Field(..., description="Endpoint name")], create_chat_completion : Annotated[Optional[CreateChatCompletion], Field(description="Chat completion params")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Invoke a chat completion  # noqa: E501


        :param endpoint_name: Endpoint name (required)
        :type endpoint_name: str
        :param create_chat_completion: Chat completion params
        :type create_chat_completion: CreateChatCompletion
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
        :rtype: tuple(ChatCompletionResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'endpoint_name',
            'create_chat_completion'
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
                    " to method dreamcatcher_web_endpoint_controller_invoke_chat_completions" % _key
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
        if _params['create_chat_completion'] is not None:
            _body_params = _params['create_chat_completion']

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
            '200': "ChatCompletionResponse",
        }

        return await self.api_client.call_api(
            '/api/v1/endpoints/{endpoint_name}/openai/v1/chat/completions', 'POST',
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
    async def dreamcatcher_web_endpoint_controller_invoke_completions(self, endpoint_name : Annotated[StrictStr, Field(..., description="Endpoint name")], completion : Annotated[Optional[Completion], Field(description="Completion params")] = None, **kwargs) -> CompletionResponse:  # noqa: E501
        """Invoke a completion  # noqa: E501


        :param endpoint_name: Endpoint name (required)
        :type endpoint_name: str
        :param completion: Completion params
        :type completion: Completion
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CompletionResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the dreamcatcher_web_endpoint_controller_invoke_completions_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return await self.dreamcatcher_web_endpoint_controller_invoke_completions_with_http_info(endpoint_name, completion, **kwargs)  # noqa: E501

    @validate_arguments
    async def dreamcatcher_web_endpoint_controller_invoke_completions_with_http_info(self, endpoint_name : Annotated[StrictStr, Field(..., description="Endpoint name")], completion : Annotated[Optional[Completion], Field(description="Completion params")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Invoke a completion  # noqa: E501


        :param endpoint_name: Endpoint name (required)
        :type endpoint_name: str
        :param completion: Completion params
        :type completion: Completion
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
        :rtype: tuple(CompletionResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'endpoint_name',
            'completion'
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
                    " to method dreamcatcher_web_endpoint_controller_invoke_completions" % _key
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
        if _params['completion'] is not None:
            _body_params = _params['completion']

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
            '200': "CompletionResponse",
        }

        return await self.api_client.call_api(
            '/api/v1/endpoints/{endpoint_name}/openai/v1/completions', 'POST',
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
    async def dreamcatcher_web_endpoint_controller_models(self, endpoint_name : Annotated[StrictStr, Field(..., description="Endpoint name")], **kwargs) -> ListModelsResponse:  # noqa: E501
        """Lists upstreams (ie models) for an endpoint  # noqa: E501


        :param endpoint_name: Endpoint name (required)
        :type endpoint_name: str
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ListModelsResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the dreamcatcher_web_endpoint_controller_models_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return await self.dreamcatcher_web_endpoint_controller_models_with_http_info(endpoint_name, **kwargs)  # noqa: E501

    @validate_arguments
    async def dreamcatcher_web_endpoint_controller_models_with_http_info(self, endpoint_name : Annotated[StrictStr, Field(..., description="Endpoint name")], **kwargs) -> ApiResponse:  # noqa: E501
        """Lists upstreams (ie models) for an endpoint  # noqa: E501


        :param endpoint_name: Endpoint name (required)
        :type endpoint_name: str
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
        :rtype: tuple(ListModelsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'endpoint_name'
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
                    " to method dreamcatcher_web_endpoint_controller_models" % _key
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
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['authorization']  # noqa: E501

        _response_types_map = {
            '200': "ListModelsResponse",
        }

        return await self.api_client.call_api(
            '/api/v1/endpoints/{endpoint_name}/openai/v1/models', 'GET',
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
    async def dreamcatcher_web_endpoint_controller_show(self, id : Annotated[StrictStr, Field(..., description="Endpoint name")], **kwargs) -> ShowEndpointResponse:  # noqa: E501
        """Get an endpoint  # noqa: E501


        :param id: Endpoint name (required)
        :type id: str
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ShowEndpointResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the dreamcatcher_web_endpoint_controller_show_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return await self.dreamcatcher_web_endpoint_controller_show_with_http_info(id, **kwargs)  # noqa: E501

    @validate_arguments
    async def dreamcatcher_web_endpoint_controller_show_with_http_info(self, id : Annotated[StrictStr, Field(..., description="Endpoint name")], **kwargs) -> ApiResponse:  # noqa: E501
        """Get an endpoint  # noqa: E501


        :param id: Endpoint name (required)
        :type id: str
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
        :rtype: tuple(ShowEndpointResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
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
                    " to method dreamcatcher_web_endpoint_controller_show" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
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
            '200': "ShowEndpointResponse",
        }

        return await self.api_client.call_api(
            '/api/v1/endpoints/{id}', 'GET',
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
