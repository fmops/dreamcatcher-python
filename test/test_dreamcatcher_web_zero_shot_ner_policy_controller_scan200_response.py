# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.dreamcatcher_web_zero_shot_ner_policy_controller_scan200_response import DreamcatcherWebZeroShotNERPolicyControllerScan200Response

class TestDreamcatcherWebZeroShotNERPolicyControllerScan200Response(unittest.TestCase):
    """DreamcatcherWebZeroShotNERPolicyControllerScan200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DreamcatcherWebZeroShotNERPolicyControllerScan200Response:
        """Test DreamcatcherWebZeroShotNERPolicyControllerScan200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DreamcatcherWebZeroShotNERPolicyControllerScan200Response`
        """
        model = DreamcatcherWebZeroShotNERPolicyControllerScan200Response()
        if include_optional:
            return DreamcatcherWebZeroShotNERPolicyControllerScan200Response(
                violates_policy = True
            )
        else:
            return DreamcatcherWebZeroShotNERPolicyControllerScan200Response(
        )
        """

    def testDreamcatcherWebZeroShotNERPolicyControllerScan200Response(self):
        """Test DreamcatcherWebZeroShotNERPolicyControllerScan200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
