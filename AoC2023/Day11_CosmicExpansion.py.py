import itertools

#Part 1 Solution (Naive approach, adding new lines to grid)
f1 = open("day11.txt")

sumOfShortestPath = 0 
foundColumn = set()
newGrid = []
galaxy = []

for y, line in enumerate(f1):
    line = list(line.strip())
    doubleLine = True 

    for x, val in enumerate(line): 
        if val == "#": 
            foundColumn.add(x)
            doubleLine = False 
    
    newGrid.append(line)
    if doubleLine == True:
        newGrid.append(line)

for x in range(len(newGrid[0]), 0, -1):
    if x not in foundColumn:
        for y in range(len(newGrid)):
            newGrid[y] = newGrid[y][:x + 1] + ["."] + newGrid[y][x + 1:]

for y, row in enumerate(newGrid):
    for x, val in enumerate(row): 
        if val == "#": 
            galaxy.append((x, y))

for a, b in itertools.combinations(galaxy, 2):
    sumOfShortestPath += abs(a[0] - b[0]) + abs(a[1] - b[1])

print(sumOfShortestPath)

#Part 2 Solution (better approach, increasing index for POIs)
f1 = open("day11.txt")

sumOfShortestPath = 0 
foundColumn = set()
galaxy = []
curY = 0

for y, line in enumerate(f1):
    line = list(line.strip())
    doubleLine = True 

    for x, val in enumerate(line): 
        if val == "#": 
            galaxy.append((x, curY))
            doubleLine = False
            foundColumn.add(x)
    
    if doubleLine == True:
        curY += 1000000
    else:
        curY += 1

lenX = len(line)

for x in range(lenX - 1, 0, -1):
    if x not in foundColumn:
        for indx, val in enumerate(galaxy): 
            if val[0] > x:
                galaxy[indx] = (val[0] + 999999, val[1])

for a, b in itertools.combinations(galaxy, 2):
    sumOfShortestPath += abs(a[0] - b[0]) + abs(a[1] - b[1])

print(sumOfShortestPath)
