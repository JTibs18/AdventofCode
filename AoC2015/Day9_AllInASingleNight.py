#Part 1 Solution
f1 = open("day9.txt")

destinationDistances = dict()
unvisited = []

for line in f1:
    curLocation, toParse = line.strip().split(" to ")
    destination, distance = toParse.split(' = ')
    distance = int(distance)
    
    if curLocation in destinationDistances: 
        destinationDistances[curLocation].append((destination, distance))
    else: 
        destinationDistances[curLocation] = [(destination, distance)]

    unvisited.append(curLocation)

parent = [-1]
queue = []

queue.append(unvisited[0])
unvisited.pop(unvisited[0])

while queue: 
    curPath = queue.pop(0)

    for i in destinationDistances[]