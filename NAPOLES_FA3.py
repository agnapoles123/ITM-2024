#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def relationship_status(from_member, to_member, social_graph):
    if to_member in social_graph[from_member]["following"] and from_member in social_graph[to_member]["following"]:
        return "friends"
    elif from_member in social_graph[to_member]["following"]:
        return "followed by"
    elif to_member in social_graph[from_member]["following"]:
        return "follower"
    else:
        return "no relationship"

def tic_tac_toe(board):
    ## alternative to the all fuction since I wasn't sure if we can use it HAHAH 
    def evaluate(line):
        counter = 0
        for x in line:
            if x == line[0] and line[0] != '':
                counter+=1
            if counter == len(board):
                return True
        return False

    for rows in board:
        if evaluate(rows):
            return rows[0]
        for columns in range(0,len(board)):
            col = list(map(lambda x: x[columns],board))
            if evaluate(col):
                return col[0]
    decline_diagonal = list(map(lambda x: board[x][x], range(0,len(board))))
    incline_diagonal = list(map(lambda x: board[x][len(board)-1-x], range(0,len(board))))
    if evaluate (decline_diagonal):
        return decline_diagonal[0]
    elif evaluate (incline_diagonal):
        return incline_diagonal[0]
    else:
        return 'NO WINNER'


def eta(first_stop, second_stop, route_map):
    eta = 0
    current_loc = first_stop
    while second_stop != current_loc:
        for origin, destination in route_map.keys():
            if origin == current_loc:
                eta += route_map[origin,destination]['travel_time_mins']
                current_loc = destination
                break
            else:
                continue
    return eta

