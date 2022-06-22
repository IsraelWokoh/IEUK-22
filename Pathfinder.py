def createGrid(
        rows = 10,
        columns = 10
):

    fullGrid = [[] for x in range(rows)]
    for x in range(rows * columns):
        fullGrid[x % rows].append([])

    return fullGrid


def display():
    for row in grid:
        print(row)
    print()


def insertObstacles(locationsXY):
    for point in locationsXY:
        grid[point[1]][point[0]] = obstacle


def withinGridBounds(next_position):
    return next_position[y_index] in range(rows) \
    and next_position[x_index] in range(columns)

def unobstructed(next_position):
    return grid[next_position[y_index]][next_position[x_index]] is not obstacle

def findPath(
        position=(0, 0),
        path = [],
        lastDirection = None,
        start=(0, 0),
        goal=(9, 9)
):

    backtrack = list(moveChoices).index

    for direction in [dir for dir in moveChoices.keys() if dir is not backtrack(lastDirection)]:
        if position is not goal: # Goal not reached
            if position is not move(position, direction): # if move is legal...
                position = move(position, direction) # ...make that move
                path.append(direction) # Add to current path
                findPath(position, path, direction) # Recurse
        else: # Goal reached
            solutions.append(path) # Add full path to list of solutions
            break

def backtrack(lastDirection): # Determines opposite direction
    return opposite[lastDirection]

def move(position, direction):
    next_position = [position[y_index + moveChoices[direction][y_index]],
                     position[x_index + moveChoices[direction][x_index]]]

    if withinGridBounds(next_position) and unobstructed(next_position): # If legal, do move
        position = next_position

    return position

if __name__ == '__main__':
    rows = 10
    columns = 10
    grid = createGrid(rows, columns)

    # Allowed moves to reach goal
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

    # To avoid backtracking on the next move (unless necessary)
    opposite = {
        'left': 'right',
        'up': 'down',
        'down-right': 'up-left',
        'down-left': 'up-right',
        'up-right': 'down-left',
        'up-left': 'down-right',
        'down': 'up',
        'right': 'left',
        None: None
    }

    # Preset obstacle locations
    locationsXY = (
        (9, 7),
        (8, 7),
        (6, 7),
        (6, 8)
    )

    obstacle = '✖'
    insertObstacles(locationsXY)

    playerIcon = '▣'

    # Start and Goal
    grid[0][0] = '○'
    grid[9][9] = '☆'



    # NOTE: [row][column] means [y][x]
    y_index = 0
    x_index = 1

    solutions = []
    findPath()
    if len(solutions) > 0:
        print(solutions)
    else:
        print('No paths found.')

