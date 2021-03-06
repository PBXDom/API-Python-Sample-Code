# coding: utf-8

"""
    <PBXDom API>


    OpenAPI spec version: 2.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    
        http://www.apache.org/licenses/LICENSE-2.0
    
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class DefaultApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def calls_get(self, rpt_type, rpt_id, **kwargs):
        """
        
        Gets `Calls` info. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.calls_get(rpt_type, rpt_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param float rpt_type: Report type. (0 report, 1 widget, 2 chart). (required)
        :param float rpt_id: Report id. (required)
        :param float start: Start offset.
        :param float limit: Number of results to return. Max 10K.
        :param str sort_by: Sort column.
        :param str sort_type: Sort mode asc/desc.
        :param str from_date: Start date time.
        :param str to_date: End date time.
        :param float duration: Duration range.
        :param str phone: List of caller phone.
        :param str phone1: List of dialled phones.
        :param str co: List of trunk/co.
        :param str ext: list of extensions.
        :param float pbx_id: list of PBX Ids.
        :param float call_source: list of callsource.
        :param float call_type: list of call type signatures.(5 Unanswered Calls, 7 Transfered Calls, 8 Forwarded Calls)
        :param float direction: list of direction.(0 incoming, 1 outgoing, 2 internal)
        :param str caller_name: list of caller name.
        :param str did: list of did.
        :param str dnis: list of dnis.
        :param str acc: list of account code.
        :param float ring: Ring range.Seconds unit.
        :param float cost: Cost range.
        :param float group: Department/Group id.
        :return: list[InlineResponse200]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['rpt_type', 'rpt_id', 'start', 'limit', 'sort_by', 'sort_type', 'from_date', 'to_date', 'duration', 'phone', 'phone1', 'co', 'ext', 'pbx_id', 'call_source', 'call_type', 'direction', 'caller_name', 'did', 'dnis', 'acc', 'ring', 'cost', 'group']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method calls_get" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'rpt_type' is set
        if ('rpt_type' not in params) or (params['rpt_type'] is None):
            raise ValueError("Missing the required parameter `rpt_type` when calling `calls_get`")
        # verify the required parameter 'rpt_id' is set
        if ('rpt_id' not in params) or (params['rpt_id'] is None):
            raise ValueError("Missing the required parameter `rpt_id` when calling `calls_get`")


        resource_path = '/Calls'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'rpt_type' in params:
            query_params['rptType'] = params['rpt_type']
        if 'rpt_id' in params:
            query_params['rptId'] = params['rpt_id']
        if 'start' in params:
            query_params['start'] = params['start']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'sort_by' in params:
            query_params['sortBy'] = params['sort_by']
        if 'sort_type' in params:
            query_params['sortType'] = params['sort_type']
        if 'from_date' in params:
            query_params['fromDate'] = params['from_date']
        if 'to_date' in params:
            query_params['toDate'] = params['to_date']
        if 'duration' in params:
            query_params['duration'] = params['duration']
        if 'phone' in params:
            query_params['phone'] = params['phone']
        if 'phone1' in params:
            query_params['phone1'] = params['phone1']
        if 'co' in params:
            query_params['co'] = params['co']
        if 'ext' in params:
            query_params['ext'] = params['ext']
        if 'pbx_id' in params:
            query_params['pbxId'] = params['pbx_id']
        if 'call_source' in params:
            query_params['callSource'] = params['call_source']
        if 'call_type' in params:
            query_params['callType'] = params['call_type']
        if 'direction' in params:
            query_params['direction'] = params['direction']
        if 'caller_name' in params:
            query_params['callerName'] = params['caller_name']
        if 'did' in params:
            query_params['did'] = params['did']
        if 'dnis' in params:
            query_params['dnis'] = params['dnis']
        if 'acc' in params:
            query_params['acc'] = params['acc']
        if 'ring' in params:
            query_params['ring'] = params['ring']
        if 'cost' in params:
            query_params['cost'] = params['cost']
        if 'group' in params:
            query_params['group'] = params['group']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[InlineResponse200]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def features_charts_get(self, **kwargs):
        """
        
        Gets `Charts` list. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.features_charts_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[InlineResponse200]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method features_charts_get" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/Features/charts'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[InlineResponse200]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def features_reports_get(self, **kwargs):
        """
        
        Gets `Reports` list. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.features_reports_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[InlineResponse200]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method features_reports_get" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/Features/reports'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[InlineResponse200]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def features_widget_get(self, **kwargs):
        """
        
        Gets `Widgets` list. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.features_widget_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[InlineResponse200]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method features_widget_get" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/Features/widget'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[InlineResponse200]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
