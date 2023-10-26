def handle_preflight(
    allowed_methods="POST, GET, PUT, PATCH, DELETE, OPTIONS",
    allowed_headers="Content-Type",
    max_age="3600",
):
    """Handles CORS preflight requests.
    Args:
        allowed_methods (str): Comma separated list of allowed HTTP methods.
        allowed_headers (str): Comma separated list of allowed HTTP headers.
        max_age (str): Maximum number of seconds the client/browser should cache
            the preflight response.
    Returns:
        A set of values that can be turned into a Response object using
        `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response
    """
    headers = {
        "Access-Control-Allow-Methods": allowed_methods,
        "Access-Control-Allow-Headers": allowed_headers,
        "Access-Control-Max-Age": max_age,
    }

    return "", 204, headers
