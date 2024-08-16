"""
This example demonstrates how to use the Dreamcatcher API to interact with Endpoints.
Specifically, in this example we list all available endpoints, select one by name, and
then invoke it with example data to demonstrate the policy engine in action.
"""
import asyncio
import os
from pprint import pprint

import dreamcatcher
from dreamcatcher.rest import ApiException

configuration = dreamcatcher.Configuration(
    host=os.environ.get("DREAMCATCHER_API_BASE", "https://dreamcatcher.blueteam.ai"),
    access_token=os.environ.get("BEARER_TOKEN")
)


# Enter a context with an instance of the API client
with dreamcatcher.ApiClient(configuration) as api_client:

    # Create an instance of the API class
    api_instance = dreamcatcher.EndpointsApi(api_client)
    api_response = None

    try:
        # List endpoints
        api_response = api_instance.dreamcatcher_web_endpoint_controller_index()
        print("The response of EndpointsApi->dreamcatcher_web_endpoint_controller_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->dreamcatcher_web_endpoint_controller_index: %s\n" % e)

    endpoint_name = 'demo-endpoint' # str | Endpoint name
    try:
        # Get an endpoint
        api_response = api_instance.dreamcatcher_web_endpoint_controller_show(endpoint_name)
        print("The response of EndpointsApi->dreamcatcher_web_endpoint_controller_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->dreamcatcher_web_endpoint_controller_show: %s\n" % e)

    create_chat_completion = dreamcatcher.CreateChatCompletion(
        model="foo",
        messages=[{"role": "user", "content": "Hello, world!"}]
    )
    try:
        # Invoke a chat completion
        api_response = api_instance.dreamcatcher_web_endpoint_controller_invoke_chat_completions(endpoint_name, create_chat_completion=create_chat_completion)
        print("The response of EndpointsApi->dreamcatcher_web_endpoint_controller_invoke_chat_completions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->dreamcatcher_web_endpoint_controller_invoke_chat_completions: %s\n" % e)
