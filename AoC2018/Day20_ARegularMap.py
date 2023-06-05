#Part 1 Solution
f1 = open("day20.txt")

curGroup = ''
parent = ''
parentChildConnection = dict() 
parentStack = []
longestPath = 0

for line in f1:
        instructions = line.strip("^$")

for indx, val in enumerate(instructions): 
    if val == "(": 
        if parent in parentChildConnection: 
            parentChildConnection[parent].append(curGroup)
        else:
            parentChildConnection[parent] = [curGroup] 
        parentStack.append(parent)
        parent = curGroup 
        curGroup = ''
    elif val == ")" and instructions[indx - 1] != "|" and curGroup != '': 
        if parent in parentChildConnection: 
            parentChildConnection[parent].append(curGroup)
        else:
            parentChildConnection[parent] = [curGroup] 
        parent = parentStack.pop() 
        curGroup = ''
    elif val == "|" and instructions[indx + 1] != ")": 
        if parent in parentChildConnection: 
            parentChildConnection[parent].append(curGroup)
        else:
            parentChildConnection[parent] = [curGroup] 
        curGroup = ''
    elif (val == "|" and instructions[indx + 1] == ")"):
        curGroup = parent
        parent = parentStack.pop()
        parentChildConnection[parent].pop()
    elif val not in "|()":  
        curGroup += val

if parent in parentChildConnection: 
    parentChildConnection[parent].append(curGroup)
else:
    parentChildConnection[parent] = [curGroup] 

print(parentChildConnection)
queue = [[max(parentChildConnection[''])]]

while queue: 
    curPath = queue.pop(0)
    lastElement = curPath[len(curPath) - 1]

    if lastElement not in parentChildConnection: 
        count = 0
        for i in curPath: 
            count += len(i)
        
        if count > longestPath: 
            longestPath = count
    else: 
        for i in parentChildConnection[lastElement]: 
            if i != "" and i not in curPath: 
                queue.append(curPath + [i])

print(longestPath)

# Simply does not work on test input. Queue gets wayyyy to large
# Need a different strategy all together for parsing input and finding connections
# Need topological sort not bfs