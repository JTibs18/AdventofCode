#Part 1 Solution
import hashlib 

f1 = open("day17.txt")

startCoordinates = (0, 0)
endCoordinates = (3, 3)
queue = [[startCoordinates]]
pathQueue = [""]

for line in f1:
    code = line

while queue: 
    curPathCoords = queue.pop(0)
    curPath = pathQueue.pop(0)
    lastElement = curPathCoords[len(curPathCoords) - 1]

    if lastElement == endCoordinates: 
        print(curPath)
        break 
    else: 
        passcode = code + curPath
        passcodeHash = hashlib.md5(passcode.encode()).hexdigest() 

        if passcodeHash[0] in "bcdef" and lastElement[1] - 1 >= 0:
            queue.append(curPathCoords + [(lastElement[0], lastElement[1] - 1)])
            pathQueue.append(curPath + "U")
        if passcodeHash[1] in "bcdef" and lastElement[1] + 1 < 4:
            queue.append(curPathCoords + [(lastElement[0], lastElement[1] + 1)])
            pathQueue.append(curPath + "D")
        if passcodeHash[2] in "bcdef" and lastElement[0] - 1 >= 0:
            queue.append(curPathCoords + [(lastElement[0] - 1, lastElement[1])])
            pathQueue.append(curPath + "L")
        if passcodeHash[3] in "bcdef" and lastElement[0] + 1 < 4:
            queue.append(curPathCoords + [(lastElement[0] + 1, lastElement[1])])
            pathQueue.append(curPath + "R")

#Part 2 Solution
import hashlib 

f1 = open("day17.txt")

longestPath = 0 
startCoordinates = (0, 0)
endCoordinates = (3, 3)
queue = [[startCoordinates]]
pathQueue = [""]

for line in f1:
    code = line

while queue: 
    curPathCoords = queue.pop(0)
    curPath = pathQueue.pop(0)
    lastElement = curPathCoords[len(curPathCoords) - 1]

    if lastElement == endCoordinates: 
        if len(curPath) > longestPath: 
            longestPath = len(curPath)
    else: 
        passcode = code + curPath
        passcodeHash = hashlib.md5(passcode.encode()).hexdigest()

        if passcodeHash[0] in "bcdef" and lastElement[1] - 1 >= 0:
            queue.append(curPathCoords + [(lastElement[0], lastElement[1] - 1)])
            pathQueue.append(curPath + "U")
        if passcodeHash[1] in "bcdef" and lastElement[1] + 1 < 4:
            queue.append(curPathCoords + [(lastElement[0], lastElement[1] + 1)])
            pathQueue.append(curPath + "D")
        if passcodeHash[2] in "bcdef" and lastElement[0] - 1 >= 0:
            queue.append(curPathCoords + [(lastElement[0] - 1, lastElement[1])])
            pathQueue.append(curPath + "L")
        if passcodeHash[3] in "bcdef" and lastElement[0] + 1 < 4:
            queue.append(curPathCoords + [(lastElement[0] + 1, lastElement[1])])
            pathQueue.append(curPath + "R")

print(longestPath)