# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.endpoints_api import EndpointsApi


class TestEndpointsApi(unittest.TestCase):
    """EndpointsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = EndpointsApi()

    def tearDown(self) -> None:
        pass

    def test_dreamcatcher_web_endpoint_controller_index(self) -> None:
        """Test case for dreamcatcher_web_endpoint_controller_index

        List endpoints
        """
        pass

    def test_dreamcatcher_web_endpoint_controller_show(self) -> None:
        """Test case for dreamcatcher_web_endpoint_controller_show

        Get an endpoint
        """
        pass


if __name__ == '__main__':
    unittest.main()
