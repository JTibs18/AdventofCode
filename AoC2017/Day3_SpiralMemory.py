#Part 1 Solution
import math

f1 = open("day3.txt")

for line in f1:
    num = int(line)

outer = math.ceil((math.ceil(math.sqrt(num)) - 1) / 2)
prevSquare = (((outer * 2) - 1) ** 2)
straight = []

straight.append(prevSquare + outer)

for i in range(1, 4):
    straight.append(straight[i - 1] + (outer * 2))

if num in straight:
    print(outer)
else:
    min = outer
    for i in range(4):
        if abs(straight[i] - num) < min:
            min = abs(straight[i] - num)
    print(outer + min)

#Part 2 Solution
f1 = open("day3.txt")

for line in f1: 
    inputNum = int(line.strip())

directionPtr = 0 
repeat = 1
foundNums = [1]
grid = {(0, 0): 1}
curCoord = (0, 0)
direction = ["R", "U", "L", "D"]

while foundNums[-1] < inputNum:
    for i in range(0, repeat):
        if direction[directionPtr] == "R":
            newCoord = (curCoord[0] + 1, curCoord[1])
        elif direction[directionPtr] == "U":
            newCoord = (curCoord[0], curCoord[1] + 1)
        elif direction[directionPtr] == "L":
            newCoord = (curCoord[0] - 1, curCoord[1])
        else:
            newCoord = (curCoord[0], curCoord[1] - 1)
    
        newVal = 0 

        if (newCoord[0] - 1, newCoord[1] + 1) in grid:
            newVal += grid[(newCoord[0] - 1, newCoord[1] + 1)]

        if (newCoord[0] - 1, newCoord[1]) in grid:
            newVal += grid[(newCoord[0] - 1, newCoord[1])]

        if (newCoord[0] - 1, newCoord[1] - 1) in grid:
            newVal += grid[(newCoord[0] - 1, newCoord[1] - 1)]

        if (newCoord[0], newCoord[1] + 1) in grid:
            newVal += grid[(newCoord[0], newCoord[1] + 1)]

        if (newCoord[0], newCoord[1] - 1) in grid:
            newVal += grid[(newCoord[0], newCoord[1] - 1)]

        if (newCoord[0] + 1, newCoord[1] + 1) in grid:
            newVal += grid[(newCoord[0] + 1, newCoord[1] + 1)]

        if (newCoord[0] + 1, newCoord[1]) in grid:
            newVal += grid[(newCoord[0] + 1, newCoord[1])]

        if (newCoord[0] + 1, newCoord[1] - 1) in grid:
            newVal += grid[(newCoord[0] + 1, newCoord[1] - 1)]

        foundNums.append(newVal)
        grid[newCoord] = newVal
        curCoord = newCoord

        if foundNums[-1] > inputNum:
            break 

    if direction[directionPtr] == "U" or direction[directionPtr] == "D":
        repeat += 1

    directionPtr += 1
    if directionPtr == len(direction):
        directionPtr = 0

print(foundNums[-1])