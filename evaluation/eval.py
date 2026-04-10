def evaluate_response(response, expected):
    return {
        "match": expected.lower() in response.lower()
    }
