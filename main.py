from flask import escape

import functions_framework


@functions_framework.http
def http_function(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        A set of values that can be turned into a Response object using
        ‚`make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """

    # ToDo: Add your functionality

    # ToDo: Set header, status_code and response. You response can have any value
    # that can be turned into a Repsonse object using `make_reponse'.
    # See more https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response
    status_code = 200
    header = {}
    response = {}

    return response, status_code, header


# For testing purposes only!
# It is easier to develop your function without the need to restart your cloud function every time
# But keep in mind that this is not completely the same environment as in the cloud function environment
if __name__ == "__main__":
    # ToDo: Add your function here

    pass
