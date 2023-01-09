# Part 1 Solution
from copy import deepcopy

f1 = open("day11.txt")

flashes = 0
steps = 100
control = True
grid = []
flashed = set() 

for line in f1:
    row = line.strip()
    grid.append([int(i) for i in list(row)])

newGrid = deepcopy(grid)

while steps: 
    flashed = set() 
    for indx, row in enumerate(grid): 
        for i, num in enumerate(row): 
            newGrid[indx][i] += 1  

    control = True 
    grid = deepcopy(newGrid)

    while control: 
        for indx, row in enumerate(newGrid): 
            for i, num in enumerate(row): 
                if newGrid[indx][i] > 9: 
                    newGrid[indx][i] = 0
                    flashes += 1 
                    flashed.add((indx, i))

                    if indx - 1 >= 0 and i - 1 >= 0 and (indx - 1, i -1) not in flashed: 
                        newGrid[indx -1][i - 1] += 1 
                    if i - 1 >= 0 and (indx, i -1) not in flashed: 
                        newGrid[indx][i - 1] += 1
                    if indx + 1 < len(grid) and i - 1 >= 0 and (indx + 1, i -1) not in flashed: 
                        newGrid[indx + 1][i - 1] += 1 
                    if indx - 1 >= 0 and (indx - 1, i) not in flashed: 
                        newGrid[indx - 1][i] += 1 
                    if indx - 1 >= 0 and i + 1 < len(row) and (indx - 1, i + 1) not in flashed: 
                        newGrid[indx - 1][i + 1] += 1 
                    if i + 1 < len(row) and (indx, i + 1) not in flashed:
                        newGrid[indx][i + 1] += 1 
                    if indx + 1 < len(grid) and i + 1 < len(row) and (indx + 1, i + 1) not in flashed: 
                        newGrid[indx + 1][i + 1] += 1 
                    if indx + 1 < len(grid) and (indx + 1, i) not in flashed: 
                        newGrid[indx + 1][i] += 1
            
            control = False 
            for row in newGrid: 
                for i in row: 
                    if i > 9: 
                        control = True 
                        break

            grid = deepcopy(newGrid)
    
    steps -= 1 

print(flashes)

# Part 2 Solution
f1 = open("day11.txt")

step = 0 
control = True
grid = []
flashed = set() 

for line in f1:
    row = line.strip()
    grid.append([int(i) for i in list(row)])

newGrid = deepcopy(grid)
totalOct = len(grid) * len(grid[0])

while True: 
    step += 1
    flashed = set() 
    for indx, row in enumerate(grid): 
        for i, num in enumerate(row): 
            newGrid[indx][i] += 1  

    control = True 
    grid = deepcopy(newGrid)

    while control: 
        for indx, row in enumerate(newGrid): 
            for i, num in enumerate(row): 
                if newGrid[indx][i] > 9: 
                    newGrid[indx][i] = 0
                    flashed.add((indx, i))

                    if indx - 1 >= 0 and i - 1 >= 0 and (indx - 1, i -1) not in flashed: 
                        newGrid[indx -1][i - 1] += 1 
                    if i - 1 >= 0 and (indx, i -1) not in flashed: 
                        newGrid[indx][i - 1] += 1
                    if indx + 1 < len(grid) and i - 1 >= 0 and (indx + 1, i -1) not in flashed: 
                        newGrid[indx + 1][i - 1] += 1 
                    if indx - 1 >= 0 and (indx - 1, i) not in flashed: 
                        newGrid[indx - 1][i] += 1 
                    if indx - 1 >= 0 and i + 1 < len(row) and (indx - 1, i + 1) not in flashed: 
                        newGrid[indx - 1][i + 1] += 1 
                    if i + 1 < len(row) and (indx, i + 1) not in flashed:
                        newGrid[indx][i + 1] += 1 
                    if indx + 1 < len(grid) and i + 1 < len(row) and (indx + 1, i + 1) not in flashed: 
                        newGrid[indx + 1][i + 1] += 1 
                    if indx + 1 < len(grid) and (indx + 1, i) not in flashed: 
                        newGrid[indx + 1][i] += 1
            
            control = False 
            for row in newGrid: 
                for i in row: 
                    if i > 9: 
                        control = True 
                        break

            grid = deepcopy(newGrid)
            
    if len(flashed) == totalOct: 
        break
    
print(step)