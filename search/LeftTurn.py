# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's 
# optimal path to the position specified in goal; 
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a 
# right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right
                
goal = [2, 0] # given in the form [row,col]

cost = [2, 1, 20] # cost has 3 values, corresponding to making 
                  # a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D(grid,init,goal,cost):
    value = [[[999 for f in range(len(forward))]\
        for c in range(len(grid[0]))]\
        for r in range(len(grid))]
    policy = [[[' ' for f in range(len(forward))]\
        for c in range(len(grid[0]))]\
        for r in range(len(grid))]
        
    change = True

    while change:
        change = False

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                for f in range(len(forward)):
                    if goal[0] == x and goal[1] == y:
                        if value[x][y][f] > 0:
                            value[x][y][f] = 0
                            policy[x][y][f] = "*"
                            change = True
                    elif grid[x][y] == 0:
                        for a in range(len(action)):
                            f2 = (f + action[a]) % len(forward)
                            x2 = x + forward[f2][0]
                            y2 = y + forward[f2][1]
                            if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                                v2 = value[x2][y2][f2] + cost[a]
                                if v2 < value[x][y][f]:
                                    value[x][y][f] = v2
                                    policy[x][y][f] = action_name[a]
                                    change = True

    opolicy = [[" " for row in range(len(grid[0]))] for col in range(len(grid))]
    x = init[0]
    y = init[1]
    f = init[2]

    opolicy[x][y] = policy[x][y][f]

    while policy[x][y][f] != '*':
        if policy[x][y][f] == 'R':
            f = (f - 1) % len(forward)
        elif policy[x][y][f] == 'L':
            f = (f + 1) % len(forward)
        x += forward[f][0]
        y += forward[f][1]
        opolicy[x][y] = policy[x][y][f]

    
    return policy


value = optimum_policy2D (grid,init,goal,cost)

for line in value:
    print line