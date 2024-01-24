#Part 1 Solution
f1 = open("day13.txt")

x = 0 
y = 0
maximumHappiness = 0
graph = dict()
negative = False
NUM_SEATS = 8

# creating the graph
for line in f1:
    parsed = line.strip().split(" ")
    
    if x == y:
        y += 1 

    if y == NUM_SEATS:
        x += 1 
        y = 0

    coords = tuple(sorted([x, y]))

    if parsed[2] == "lose": 
        negative = True
    else:
        negative = False 

    if coords in graph or coords in graph:
        if negative:
            graph[coords] -= int(parsed[3])
        else:
            graph[coords] += int(parsed[3])
    else:
        if negative:
            graph[coords] = -1 * int(parsed[3])
        else: 
            graph[coords] = int(parsed[3])

    y += 1 

    if y == NUM_SEATS:
        x += 1 
        y = 0

# finding maximum happiness    
distances = []

for start in range(0, NUM_SEATS):
    q = [(start, 0, [])]

    while q:
        curNode, happiness, visited = q.pop(0)
        qCount = 0
        
        v = set(visited) 
        v.add(curNode)

        for i in range(0, NUM_SEATS):
            coords = tuple(sorted([curNode, i]))

            if coords in graph and i not in v:
                q.append((i, happiness + graph[coords], v))
                qCount += 1 
        
        coords = tuple(sorted([start, curNode]))

        if qCount == 0 and coords in graph:
            distances.append(happiness + graph[coords])

print(max(distances))

#Part 2 Solution (Takes about 30 seconds to run)
f1 = open("day13.txt")

x = 0 
y = 0
maximumHappiness = 0
graph = dict()
negative = False
NUM_SEATS = 9

# creating the graph
for line in f1:
    parsed = line.strip().split(" ")
    
    if x == y:
        y += 1 

    if y == NUM_SEATS - 1:
        x += 1 
        y = 0

    coords = tuple(sorted([x, y]))

    if parsed[2] == "lose": 
        negative = True
    else:
        negative = False 

    if coords in graph or coords in graph:
        if negative:
            graph[coords] -= int(parsed[3])
        else:
            graph[coords] += int(parsed[3])
    else:
        if negative:
            graph[coords] = -1 * int(parsed[3])
        else: 
            graph[coords] = int(parsed[3])

    y += 1 

    if y == NUM_SEATS - 1:
        x += 1 
        y = 0

# adding myself to graph 
for i in range(NUM_SEATS - 1):
    graph[(i, 8)] = 0

# finding maximum happiness    
distances = []

for start in range(0, NUM_SEATS):
    q = [(start, 0, [])]

    while q:
        curNode, happiness, visited = q.pop(0)
        qCount = 0
        
        v = set(visited) 
        v.add(curNode)

        for i in range(0, NUM_SEATS):
            coords = tuple(sorted([curNode, i]))
            
            if coords in graph and i not in v:
                q.append((i, happiness + graph[coords], v))
                qCount += 1 
        
        coords = tuple(sorted([start, curNode]))

        if qCount == 0 and coords in graph:
            distances.append(happiness + graph[coords])

print(max(distances))