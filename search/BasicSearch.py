# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    open = []
    #push origin into path queue
    open.append([0,init[0],init[1]])
    while(len(open)>0):   #while queue is not empty
        current=open.pop()
        if current[1] == goal[0] and current[2] == goal[1]: #have we reached the goal?
            return current

        #visit  neighbors and put in queue if the grid are not opened or blocked 
        for d in delta:
            step_r = current[1]+d[0]  
            step_c = current[2] + d[1] 
            if step_r>=0 and step_c>=0 and step_r<len(grid) and step_c<len(grid[0]) and grid[step_r][step_c]==0:
                open.append([current[0]+1, step_r,step_c])
                grid[step_r][step_c] = 1  #block the cell off
    return -1 #failed to reach goal

print search(grid,init,goal,cost)



