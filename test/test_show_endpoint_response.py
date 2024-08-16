# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from dreamcatcher.models.show_endpoint_response import ShowEndpointResponse  # noqa: E501

class TestShowEndpointResponse(unittest.TestCase):
    """ShowEndpointResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ShowEndpointResponse:
        """Test ShowEndpointResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ShowEndpointResponse`
        """
        model = ShowEndpointResponse()  # noqa: E501
        if include_optional:
            return ShowEndpointResponse(
                content_moderation_policies = dreamcatcher.models.content_moderation_policy.ContentModerationPolicy(
                    active = True, 
                    blocked_content_types = [
                        'toxic'
                        ], 
                    name = '', 
                    score_threshold = 1.337, ),
                dlp_policies = dreamcatcher.models.dlp_policy.DlpPolicy(
                    active = True, 
                    anonymizer = dreamcatcher.models.dlp_policy_anonymizer.DlpPolicy_anonymizer(
                        type = 'replace', ), 
                    entities = [
                        'MEDICAL_LICENSE'
                        ], 
                    name = '', 
                    response = 'block', 
                    score_threshold = 1.337, ),
                dlp_zsner_policies = dreamcatcher.models.dlp_zsner_policy.DlpZsnerPolicy(
                    active = True, 
                    anonymizer = dreamcatcher.models.dlp_policy_anonymizer.DlpPolicy_anonymizer(
                        type = 'replace', ), 
                    entities = [
                        dreamcatcher.models.dlp_zsner_policy_entities_inner.DlpZsnerPolicy_entities_inner(
                            entity = '', )
                        ], 
                    name = '', 
                    response = 'block', 
                    score_threshold = 1.337, ),
                name = ''
            )
        else:
            return ShowEndpointResponse(
        )
        """

    def testShowEndpointResponse(self):
        """Test ShowEndpointResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
