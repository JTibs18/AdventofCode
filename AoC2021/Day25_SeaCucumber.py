# Part 1 Solution
from copy import deepcopy

f1 = open("day25.txt")

grid = []
cucumbersMoved = 0 
steps = 0

for line in f1:
    row = line.strip()
    grid.append(list(row))

newGrid = deepcopy(grid)

while True: 
    steps += 1 
    cucumbersMoved = 0 
    grid = deepcopy(newGrid) 
    for i, row in enumerate(grid): 
        ptr1 = 0 
        ptr2 = 1
        for indx, val in enumerate(row): 
            if row[ptr1] == ">" and row[ptr2] == ".": 
                newGrid[i][ptr1] = "."
                newGrid[i][ptr2] = ">"
                cucumbersMoved += 1 

            ptr1 += 1
            if ptr1 == len(row) - 1: 
                ptr2 = 0
            else: 
                ptr2 += 1
    
    grid = deepcopy(newGrid)

    for i, row in enumerate(grid): 
        ptr2 = i + 1

        if ptr2 == len(grid):
            ptr2 = 0 

        for indx, val in enumerate(row): 
            if val == "v" and grid[ptr2][indx] == ".": 
                newGrid[i][indx] = "."
                newGrid[ptr2][indx] = "v"
                cucumbersMoved += 1 
            
    if cucumbersMoved == 0:
        break

print(steps)

# Part 2 Solution
from copy import deepcopy

f1 = open("day25.txt")

grid = []
cucumbersMoved = 0 
steps = 0

for line in f1:
    row = line.strip()
    grid.append(list(row))

newGrid = deepcopy(grid)

while True: 
    steps += 1 
    cucumbersMoved = 0 
    grid = deepcopy(newGrid) 
    for i, row in enumerate(grid): 
        ptr1 = 0 
        ptr2 = 1
        for indx, val in enumerate(row): 
            if row[ptr1] == ">" and row[ptr2] == ".": 
                newGrid[i][ptr1] = "."
                newGrid[i][ptr2] = ">"
                cucumbersMoved += 1 

            ptr1 += 1
            if ptr1 == len(row) - 1: 
                ptr2 = 0
            else: 
                ptr2 += 1
    
    grid = deepcopy(newGrid)

    for i, row in enumerate(grid): 
        ptr2 = i + 1

        if ptr2 == len(grid):
            ptr2 = 0 

        for indx, val in enumerate(row): 
            if val == "v" and grid[ptr2][indx] == ".": 
                newGrid[i][indx] = "."
                newGrid[ptr2][indx] = "v"
                cucumbersMoved += 1 
            
    if cucumbersMoved == 0:
        break

print(steps)