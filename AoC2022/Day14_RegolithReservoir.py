# Part 1 Solution
f1 = open("day14.txt")

instructions = []
rocks = set()
sand = set()
curSand = (500, 0)
maxX = 500
minX = 500 
maxY = 0

for line in f1:
    path = []
    line = line.strip().split(" -> ")
    for i in line: 
        path.append(i.split(','))

    instructions.append(path)

for i in instructions: 
    xStart = ''
    yStart = ''
    xStop = ''
    yStop = ''
    for j in i: 
        if xStart == '':
            xStart = int(j[0])
            yStart = int(j[1])
            rocks.add((xStart, yStart))
        elif xStop == '': 
            xStop = int(j[0])
            yStop = int(j[1])
            if xStop - xStart > 0: 
                for k in range(xStop - xStart): 
                    rocks.add((xStart + k + 1, yStart))
            elif xStart - xStop > 0: 
                for k in range(xStart - xStop): 
                    rocks.add((xStart - k - 1, yStart))
            if yStop - yStart > 0: 
                for k in range(yStop - yStart): 
                    rocks.add((xStart, yStart + k + 1))
            elif yStart - yStop > 0: 
                for k in range(yStart - yStop): 
                    rocks.add((xStart, yStart - k - 1))
            
            xStart = xStop
            yStart = yStop
            xStop = ''

for i in rocks: 
    if i[0] > maxX: 
        maxX = i[0]
    elif i[0] < minX: 
        minY = i[0]
    if i[1] > maxY: 
        maxY = i[1]

while (curSand[0] >= minX or curSand[0] <= maxX) and curSand[1] <= maxY: 
    if (curSand[0], curSand[1] + 1) not in rocks and (curSand[0], curSand[1] + 1) not in sand: 
        curSand = (curSand[0], curSand[1] + 1)
    elif (curSand[0] - 1, curSand[1] + 1) not in rocks and (curSand[0] - 1, curSand[1] + 1) not in sand: 
        curSand = (curSand[0] - 1, curSand[1] + 1)
    elif (curSand[0] + 1, curSand[1] + 1) not in rocks and (curSand[0] + 1, curSand[1] + 1) not in sand: 
        curSand = (curSand[0] + 1, curSand[1] + 1)
    else: 
        sand.add(curSand)
        curSand = (500, 0)

print(len(sand))

# Part 2 Solution
f1 = open("day14.txt")

instructions = []
rocks = set()
sand = set()
curSand = (500, 0)
maxX = 500
minX = 500 
maxY = 0

for line in f1:
    path = []
    line = line.strip().split(" -> ")
    for i in line: 
        path.append(i.split(','))

    instructions.append(path)

for i in instructions: 
    xStart = ''
    yStart = ''
    xStop = ''
    yStop = ''
    for j in i: 
        if xStart == '':
            xStart = int(j[0])
            yStart = int(j[1])
            rocks.add((xStart, yStart))
        elif xStop == '': 
            xStop = int(j[0])
            yStop = int(j[1])
            if xStop - xStart > 0: 
                for k in range(xStop - xStart): 
                    rocks.add((xStart + k + 1, yStart))
            elif xStart - xStop > 0: 
                for k in range(xStart - xStop): 
                    rocks.add((xStart - k - 1, yStart))
            if yStop - yStart > 0: 
                for k in range(yStop - yStart): 
                    rocks.add((xStart, yStart + k + 1))
            elif yStart - yStop > 0: 
                for k in range(yStart - yStop): 
                    rocks.add((xStart, yStart - k - 1))
            
            xStart = xStop
            yStart = yStop
            xStop = ''

for i in rocks: 
    if i[1] > maxY: 
        maxY = i[1]

while True: 
    if (curSand[0], curSand[1] + 1) not in rocks and (curSand[0], curSand[1] + 1) not in sand and curSand[1] + 1 < maxY + 2: 
        curSand = (curSand[0], curSand[1] + 1)
    elif (curSand[0] - 1, curSand[1] + 1) not in rocks and (curSand[0] - 1, curSand[1] + 1) not in sand and curSand[1] + 1 < maxY + 2: 
        curSand = (curSand[0] - 1, curSand[1] + 1)
    elif (curSand[0] + 1, curSand[1] + 1) not in rocks and (curSand[0] + 1, curSand[1] + 1) not in sand and curSand[1] + 1 < maxY + 2: 
        curSand = (curSand[0] + 1, curSand[1] + 1)
    else: 
        if curSand == (500, 0): 
            sand.add(curSand)
            break

        sand.add(curSand)
        curSand = (500, 0)

print(len(sand))