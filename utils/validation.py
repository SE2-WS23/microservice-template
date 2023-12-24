def validate_query_params(request, expected_params):
    """
    Validates the query parameters of a request against the expected parameters.

    :param request: The Flask request object.
    :param expected_params: A dictionary where keys are the names of expected query parameters
                            and values are the expected types (e.g., str, int).
    :return: A tuple containing a boolean indicating if validation passed,
             and a message or None if validation failed.
    """
    for param, expected_type in expected_params.items():
        # Check if the parameter is in the request
        if param not in request.args:
            return False, f"Missing query parameter: {param}"

        # Validate the type of the parameter
        try:
            expected_type(request.args[param])
        except ValueError:
            return (
                False,
                f"Incorrect type for parameter: {param}. Expected {expected_type.__name__}",
            )

    return True, None
