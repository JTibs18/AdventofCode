# Part 1 Solution
f1 = open("day16.txt")

energized = set()
visitedCount = dict()
grid = []
start = (0, 0)
queue = [] 

for line in f1:
    grid.append(list(line.strip()))  

if grid[start[1]][start[0]] == ".":
    queue.append((start, "R"))
elif grid[start[1]][start[0]] == "/": 
    direction = "U"
    queue.append((start, direction))
elif grid[start[1]][start[0]] == "\\": 
    direction = "D"
    queue.append((start, direction))
elif grid[start[1]][start[0]] == "-":
    queue.append((start, "R"))
elif grid[start[1]][start[0]] == "|":
        queue.append((start, "D"))
        queue.append((start, "U"))

while queue:
    curLocation, direction = queue.pop(0)
    
    if curLocation in visitedCount:
        visitedCount[curLocation] += 1
    else:
        visitedCount[curLocation] = 1 
        energized.add(curLocation)

    if visitedCount[curLocation] > 5:
        continue

    if direction == "R" and curLocation[0] + 1 < len(grid[0]):
        nextLocation = (curLocation[0] + 1, curLocation[1])
    elif direction == "U" and curLocation[1] - 1 >= 0:
        nextLocation = (curLocation[0], curLocation[1] - 1)
    elif direction == "L" and curLocation[0] - 1 >= 0:
        nextLocation = (curLocation[0] - 1, curLocation[1])
    elif direction == "D" and curLocation[1] + 1 < len(grid):
        nextLocation = (curLocation[0], curLocation[1] + 1)
    else:
        continue 

    if grid[nextLocation[1]][nextLocation[0]] == "." or ((direction == "L" or direction == "R") and grid[nextLocation[1]][nextLocation[0]] == "-") or ((direction == "U" or direction == "D") and grid[nextLocation[1]][nextLocation[0]] == "|"):
        queue.append((nextLocation, direction))
    elif grid[nextLocation[1]][nextLocation[0]] == "/": 
        if direction == "R":
            direction = "U"
        elif direction == "L":
            direction = "D"
        elif direction == "U":
            direction = "R"
        else:
            direction = "L"
        queue.append((nextLocation, direction))
    elif grid[nextLocation[1]][nextLocation[0]] == "\\": 
        if direction == "R":
            direction = "D"
        elif direction == "L":
            direction = "U"
        elif direction == "U":
            direction = "L"
        else:
            direction = "R"
        queue.append((nextLocation, direction))
    elif (direction == "L" or direction == "R") and grid[nextLocation[1]][nextLocation[0]] == "|":
        queue.append((nextLocation, "D"))
        queue.append((nextLocation, "U"))
    else:
        queue.append((nextLocation, "L"))
        queue.append((nextLocation, "R"))

print(len(energized))

# Part 2 Solution (Takes about 20 seconds)
f1 = open("day16.txt")

grid = []
maxEnergized = 0 

for line in f1:
    grid.append(list(line.strip()))  

def determineDirection(coordinates, initialDirection):
    if grid[coordinates[1]][coordinates[0]] == "." or ((initialDirection == "L" or initialDirection == "R") and grid[coordinates[1]][coordinates[0]] == "-") or ((initialDirection == "U" or initialDirection == "D") and grid[coordinates[1]][coordinates[0]] == "|"):
        return [initialDirection]
    elif grid[coordinates[1]][coordinates[0]] == "/": 
        if initialDirection == "R":
            direction = "U"
        elif initialDirection == "L":
            direction = "D"
        elif initialDirection == "U":
            direction = "R"
        else:
            direction = "L"
        return [direction]
    elif grid[coordinates[1]][coordinates[0]] == "\\": 
        if initialDirection == "R":
            direction = "D"
        elif initialDirection == "L":
            direction = "U"
        elif initialDirection == "U":
            direction = "L"
        else:
            direction = "R"
        return [direction] 
    elif (initialDirection == "L" or initialDirection == "R") and grid[coordinates[1]][coordinates[0]] == "|":
        return ["U", "D"]
    else:
        return ["L", "R"]

def countTiles(startC, initialDirection):
    queue = []  
    energized = set()
    visitedCount = dict()

    for i in determineDirection(startC, initialDirection):
        queue.append((startC, i))

    while queue:
        curLocation, direction = queue.pop(0)
        
        if curLocation in visitedCount:
            visitedCount[curLocation] += 1
        else:
            visitedCount[curLocation] = 1 
            energized.add(curLocation)

        if visitedCount[curLocation] > 5:
            continue

        if direction == "R" and curLocation[0] + 1 < len(grid[0]):
            nextLocation = (curLocation[0] + 1, curLocation[1])
        elif direction == "U" and curLocation[1] - 1 >= 0:
            nextLocation = (curLocation[0], curLocation[1] - 1)
        elif direction == "L" and curLocation[0] - 1 >= 0:
            nextLocation = (curLocation[0] - 1, curLocation[1])
        elif direction == "D" and curLocation[1] + 1 < len(grid):
            nextLocation = (curLocation[0], curLocation[1] + 1)
        else:
            continue 

        for i in determineDirection(nextLocation, direction):
            queue.append((nextLocation, i))

    return len(energized)

for i in range(len(grid)):
    startLeft = (0, i)
    startRight = (len(grid[0]) - 1, i)
    energizedValues = []

    if i == 0:
        energizedValues.append(countTiles(startLeft, "D"))
        energizedValues.append(countTiles(startLeft, "R"))
        energizedValues.append(countTiles(startRight, "L"))
        energizedValues.append(countTiles(startRight, "D"))
    elif i == len(grid) - 1:
        energizedValues.append(countTiles(startLeft, "U"))
        energizedValues.append(countTiles(startLeft, "R"))
        energizedValues.append(countTiles(startRight, "L"))
        energizedValues.append(countTiles(startRight, "U"))
    else: 
        energizedValues.append(countTiles(startLeft, "R"))
        energizedValues.append(countTiles(startRight, "L"))

    if max(energizedValues) > maxEnergized:
        maxEnergized = max(energizedValues)

for i in range(len(grid[0])):
    startTop = (i, 0)
    startBottom = (i, len(grid) - 1)
    energizedValues = []

    if i == 0:
        energizedValues.append(countTiles(startTop, "D"))
        energizedValues.append(countTiles(startTop, "R"))
        energizedValues.append(countTiles(startBottom, "R"))
        energizedValues.append(countTiles(startBottom, "U"))
    elif i == len(grid[0]) - 1:
        energizedValues.append(countTiles(startTop, "D"))
        energizedValues.append(countTiles(startTop, "L"))
        energizedValues.append(countTiles(startBottom, "L"))
        energizedValues.append(countTiles(startBottom, "U"))
    else: 
        energizedValues.append(countTiles(startTop, "D"))
        energizedValues.append(countTiles(startBottom, "U"))

    if max(energizedValues) > maxEnergized:
        maxEnergized = max(energizedValues)

print(maxEnergized)
