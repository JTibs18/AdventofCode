#Part 1 Solution
import copy 
f1 = open("day18.txt")

grid = []
steps = 100
onLights = 0

for line in f1: 
    grid.append(list(line.strip()))

newGrid = copy.deepcopy(grid)

while steps: 
    for indxY, y in enumerate(grid): 
        for indxX, x in enumerate(y): 
            surroundingLightOn = 0

            if indxY > 0 and indxX > 0 and grid[indxY-1][indxX-1] == "#":
                surroundingLightOn += 1 
            if indxY + 1 < len(grid) and indxX + 1 < len(y) and grid[indxY+1][indxX+1] == "#":
                surroundingLightOn += 1 
            if indxX > 0 and indxY + 1 < len(grid) and grid[indxY+1][indxX-1] == "#": 
                surroundingLightOn += 1 
            if indxX + 1 < len(y) and indxY > 0 and grid[indxY-1][indxX+1] == "#": 
                surroundingLightOn += 1 
            if indxY > 0 and grid[indxY-1][indxX] == "#":
                surroundingLightOn += 1 
            if indxY + 1 < len(grid) and grid[indxY+1][indxX] == "#": 
                surroundingLightOn += 1 
            if indxX + 1 < len(y) and grid[indxY][indxX+1] == "#": 
                surroundingLightOn += 1 
            if indxX > 0 and grid[indxY][indxX-1] == "#": 
                surroundingLightOn += 1 

            if (x == "#" and (surroundingLightOn == 2 or surroundingLightOn == 3)) or (x == "." and surroundingLightOn == 3): 
                newGrid[indxY][indxX] = "#" 
            else: 
                newGrid[indxY][indxX] = "."
            
    grid = copy.deepcopy(newGrid)
    steps -= 1 

for x in grid: 
    for y in x: 
        if y == "#":
            onLights += 1

print(onLights)

#Part 2 Solution
import copy 
f1 = open("day18.txt")

grid = []
steps = 100
onLights = 0
alwaysOn = ((0, 0), (0, steps - 1), (steps - 1, 0), (steps - 1, steps -1))

for line in f1: 
    grid.append(list(line.strip()))

grid[0][0] = "#"
grid[0][steps-1] = "#"
grid[steps-1][0] = "#"
grid[steps-1][steps-1] = "#"
newGrid = copy.deepcopy(grid)

while steps: 
    for indxY, y in enumerate(grid): 
        for indxX, x in enumerate(y): 
            surroundingLightOn = 0

            if indxY > 0 and indxX > 0 and grid[indxY-1][indxX-1] == "#":
                surroundingLightOn += 1 
            if indxY + 1 < len(grid) and indxX + 1 < len(y) and grid[indxY+1][indxX+1] == "#":
                surroundingLightOn += 1 
            if indxX > 0 and indxY + 1 < len(grid) and grid[indxY+1][indxX-1] == "#": 
                surroundingLightOn += 1 
            if indxX + 1 < len(y) and indxY > 0 and grid[indxY-1][indxX+1] == "#": 
                surroundingLightOn += 1 
            if indxY > 0 and grid[indxY-1][indxX] == "#":
                surroundingLightOn += 1 
            if indxY + 1 < len(grid) and grid[indxY+1][indxX] == "#": 
                surroundingLightOn += 1 
            if indxX + 1 < len(y) and grid[indxY][indxX+1] == "#": 
                surroundingLightOn += 1 
            if indxX > 0 and grid[indxY][indxX-1] == "#": 
                surroundingLightOn += 1 

            if (x == "#" and (surroundingLightOn == 2 or surroundingLightOn == 3)) or (x == "." and surroundingLightOn == 3) or (indxY, indxX) in alwaysOn: 
                newGrid[indxY][indxX] = "#" 
            else: 
                newGrid[indxY][indxX] = "."
            
    grid = copy.deepcopy(newGrid)
    steps -= 1 

for x in grid: 
    for y in x: 
        if y == "#":
            onLights += 1

print(onLights)