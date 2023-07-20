#Part 1 Solution
f1 = open("day9.txt")

destinationDistances = dict()
unvisited = set()
queue = []
minDistance = 10000000

for line in f1:
    curLocation, toParse = line.strip().split(" to ")
    destination, distance = toParse.split(' = ')
    distance = int(distance)
    
    if curLocation in destinationDistances: 
        destinationDistances[curLocation].append((destination, distance))
    else: 
        destinationDistances[curLocation] = [(destination, distance)]

    if destination in destinationDistances: 
        destinationDistances[destination].append((curLocation, distance))
    else: 
        destinationDistances[destination] = [(curLocation, distance)]

    unvisited.add(curLocation)
    unvisited.add(destination)

startList = list(unvisited)

for city in startList: 
    unvisited = startList[:]

    queue.append(city)
    unvisited.remove(city)
    totalDistance = 0

    while queue: 
        curPath = queue.pop(0)
        nextNodeName = ''
        nextNodeDistance = 10000000

        for name, dist in destinationDistances[curPath]: 
            if dist < nextNodeDistance and name in unvisited: 
                nextNodeDistance = dist
                nextNodeName = name 
        
        if nextNodeName != "": 
            unvisited.remove(nextNodeName)
            queue.append(nextNodeName)
            totalDistance += nextNodeDistance

    if totalDistance < minDistance: 
        minDistance = totalDistance

print(minDistance)
    
# Part 2 Solution 
f1 = open("day9.txt")

destinationDistances = dict()
unvisited = set()
queue = []
maxDistance = 0

for line in f1:
    curLocation, toParse = line.strip().split(" to ")
    destination, distance = toParse.split(' = ')
    distance = int(distance)
    
    if curLocation in destinationDistances: 
        destinationDistances[curLocation].append((destination, distance))
    else: 
        destinationDistances[curLocation] = [(destination, distance)]

    if destination in destinationDistances: 
        destinationDistances[destination].append((curLocation, distance))
    else: 
        destinationDistances[destination] = [(curLocation, distance)]

    unvisited.add(curLocation)
    unvisited.add(destination)

startList = list(unvisited)

for city in startList: 
    unvisited = startList[:]

    queue.append(city)
    unvisited.remove(city)
    totalDistance = 0

    while queue: 
        curPath = queue.pop(0)
        nextNodeName = ''
        nextNodeDistance = 0

        for name, dist in destinationDistances[curPath]: 
            if dist > nextNodeDistance and name in unvisited: 
                nextNodeDistance = dist
                nextNodeName = name 
        
        if nextNodeName != "": 
            unvisited.remove(nextNodeName)
            queue.append(nextNodeName)
            totalDistance += nextNodeDistance

    if totalDistance > maxDistance: 
        maxDistance = totalDistance

print(maxDistance)