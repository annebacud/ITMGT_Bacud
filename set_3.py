def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    from_follows=to_member in social_graph.get(from_member, {}).get('following', [])
    to_follows=from_member in social_graph.get(to_member, {}).get('following', [])

    
    if from_follows and to_follows:
        return "friends"
    elif from_follows:
        return "follower"
    elif to_follows:
        return "followed by"
    else:
        return "no relationship"

def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    rows=len(board)
    columns=len(board[0])

    for row in board:
        if row[0]!='' and all(symbol==row[0] for symbol in row):
            return row[0]

    for col in range(columns):
        if board[0][col] !='' and all(board[row][col]==board[0][col] for row in range(rows)):
            return board[0][col]
        
    #from top left to bottom right ex. [0,0], [1,1], [2,2], etc.
    if board[0][0] !='' and all(board[i][i] == board[0][0] for i in range(rows)):
        return board[0][0]

    #from bottom left to top right i=0, [0,3], i=1, [1,2], i=2, [2, 1], i=3, [3, 0] (tested with 4x4)
    if board[0][rows-1]!='' and all(board[i][rows - 1 - i] == board[0][rows-1] for i in range(rows)):
        return board[0][rows-1]

    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    def travel_time(origin, destination, legs):
        key=(origin, destination)
        if key in legs:
            return legs[key]["travel_time_mins"]
        else:
            return None

    direct_travel=travel_time(first_stop, second_stop, route_map)
    if direct_travel is not None:
        return direct_travel

    total_travel_time=0
    current_stop=first_stop
    visited_stops=set()

    while current_stop != second_stop:
        next_leg_found=False
        for(origin, destination), travel_data in route_map.items():
            if origin == current_stop and destination not in visited_stops:
                total_travel_time += travel_data["travel_time_mins"]
                current_stop = destination
                visited_stops.add(destination)
                next_leg_found=True
                break
        if not next_leg_found:
            return None 

    return total_travel_time
