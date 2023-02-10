#Part 1 Solution
f1 = open("day13.txt")

startCoordinates = (1, 1)
endCoordinates = (31, 39)
walkableSpaces = set() 
connections = dict()

# reading input 
for line in f1:
    favouriteNumber = line

# calculating walkable spaces in 100 x 100 grid
for x in range(100): 
    for y in range(100):

        bitCount = 0
        code = (x * x) + (3 * x) + (2 * x * y) + y + (y * y)
        code += int(favouriteNumber)
        code = str(bin(code))
        
        for bit in code:    
            if bit == "1": 
                bitCount += 1 
        
        if bitCount % 2 == 0: 
            walkableSpaces.add((x, y))

# creating adjacency list 
for x, y in walkableSpaces: 
    if (x + 1, y) in walkableSpaces: 
        if (x, y) in connections: 
            connections[(x, y)].append((x + 1, y))
        else: 
            connections[(x, y)] = [(x + 1, y)]
        
    if (x - 1, y) in walkableSpaces: 
        if (x, y) in connections: 
            connections[(x, y)].append((x - 1, y))
        else: 
            connections[(x, y)] = [(x - 1, y)]

    if (x, y + 1) in walkableSpaces: 
        if (x, y) in connections: 
            connections[(x, y)].append((x, y + 1))
        else: 
            connections[(x, y)] = [(x, y + 1)]

    if (x, y - 1) in walkableSpaces: 
        if (x, y) in connections: 
            connections[(x, y)].append((x, y - 1))
        else: 
            connections[(x, y)] = [(x, y - 1)]
    
queue = [[startCoordinates]]

# bfs
while queue: 
    curPath = queue.pop(0)
    lastElement = curPath[len(curPath) - 1]

    if lastElement == endCoordinates: 
        print(len(curPath) - 1) 
        break
    else: 
        for i in connections[lastElement]: 
            if i != startCoordinates and i not in curPath: 
                queue.append(curPath + [i])

#Part 2 Solution
f1 = open("day13.txt")

startCoordinates = (1, 1)
walkableSpaces = set() 
endLocations = set() 
connections = dict()

# reading input 
for line in f1:
    favouriteNumber = line

# calculating walkable spaces in 100 x 100 grid
for x in range(100): 
    for y in range(100):
        
        bitCount = 0
        code = (x * x) + (3 * x) + (2 * x * y) + y + (y * y)
        code += int(favouriteNumber)
        code = str(bin(code))

        for bit in code:    
            if bit == "1": 
                bitCount += 1 

        if bitCount % 2 == 0: 
            walkableSpaces.add((x, y))

# creating adjacency list 
for x, y in walkableSpaces: 
    if (x + 1, y) in walkableSpaces: 
        if (x, y) in connections: 
            connections[(x, y)].append((x + 1, y))
        else: 
            connections[(x, y)] = [(x + 1, y)]
        
    if (x - 1, y) in walkableSpaces: 
        if (x, y) in connections: 
            connections[(x, y)].append((x - 1, y))
        else: 
            connections[(x, y)] = [(x - 1, y)]

    if (x, y + 1) in walkableSpaces: 
        if (x, y) in connections: 
            connections[(x, y)].append((x, y + 1))
        else: 
            connections[(x, y)] = [(x, y + 1)]

    if (x, y - 1) in walkableSpaces: 
        if (x, y) in connections: 
            connections[(x, y)].append((x, y - 1))
        else: 
            connections[(x, y)] = [(x, y - 1)]
    
queue = [[startCoordinates]]

# bfs
while queue: 
    curPath = queue.pop(0)
    lastElement = curPath[len(curPath) - 1]
    endLocations.add(lastElement)

    if len(curPath) - 1 != 50: 
        for i in connections[lastElement]:
            if i != startCoordinates and i not in curPath: 
                queue.append(curPath + [i])
    
print(len(endLocations))

