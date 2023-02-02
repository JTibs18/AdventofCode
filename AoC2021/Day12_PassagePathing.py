#Part 1 Solution
f1 = open("day12.txt")

connections = dict() 
foundPathsCount = 0

for line in f1:
    cave1, cave2 = line.strip().split('-')
    
    if cave1 in connections: 
        connections[cave1].append(cave2)
    else: 
        connections[cave1] = [cave2]

    if cave2 in connections: 
        connections[cave2].append(cave1)
    else: 
        connections[cave2] = [cave1]

queue = [['start']]

while queue: 
    curPath = queue.pop(0)
    lastElement = curPath[len(curPath) - 1]

    if lastElement == 'end': 
        foundPathsCount += 1  
    else: 
        for i in connections[lastElement]: 
            if i != 'start' and (i == 'end' or i.isupper() or i not in curPath): 
                queue.append(curPath + [i])
    
print(foundPathsCount)

#Part 2 Solution
f1 = open("day12.txt")

connections = dict() 
foundPathsCount = 0

for line in f1:
    cave1, cave2 = line.strip().split('-')
    
    if cave1 in connections: 
        connections[cave1].append(cave2)
    else: 
        connections[cave1] = [cave2]

    if cave2 in connections: 
        connections[cave2].append(cave1)
    else: 
        connections[cave2] = [cave1]

queue = [(['start'], False)]

while queue: 
    curPath = queue.pop(0)
    lastElement = curPath[0][len(curPath[0]) - 1]

    if lastElement == 'end': 
        foundPathsCount += 1  
    else: 
        for i in connections[lastElement]: 
            if i != 'start' and (i == 'end' or i.isupper() or i not in curPath[0]): 
                queue.append((curPath[0] + [i], curPath[1]))
            elif curPath[1] == False and i != 'start' and i != 'end' and i in curPath[0]: 
                queue.append((curPath[0] + [i], True))

print(foundPathsCount)
