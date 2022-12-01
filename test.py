"""
# --------------------------- Testing --------------------------- #
    # Get cost matrix
    if request['billions_API'] == 1:
        cost_matrix = matrix.billions(request)
    else:
        cost_matrix = matrix.haversine(request)

    # Append cost matrix to request
    request['cost_matrix'] = cost_matrix
    # --------------------------------------------------------------- #

    responses = []
    for search_strategy in range(1, 2):
        request['search_parameters'] = search_strategy

        # get response for each search strategy
        response = get_main_depot_response(request)
        print(f'search strategy {search_strategy} status: {response["status"]}')
        if response['status'] == 200:
            responses.append(response)

    response = min(responses, key=lambda x: x['total_distance'])
"""
