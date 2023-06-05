#Part 1 Solution
f1 = open("day18.txt")

walkableSpaces = set()
connections = dict()
keys = dict() # key is letter, value is coordinates 
doors = dict() # key is coordinates, value is letter
startingCoord = (0,0)
yIndx = 0

# parsing input
for line in f1:
    for indx, val in enumerate(line): 
        if val == '@': 
            startingCoord = (indx, yIndx)
            walkableSpaces.add((indx, yIndx))
        elif val == ".": 
            walkableSpaces.add((indx, yIndx))
        elif val in "ABCDEFGHIJKLMNOPQRSTUVWXYZ": 
            doors[(indx, yIndx)] = val 
            walkableSpaces.add((indx, yIndx))
        elif val in "abcdefghijklmnopqrstuvwxyz": 
            keys[val] = (indx, yIndx)
            walkableSpaces.add((indx, yIndx))

    yIndx += 1

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

queue = [[startingCoord]]
uniqueKeysQueue = [set()]
foundKeys = set() 

# bfs 
while queue: 
    curPath = queue.pop(0)
    uniqueKeys = uniqueKeysQueue.pop(0)
    lastElement = curPath[len(curPath) - 1]
    previousElement = curPath[len(curPath) - 2]

    if len(uniqueKeys) == len(keys): 
        print(len(curPath), curPath)
        break 
    elif foundKeys == uniqueKeys: 
        for i in connections[lastElement]: 
            if i in keys.values(): 
                foundKeys.add(i)
                uniqueKeys.add(i)
                queue.append(curPath + [i])
                uniqueKeysQueue.append(uniqueKeys)
            elif i in doors.keys() and keys[doors[i].lower()] in curPath: 
                queue.append(curPath + [i])
                uniqueKeysQueue.append(uniqueKeys)
            elif (i not in doors.keys()) and i != previousElement: 
                queue.append(curPath + [i])
                uniqueKeysQueue.append(uniqueKeys)


# Tough problem...need memoization, logic, pathfinding & bfs. 
# Doesn't pass second test case, takes too long. 