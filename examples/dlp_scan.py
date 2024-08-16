import asyncio
import os
from pprint import pprint

import dreamcatcher
from dreamcatcher.models.dreamcatcher_web_presidio_policy_controller_scan_request import DreamcatcherWebPresidioPolicyControllerScanRequest
from dreamcatcher.rest import ApiException

configuration = dreamcatcher.Configuration(
    host=os.environ.get("DREAMCATCHER_API_BASE", "https://dreamcatcher.blueteam.ai"),
    access_token=os.environ.get("BEARER_TOKEN")
)


# Enter a context with an instance of the API client
with dreamcatcher.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dreamcatcher.DlpZsnerPoliciesApi(api_client)
    endpoint_name = 'demo-endpoint' # str | Endpoint name
    id = 1 # int | DLP Policy ID

    try:
        # Get a DLP policy
        api_response = api_instance.dreamcatcher_web_zero_shot_ner_policy_controller_scan(
            endpoint_name, id,
            DreamcatcherWebPresidioPolicyControllerScanRequest(
                content="This is a test message. It contains a credit card number 4111 1111 1111 1111 and a social security number 123-45-6789."
            )
        )
        print("The response of DlpPoliciesApi->dreamcatcher_web_presidio_policy_controller_show:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DlpPoliciesApi->dreamcatcher_web_presidio_policy_controller_show: %s\n" % e)
