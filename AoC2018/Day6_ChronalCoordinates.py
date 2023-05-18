#Part 1 Solution
def manhattanDistance(testCoord, mainCoord):
    return abs(mainCoord[0] - testCoord[0]) + abs(mainCoord[1] - testCoord[1])

f1 = open("day6.txt")

allCoordinates = dict() 
providedCoords = dict() 
sectionCount = dict()
infiniteSections = []
curNum = 0
maxSection = 0 

for line in f1:
    coord = line.strip().split(", ")
    curCoord = (int(coord[0]), int(coord[1]))
    providedCoords[curCoord] = curNum
    allCoordinates[curCoord] = curNum
    curNum += 1 

xBoundaryMax = max(providedCoords, key=lambda x:x[0])[0]
yBoundaryMax = max(providedCoords, key=lambda x:x[1])[1]

for xCoord in range(xBoundaryMax): 
    for yCoord in range(yBoundaryMax): 
        minDistance = dict()
        
        for i in providedCoords.keys(): 
            dist = manhattanDistance((xCoord, yCoord), i)
            minDistance[providedCoords[i]] = dist

        distances = sorted(minDistance.values())

        if distances[0] != distances[1]: 
            allCoordinates[(xCoord, yCoord)] = [k for k, v in minDistance.items() if v == distances[0]][0]
                
for key, val in allCoordinates.items(): 
    if key[0] == 0 or key[1] == 0 or key[0] == xBoundaryMax or key[1] == yBoundaryMax: 
        infiniteSections.append(val)
    if val in sectionCount: 
        sectionCount[val] += 1 
    else: 
        sectionCount[val] = 1 

for key, val in sectionCount.items(): 
    if key not in infiniteSections and val > maxSection: 
        maxSection = val 

print(maxSection)

#Part 2 Solution
def manhattanDistance(testCoord, mainCoord):
    return abs(mainCoord[0] - testCoord[0]) + abs(mainCoord[1] - testCoord[1])

f1 = open("day6.txt")

allCoordinates = []
providedCoords = []

for line in f1:
    coord = line.strip().split(", ")
    curCoord = (int(coord[0]), int(coord[1]))
    providedCoords.append(curCoord)

xBoundaryMax = max(providedCoords, key=lambda x:x[0])[0]
yBoundaryMax = max(providedCoords, key=lambda x:x[1])[1]

for xCoord in range(xBoundaryMax): 
    for yCoord in range(yBoundaryMax): 
        minDistance = []

        for i in providedCoords: 
            dist = manhattanDistance((xCoord, yCoord), i)
            minDistance.append(dist)
        
        if sum(minDistance) < 10000: 
            allCoordinates.append((xCoord, yCoord))

print(len(allCoordinates))
