# Part 1 Solution
f1 = open("day22.txt")
startCoord = (0, 0)
erosionLevel = dict()
risk = dict() 

# parse input
for line in f1:
    if "depth" in line.strip():
        depth = int(line.split(": ")[1])
    else: 
        endCoord = line.split(": ")[1]
        endCoord = endCoord.split(",")
        endCoord = (int(endCoord[0]), int(endCoord[1]))

queue = [startCoord]

# bfs to find coordinates to calculate erosion and geologic index 
while queue: 
    curCoord = queue.pop(0)

    # geological index
    if curCoord == startCoord or curCoord == endCoord: 
        geologicalIndex = 0 
    elif curCoord[1] == 0: 
        geologicalIndex = curCoord[0] * 16807
    elif curCoord[0] == 0: 
        geologicalIndex = curCoord[1] * 48271
    else: 
        geologicalIndex = erosionLevel[(curCoord[0] - 1, curCoord[1])] * erosionLevel[(curCoord[0], curCoord[1] - 1)] 
    
    # erosion level 
    curErosionLevel = (geologicalIndex + depth) % 20183
    erosionLevel[curCoord] = curErosionLevel
    
    if curErosionLevel % 3 == 0: 
        risk[curCoord] = 0
    elif curErosionLevel % 3 == 1: 
        risk[curCoord] = 1
    else: 
        risk[curCoord] = 2
    
    # adding adjacent coordinates to queue 
    if curCoord[0] + 1 <= endCoord[0] and (curCoord[0] + 1, curCoord[1]) not in queue and (curCoord[0] + 1, curCoord[1]) not in risk: 
        queue.append((curCoord[0] + 1, curCoord[1]))
    if curCoord[1] + 1 <= endCoord[1] and (curCoord[0], curCoord[1] + 1) not in queue and (curCoord[0], curCoord[1] + 1) not in risk: 
        queue.append((curCoord[0], curCoord[1] + 1))

# summating the risk 
print(sum(risk.values()))

# Part 2  Solution
f1 = open("day22.txt")
startCoord = (0, 0)
erosionLevel = dict()
risk = dict() 
minMinutes = 1000000000000

# parse input
for line in f1:
    if "depth" in line.strip():
        depth = int(line.split(": ")[1])
    else: 
        endCoord = line.split(": ")[1]
        endCoord = endCoord.split(",")
        endCoord = (int(endCoord[0]), int(endCoord[1]))

queue = [startCoord]

# bfs to find coordinates to calculate erosion and geologic index 
while queue: 
    curCoord = queue.pop(0)

    # geological index
    if curCoord == startCoord or curCoord == endCoord: 
        geologicalIndex = 0 
    elif curCoord[1] == 0: 
        geologicalIndex = curCoord[0] * 16807
    elif curCoord[0] == 0: 
        geologicalIndex = curCoord[1] * 48271
    else: 
        geologicalIndex = erosionLevel[(curCoord[0] - 1, curCoord[1])] * erosionLevel[(curCoord[0], curCoord[1] - 1)] 
    
    # erosion level 
    curErosionLevel = (geologicalIndex + depth) % 20183
    erosionLevel[curCoord] = curErosionLevel
    
    if curErosionLevel % 3 == 0: 
        risk[curCoord] = 0
    elif curErosionLevel % 3 == 1: 
        risk[curCoord] = 1
    else: 
        risk[curCoord] = 2
    
    # adding adjacent coordinates to queue 
    if curCoord[0] + 1 <= endCoord[0] + 100 and (curCoord[0] + 1, curCoord[1]) not in queue and (curCoord[0] + 1, curCoord[1]) not in risk: 
        queue.append((curCoord[0] + 1, curCoord[1]))
    if curCoord[1] + 1 <= endCoord[1] + 100 and (curCoord[0], curCoord[1] + 1) not in queue and (curCoord[0], curCoord[1] + 1) not in risk: 
        queue.append((curCoord[0], curCoord[1] + 1))


queue = [startCoord]
minutesQueue = [0]
toolQueue = ["torch"]

while queue: 
    curPath = queue.pop(0)
    curMinutes = minutesQueue.pop(0)
    lastElement = curPath[len(curPath) - 1]

    if lastElement == endCoord and curMinutes < minMinutes: 
        minMinutes = curMinutes
    elif curMinutes < minMinutes: 
        if (curPath[0] + 1, curPath[1]) not in curPath and (curPath[0] + 1, curPath[1]) in risk: 
            if risk[(curPath[0] + 1, curPath[1])] == risk[curPath]: 
                curMinutes += 1 
                minutesQueue.append(curMinutes)
                queue.append((curPath[0] + 1, curPath[1]))

                # How to know what tool to select if changing terrains?? 