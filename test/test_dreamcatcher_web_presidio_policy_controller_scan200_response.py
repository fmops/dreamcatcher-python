# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from dreamcatcher.models.dreamcatcher_web_presidio_policy_controller_scan200_response import DreamcatcherWebPresidioPolicyControllerScan200Response  # noqa: E501

class TestDreamcatcherWebPresidioPolicyControllerScan200Response(unittest.TestCase):
    """DreamcatcherWebPresidioPolicyControllerScan200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DreamcatcherWebPresidioPolicyControllerScan200Response:
        """Test DreamcatcherWebPresidioPolicyControllerScan200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DreamcatcherWebPresidioPolicyControllerScan200Response`
        """
        model = DreamcatcherWebPresidioPolicyControllerScan200Response()  # noqa: E501
        if include_optional:
            return DreamcatcherWebPresidioPolicyControllerScan200Response(
                violates_policy = True
            )
        else:
            return DreamcatcherWebPresidioPolicyControllerScan200Response(
        )
        """

    def testDreamcatcherWebPresidioPolicyControllerScan200Response(self):
        """Test DreamcatcherWebPresidioPolicyControllerScan200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
