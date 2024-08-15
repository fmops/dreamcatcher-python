# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from dreamcatcher.models.chat_completion_response import ChatCompletionResponse  # noqa: E501

class TestChatCompletionResponse(unittest.TestCase):
    """ChatCompletionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChatCompletionResponse:
        """Test ChatCompletionResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChatCompletionResponse`
        """
        model = ChatCompletionResponse()  # noqa: E501
        if include_optional:
            return ChatCompletionResponse(
                choices = [
                    dreamcatcher.models.chat_completion_response_choices_inner.Chat_completion_response_choices_inner(
                        message = dreamcatcher.models.chat_completion_message.Chat completion message(
                            content = '', 
                            role = '', ), )
                    ],
                id = '',
                model = ''
            )
        else:
            return ChatCompletionResponse(
        )
        """

    def testChatCompletionResponse(self):
        """Test ChatCompletionResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
