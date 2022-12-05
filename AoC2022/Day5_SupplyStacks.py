# Part 1 Solution
import math
f1 = open("day5.txt")

crateStacks = [['' for x in range(8)] for y in range(9)]
readCrates = True
crateLines = []
instructions = []
topStack = ''

for line in f1:
    input = line.strip().split(' ')
    if input == ['']:
        readCrates = False
    elif readCrates == True:
        crateLines.append(input)
    else:
        instructions.append(input)

crateLines.pop()
newLineCrates = list(reversed(crateLines))

# parsing crates in 2d array of stacks
for indx, line in enumerate(newLineCrates):
    countStackIndx = 0
    stackIndx = 0
    for i, crate in enumerate(line):
        if crate == "":
            countStackIndx += 1
        elif countStackIndx > 0:
            countStackIndx = math.floor(countStackIndx / 4)
            stackIndx += countStackIndx
            crateStacks[stackIndx][indx] = crate
            countStackIndx = 0
            stackIndx += 1
        else:
            crateStacks[stackIndx][indx] = crate
            stackIndx += 1

# remove blank spaces in crate stack
for indx, val in enumerate(crateStacks):
    curLine = []
    for j in val:
        if j != '':
            curLine.append(j)
    crateStacks[indx] = curLine

# move crates
for i in instructions:
    for j in range(0, int(i[1])):
        remove = crateStacks[int(i[3]) - 1].pop()
        crateStacks[int(i[5]) - 1].append(remove)

# find top crate
for i in crateStacks:
    top = i.pop()
    topStack += top.strip('[]')

print(topStack)

# Part 2 Solution
f1 = open("day5.txt")

crateStacks = [['' for x in range(8)] for y in range(9)]
readCrates = True
crateLines = []
instructions = []
topStack = ''

for line in f1:
    input = line.strip().split(' ')
    if input == ['']:
        readCrates = False
    elif readCrates == True:
        crateLines.append(input)
    else:
        instructions.append(input)

crateLines.pop()
newLineCrates = list(reversed(crateLines))

# parsing crates in 2d array of stacks
for indx, line in enumerate(newLineCrates):
    countStackIndx = 0
    stackIndx = 0
    for i, crate in enumerate(line):
        if crate == "":
            countStackIndx += 1
        elif countStackIndx > 0:
            countStackIndx = math.floor(countStackIndx / 4)
            stackIndx += countStackIndx
            crateStacks[stackIndx][indx] = crate
            countStackIndx = 0
            stackIndx += 1
        else:
            crateStacks[stackIndx][indx] = crate
            stackIndx += 1

# remove blank spaces in crate stack
for indx, val in enumerate(crateStacks):
    curLine = []
    for j in val:
        if j != '':
            curLine.append(j)
    crateStacks[indx] = curLine

# move crates
for i in instructions:
    removeStack = []
    for j in range(0, int(i[1])):
        remove = crateStacks[int(i[3]) - 1].pop()
        removeStack.append(remove)
    crateStacks[int(i[5]) - 1].extend(list(reversed(removeStack)))

# find top crate
for i in crateStacks:
    if len(i) > 0:
        top = i.pop()
        topStack += top.strip('[]')

print(topStack)
