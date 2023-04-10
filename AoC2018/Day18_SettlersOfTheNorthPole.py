#Part 1 Solution
f1 = open("day18.txt")

grid = dict() 
rowNum = 0
minutes = 0 
greatestLength = 50

for line in f1:
    row = line.strip()

    for column, val in enumerate(row): 
        grid[(column,rowNum)] = val 
    
    rowNum += 1 

while minutes < 10: 
    minutes += 1 
    newGrid = dict() 

    for key, value in grid.items(): 
        adjacentCount = 0 

        if value == ".": 
            if key[0] - 1 >= 0 and key[1] - 1 >= 0 and grid[(key[0] - 1, key[1] - 1)] == "|": 
                adjacentCount += 1 
            if key[1] - 1 >= 0 and grid[(key[0], key[1] - 1)] == "|": 
                adjacentCount += 1 
            if key[0] + 1 < greatestLength and key[1] - 1 >= 0 and grid[(key[0] + 1, key[1] - 1)] == "|": 
                adjacentCount += 1 
            if key[0] - 1 >= 0 and grid[(key[0] - 1, key[1])] == "|":
                adjacentCount += 1 
            if key[0] + 1 < greatestLength and grid[(key[0] + 1, key[1])] == "|":
                adjacentCount += 1 
            if key[0] - 1 >= 0 and key[1] + 1 < greatestLength and grid[(key[0] - 1, key[1] + 1)] == "|": 
                adjacentCount += 1 
            if key[1] + 1 < greatestLength and grid[(key[0], key[1] + 1)] == "|": 
                adjacentCount += 1 
            if key[0] + 1 < greatestLength and key[1] + 1 < greatestLength and grid[(key[0] + 1, key[1] + 1)] == "|": 
                adjacentCount += 1 
            
            if adjacentCount >= 3: 
                newGrid[key] = "|"
            else: 
                newGrid[key] = "."

        elif value == "|": 
            if key[0] - 1 >= 0 and key[1] - 1 >= 0 and grid[(key[0] - 1, key[1] - 1)] == "#": 
                adjacentCount += 1 
            if key[1] - 1 >= 0 and grid[(key[0], key[1] - 1)] == "#": 
                adjacentCount += 1 
            if key[0] + 1 < greatestLength and key[1] - 1 >= 0 and grid[(key[0] + 1, key[1] - 1)] == "#": 
                adjacentCount += 1 
            if key[0] - 1 >= 0 and grid[(key[0] - 1, key[1])] == "#":
                adjacentCount += 1 
            if key[0] + 1 < greatestLength and grid[(key[0] + 1, key[1])] == "#":
                adjacentCount += 1 
            if key[0] - 1 >= 0 and key[1] + 1 < greatestLength and grid[(key[0] - 1, key[1] + 1)] == "#": 
                adjacentCount += 1 
            if key[1] + 1 < greatestLength and grid[(key[0], key[1] + 1)] == "#": 
                adjacentCount += 1 
            if key[0] + 1 < greatestLength and key[1] + 1 < greatestLength and grid[(key[0] + 1, key[1] + 1)] == "#": 
                adjacentCount += 1 
            
            if adjacentCount >= 3: 
                newGrid[key] = "#"
            else: 
                newGrid[key] = "|"

        else: 
            adjacencyList = [] 

            if key[0] - 1 >= 0 and key[1] - 1 >= 0: 
                adjacencyList.append(grid[(key[0] - 1, key[1] - 1)]) 
            if key[1] - 1 >= 0: 
                adjacencyList.append(grid[(key[0], key[1] - 1)]) 
            if key[0] + 1 < greatestLength and key[1] - 1 >= 0: 
                adjacencyList.append(grid[(key[0] + 1, key[1] - 1)]) 
            if key[0] - 1 >= 0:
                adjacencyList.append(grid[(key[0] - 1, key[1])]) 
            if key[0] + 1 < greatestLength:
                adjacencyList.append(grid[(key[0] + 1, key[1])]) 
            if key[0] - 1 >= 0 and key[1] + 1 < greatestLength: 
                adjacencyList.append(grid[(key[0] - 1, key[1] + 1)]) 
            if key[1] + 1 < greatestLength: 
                adjacencyList.append(grid[(key[0], key[1] + 1)]) 
            if key[0] + 1 < greatestLength and key[1] + 1 < greatestLength: 
                adjacencyList.append(grid[(key[0] + 1, key[1] + 1)]) 
            
            if "#" in adjacencyList and "|" in adjacencyList: 
                newGrid[key] = "#"
            else: 
                newGrid[key] = "."
        
    grid = newGrid

woodedAcres = 0 
lumberyards = 0 

for x in range(greatestLength):
    for y in range(greatestLength):
        if grid[(x, y)] == "|":
            woodedAcres += 1
        elif grid[(x, y)] == "#":
            lumberyards += 1 

print(lumberyards * woodedAcres)

#Part 2 Solution # Takes a few seconds to run
f1 = open("day18.txt")

grid = dict() 
rowNum = 0
minutes = 0 
greatestLength = 50
gridRepeatStarts = 0 
visitedGrids = []
repeatedGrids = []

for line in f1:
    row = line.strip()
    
    for column, val in enumerate(row): 
        grid[(column,rowNum)] = val 
    
    rowNum += 1 

while minutes < 1000000000: 
    minutes += 1 
    newGrid = dict() 

    for key, value in grid.items(): 
        adjacentCount = 0 

        if value == ".": 
            if key[0] - 1 >= 0 and key[1] - 1 >= 0 and grid[(key[0] - 1, key[1] - 1)] == "|": 
                adjacentCount += 1 
            if key[1] - 1 >= 0 and grid[(key[0], key[1] - 1)] == "|": 
                adjacentCount += 1 
            if key[0] + 1 < greatestLength and key[1] - 1 >= 0 and grid[(key[0] + 1, key[1] - 1)] == "|": 
                adjacentCount += 1 
            if key[0] - 1 >= 0 and grid[(key[0] - 1, key[1])] == "|":
                adjacentCount += 1 
            if key[0] + 1 < greatestLength and grid[(key[0] + 1, key[1])] == "|":
                adjacentCount += 1 
            if key[0] - 1 >= 0 and key[1] + 1 < greatestLength and grid[(key[0] - 1, key[1] + 1)] == "|": 
                adjacentCount += 1 
            if key[1] + 1 < greatestLength and grid[(key[0], key[1] + 1)] == "|": 
                adjacentCount += 1 
            if key[0] + 1 < greatestLength and key[1] + 1 < greatestLength and grid[(key[0] + 1, key[1] + 1)] == "|": 
                adjacentCount += 1 
            
            if adjacentCount >= 3: 
                newGrid[key] = "|"
            else: 
                newGrid[key] = "."

        elif value == "|": 
            if key[0] - 1 >= 0 and key[1] - 1 >= 0 and grid[(key[0] - 1, key[1] - 1)] == "#": 
                adjacentCount += 1 
            if key[1] - 1 >= 0 and grid[(key[0], key[1] - 1)] == "#": 
                adjacentCount += 1 
            if key[0] + 1 < greatestLength and key[1] - 1 >= 0 and grid[(key[0] + 1, key[1] - 1)] == "#": 
                adjacentCount += 1 
            if key[0] - 1 >= 0 and grid[(key[0] - 1, key[1])] == "#":
                adjacentCount += 1 
            if key[0] + 1 < greatestLength and grid[(key[0] + 1, key[1])] == "#":
                adjacentCount += 1 
            if key[0] - 1 >= 0 and key[1] + 1 < greatestLength and grid[(key[0] - 1, key[1] + 1)] == "#": 
                adjacentCount += 1 
            if key[1] + 1 < greatestLength and grid[(key[0], key[1] + 1)] == "#": 
                adjacentCount += 1 
            if key[0] + 1 < greatestLength and key[1] + 1 < greatestLength and grid[(key[0] + 1, key[1] + 1)] == "#": 
                adjacentCount += 1 
            
            if adjacentCount >= 3: 
                newGrid[key] = "#"
            else: 
                newGrid[key] = "|"

        else: 
            adjacencyList = [] 

            if key[0] - 1 >= 0 and key[1] - 1 >= 0: 
                adjacencyList.append(grid[(key[0] - 1, key[1] - 1)]) 
            if key[1] - 1 >= 0: 
                adjacencyList.append(grid[(key[0], key[1] - 1)]) 
            if key[0] + 1 < greatestLength and key[1] - 1 >= 0: 
                adjacencyList.append(grid[(key[0] + 1, key[1] - 1)]) 
            if key[0] - 1 >= 0:
                adjacencyList.append(grid[(key[0] - 1, key[1])]) 
            if key[0] + 1 < greatestLength:
                adjacencyList.append(grid[(key[0] + 1, key[1])]) 
            if key[0] - 1 >= 0 and key[1] + 1 < greatestLength: 
                adjacencyList.append(grid[(key[0] - 1, key[1] + 1)]) 
            if key[1] + 1 < greatestLength: 
                adjacencyList.append(grid[(key[0], key[1] + 1)]) 
            if key[0] + 1 < greatestLength and key[1] + 1 < greatestLength: 
                adjacencyList.append(grid[(key[0] + 1, key[1] + 1)]) 
            
            if "#" in adjacencyList and "|" in adjacencyList: 
                newGrid[key] = "#"
            else: 
                newGrid[key] = "."
        
    grid = newGrid

    if newGrid in repeatedGrids: 
        break 
    elif newGrid in visitedGrids:
        repeatedGrids.append(newGrid)
        gridRepeatStarts = minutes 
    
    visitedGrids.append(newGrid) 

adjust = (1000000000 - gridRepeatStarts) % len(repeatedGrids) 

grid = repeatedGrids[adjust - 1]

woodedAcres = 0 
lumberyards = 0 

for x in range(greatestLength):
    for y in range(greatestLength):
        if grid[(x, y)] == "|":
            woodedAcres += 1
        elif grid[(x, y)] == "#":
            lumberyards += 1 

print(lumberyards * woodedAcres)
