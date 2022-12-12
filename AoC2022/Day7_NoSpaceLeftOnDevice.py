# Part 1 Solution
f1 = open("day7.txt")

input = []
directoryDict = {}
directoryFileSizeCount = {}
currentDirectory = ''
totalSize = 0 

def findDirSize(dirName, size):
    if dirName in directoryDict: 
        for f in directoryDict[dirName]: 
            if len(f) > 1: 
                size += int(f[0])   
            else: 
                size += findDirSize(f[0], 0)
    else: 
        return 0 
    directoryFileSizeCount[dirName] = size
    return directoryFileSizeCount[dirName]
 
for line in f1:
    input.append(line.strip().split())

for command in input: 
    if command[1] == 'cd': 
        if command[2] == '..':
            path = currentDirectory.strip().split('/')
            if len(path) < 4: 
                currentDirectory = '/'
            else: 
                currentDirectory = '/' 
                path.pop(len(path) - 2)
                for i in path: 
                    if i != '': 
                        currentDirectory = currentDirectory + i + '/'
        elif command[2] == "/": 
            currentDirectory = "/"
            if currentDirectory not in directoryDict: 
                directoryDict[currentDirectory] = []
        else: 
            nextDirectory = currentDirectory + command[2] + '/' 
         
            if nextDirectory not in directoryDict: 
                directoryDict[nextDirectory] = [] 
        
            currentDirectory = nextDirectory
    elif command[0] == 'dir': 
        if currentDirectory in directoryDict: 
            directoryDict[currentDirectory].append([currentDirectory + command[1] + '/' ])
        else: 
            directoryDict[currentDirectory] = [[currentDirectory + command[1] + '/']]    
        
        if f'{currentDirectory}{command[1]}/' not in directoryDict: 
            directoryDict[f'{currentDirectory}{command[1]}/'] = []

    elif command[0] != '$': 
        if currentDirectory in directoryDict: 
            directoryDict[currentDirectory].append(command)
        else: 
            directoryDict[currentDirectory] = [command] 

findDirSize('/', 0)

for key, value in directoryFileSizeCount.items():
    if value <= 100000: 
        totalSize += value

print(totalSize)

# Part 2 Solution
f1 = open("day7.txt")

input = []
possibleDelete = []
directoryDict = {}
directoryFileSizeCount = {}
currentDirectory = ''
UNUSED_SPACE_NEEDED = 30000000
TOTAL_SPACE = 70000000

def findDirSize2(dirName, size):
    if dirName in directoryDict: 
        for f in directoryDict[dirName]: 
            if len(f) > 1: 
                size += int(f[0])   
            else: 
                size += findDirSize2(f[0], 0)
    else: 
        return 0 
    directoryFileSizeCount[dirName] = size
    return directoryFileSizeCount[dirName]
 
for line in f1:
    input.append(line.strip().split())

for command in input: 
    if command[1] == 'cd': 
        if command[2] == '..':
            path = currentDirectory.strip().split('/')
            if len(path) < 4: 
                currentDirectory = '/'
            else: 
                currentDirectory = '/' 
                path.pop(len(path) - 2)
                for i in path: 
                    if i != '': 
                        currentDirectory = currentDirectory + i + '/'
        elif command[2] == "/": 
            currentDirectory = "/"
            if currentDirectory not in directoryDict: 
                directoryDict[currentDirectory] = []
        else: 
            nextDirectory = currentDirectory + command[2] + '/' 
         
            if nextDirectory not in directoryDict: 
                directoryDict[nextDirectory] = [] 
        
            currentDirectory = nextDirectory
    elif command[0] == 'dir': 
        if currentDirectory in directoryDict: 
            directoryDict[currentDirectory].append([currentDirectory + command[1] + '/' ])
        else: 
            directoryDict[currentDirectory] = [[currentDirectory + command[1] + '/']]    
        
        if f'{currentDirectory}{command[1]}/' not in directoryDict: 
            directoryDict[f'{currentDirectory}{command[1]}/'] = []

    elif command[0] != '$': 
        if currentDirectory in directoryDict: 
            directoryDict[currentDirectory].append(command)
        else: 
            directoryDict[currentDirectory] = [command] 

findDirSize2('/', 0)

spaceNeeded = UNUSED_SPACE_NEEDED - (TOTAL_SPACE - directoryFileSizeCount['/'])

for key, value in directoryFileSizeCount.items():
    if value >= spaceNeeded: 
        possibleDelete.append(value)

sortedPossibleDelete = sorted(possibleDelete)
print(sortedPossibleDelete[0])