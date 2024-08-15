import os
import time
import dreamcatcher
from dreamcatcher.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:4000
# See configuration.py for a list of all supported configuration parameters.
configuration = dreamcatcher.Configuration(
    host = "http://localhost:4000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authorization
configuration = dreamcatcher.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

from dreamcatcher.models.dreamcatcher_web_zero_shot_ner_policy_controller_scan_request import DreamcatcherWebZeroShotNERPolicyControllerScanRequest

async def main():
# Enter a context with an instance of the API client
    async with dreamcatcher.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = dreamcatcher.DlpZsnerPoliciesApi(api_client)
        endpoint_name = 'demo-endpoint' # str | Endpoint name
        id = 1 # int | DLP Policy ID

        try:
            # Get a DLP policy
            api_response = await api_instance.dreamcatcher_web_zero_shot_ner_policy_controller_scan(
                endpoint_name, id,
                DreamcatcherWebZeroShotNERPolicyControllerScanRequest(
                    content="This is a test message. It contains a credit card number 4111 1111 1111 1111 and a social security number 123-45-6789. I like fords."
                )
            )
            print("The response of DlpPoliciesApi->dreamcatcher_web_presidio_policy_controller_show:\n")
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling DlpPoliciesApi->dreamcatcher_web_presidio_policy_controller_show: %s\n" % e)


import asyncio
asyncio.run(main())
