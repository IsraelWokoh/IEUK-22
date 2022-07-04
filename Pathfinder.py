# Amazon Coding Exercise
# Written by Israel Wokoh
# Developed in Python 3.11.0b3, June 2022


def createGrid( # Creates grid
        rows = 10,
        columns = 10
):

    # Ran into weird assignment issues before, chose this method
    fullGrid = [[] for x in range(rows)]
    for x in range(rows * columns):
        fullGrid[x % rows].append([])

    return fullGrid


def displayGrid(): # Displays grid
    for row in grid:
        print(row)
    print()


def insertObstacles(locationsXY): # Inserts obstacles at predetermined locations
    for point in locationsXY:
        grid[point[1]][point[0]] = obstacle


def withinGridBounds(next_position): # Checks if out of bounds
    return next_position[y_index] in range(rows) \
    and next_position[x_index] in range(columns)


def unobstructed(next_position): # Checks if obstacle in the way
    return grid[next_position[y_index]][next_position[x_index]] is not obstacle


def findPath( # Depth-first search - EXTREMELY SLOW
        position=(0, 0),
        path = [(0,0)],
        step = 1,
        start=(0, 0),
        goal=(9, 9)
):

    for direction in moveChoices.keys(): # iterate over directions

        newPosition = move(position, direction)

        if newPosition not in path: # If position unvisited...
            newPath = path + [newPosition]
            if newPosition == goal: # if goal reached
                if newPath not in solutions: # if NEW solution
                    if solutions != []: # if NOT FIRST
                        if len(newPath) < len(solutions[-1]): # if SHORTER
                            solutions.remove(solutions[0]) # out with old...
                            solutions.append(newPath) # ...in with new - clumsy for 1-element list. WILL CHANGE!
                            print(f'{len(solutions[0])}-step solution found') # For testing
                    else: # if first
                        solutions.append(newPath) # append it
                break # don't go any further down this path

            else: # if goal NOT reached
                findPath(newPosition, newPath, step+1) # recurse


def move(position, direction): # Changes position
    next_position = (position[y_index] + moveChoices[direction][y_index],
                     position[x_index] + moveChoices[direction][x_index]) # Calculate new position

    if withinGridBounds(next_position) and unobstructed(next_position): # If legal...
        position = next_position # do move

    return position


if __name__ == '__main__':
    rows = 10
    columns = 10
    grid = createGrid(rows, columns)

    # Allowed moves: vector
    moveChoices = {
        'left': (0, -1),
        'up': (-1, 0),
        'down-right': (1, 1),
        'down-left': (1, -1),
        'up-right': (-1, 1),
        'up-left': (-1, -1),
        'down': (1, 0),
        'right': (0, 1)
    }

    # Preset obstacle locations
    obstacle = '✖' # Obstacle icon
    locationsXY = (
        (9, 7),
        (8, 7),
        (6, 7),
        (6, 8)
    )

    insertObstacles(locationsXY) # Places obstacles

    playerIcon = '▣'

    # Start and Goal
    grid[0][0] = '○'
    grid[9][9] = '☆'

    # NOTE: [row][column] means [y][x]
    y_index = 0
    x_index = 1

    solutions = [] # List of solutions - at most one element (will change)
    findPath() # Calls pathfinding function

    if len(solutions) != 0: # Never make it here because I'm too slow.
        print(solutions)
    else:
        print('No paths found.')
