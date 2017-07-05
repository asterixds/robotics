# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid,goal,cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    
    # make sure your function returns a grid of values as 
    # demonstrated in the previous video.

    values = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    
    x = goal[0]
    y = goal[1]
    g = 0
    grid[x][y] = 1
    values[x][y] = 0
    
    open = [[g, x, y]]

    while(len(open)>0):   #while queue is not empty
        current=open.sort()
        current=open.reverse()
        current=open.pop()
        
        #visit  neighbors and put in queue if the grid are not opened or blocked 
        for d in delta:
            step_r = current[1]-d[0]  
            step_c = current[2] - d[1] 
            if step_r>=0 and step_c>=0 and step_r<len(grid) and step_c<len(grid[0]):
                if  grid[step_r][step_c]==0 and values[step_r][step_c]==99:
                    g = current[0]+cost
                    open.append([g, step_r,step_c])
                    grid[step_r][step_c] = 1
                    values[step_r][step_c] = g
    return values

values = compute_value(grid,goal,cost)

for line in values:
    print line