# Part 1 Solution
f1 = open("day10.txt")

def cycleCheck(cycle, X): 
    if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220: 
        sigStrength = X * cycle
        signals.append(sigStrength)

def manageCycles(queue, skip, X): 
    if len(queue) > 0:
        if queue[0] == 'noop' and skip == 0: 
            queue.pop(0)
        else: 
            skip += 1 
    if skip == 2: 
        skip = 0
        X += queue.pop(0)
    return queue, skip, X

instructions = []
signals = []
queue = []
X = 1
skip = 0
cycle = 0

for line in f1:
    instructions.append(line.strip().split(' '))

for i in instructions: 
    cycle += 1 
    cycleCheck(cycle, X)
    if len(i) > 1: 
        queue.append(int(i[1]))
    else: 
        queue.append(i[0])
    
    queue, skip, X = manageCycles(queue, skip, X)
    
while len(queue) > 0:
    cycle += 1
    cycleCheck(cycle, X)
    queue, skip, X = manageCycles(queue, skip, X)

print(sum(signals))

# Part 2 Solution
f1 = open("day10.txt")

def cyclePosition(crtPosition, verticalIndx): 
    if crtPosition == 40 or crtPosition == 80 or crtPosition == 120 or crtPosition == 160 or crtPosition == 200: 
        return verticalIndx + 1, 0
    return verticalIndx, crtPosition

def drawPixel(X, grid, crtPosition, verticalIndx): 
    if crtPosition == X or crtPosition == X - 1 or crtPosition == X + 1: 
        grid[verticalIndx][crtPosition] = "#"
    return grid 

def manageCycles2(queue, skip, X): 
    if len(queue) > 0:
        if queue[0] == 'noop' and skip == 0: 
            queue.pop(0)
        else: 
            skip += 1 
    if skip == 2: 
        skip = 0
        X += queue.pop(0)
    return queue, skip, X

grid = [['.' for x in range(40)] for y in range(6)]
instructions = []
queue = []
X = 1
skip = 0
cycle = 0
crtPosition = 0
verticalIndx = 0

for line in f1:
    instructions.append(line.strip().split(' '))

for i in instructions: 
    cycle += 1 
    verticalIndx, crtPosition = cyclePosition(crtPosition, verticalIndx)
    grid = drawPixel(X, grid, crtPosition, verticalIndx)
    crtPosition += 1
    if len(i) > 1: 
        queue.append(int(i[1]))
    else: 
        queue.append(i[0])
    
    queue, skip, X = manageCycles2(queue, skip, X)

while len(queue) > 0:
    cycle += 1
    verticalIndx, crtPosition = cyclePosition(crtPosition, verticalIndx)
    grid = drawPixel(X, grid, crtPosition, verticalIndx)
    crtPosition += 1
    queue, skip, X = manageCycles2(queue, skip, X)

print(grid)
