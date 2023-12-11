#Part 1 Solution  
f1 = open("day19.txt")

direction = "D"
letterOrder = ""
grid = dict()
traversed = set()
start = ()

for y, line in enumerate(f1):
    row = line

    for x, val in enumerate(row):
        if val != " " and val != "\n":
            grid[(x, y)] = val

            if y == 0:
                start = (x, y)

queue = [start]

while queue:
    curCoord = queue.pop(0)
    traversed.add(curCoord)

    if grid[curCoord] == "+":
        if (curCoord[0] + 1, curCoord[1]) in grid and (curCoord[0] + 1, curCoord[1]) not in traversed: 
            queue.append((curCoord[0] + 1,  curCoord[1]))
            direction = "R"
        if (curCoord[0] - 1, curCoord[1]) in grid and (curCoord[0] - 1, curCoord[1]) not in traversed: 
            queue.append((curCoord[0] - 1,  curCoord[1]))
            direction = "L"
        if (curCoord[0], curCoord[1] + 1) in grid and (curCoord[0], curCoord[1] + 1) not in traversed: 
            queue.append((curCoord[0],  curCoord[1] + 1))
            direction = "D"
        if (curCoord[0], curCoord[1] - 1) in grid and (curCoord[0], curCoord[1] - 1) not in traversed: 
            queue.append((curCoord[0],  curCoord[1] - 1))
            direction = "U"
        continue 

    if grid[curCoord] != "-" and grid[curCoord] != "|":
        letterOrder += grid[curCoord]

    if direction == "R" and (curCoord[0] + 1, curCoord[1]) in grid: 
        queue.append((curCoord[0] + 1, curCoord[1]))
    elif direction == "L" and (curCoord[0] - 1, curCoord[1]) in grid:
        queue.append((curCoord[0] - 1, curCoord[1]))
    elif direction == "D" and (curCoord[0], curCoord[1] + 1) in grid: 
        queue.append((curCoord[0], curCoord[1] + 1))
    elif direction == "U" and (curCoord[0], curCoord[1] - 1) in grid:
        queue.append((curCoord[0], curCoord[1] - 1))

print(letterOrder)

#Part 2 Solution  
f1 = open("day19.txt")

direction = "D"
steps = 0
grid = dict()
traversed = set()
start = ()

for y, line in enumerate(f1):
    row = line

    for x, val in enumerate(row):
        if val != " " and val != "\n":
            grid[(x, y)] = val

            if y == 0:
                start = (x, y)

queue = [start]

while queue:
    curCoord = queue.pop(0)
    traversed.add(curCoord)
    steps += 1

    if grid[curCoord] == "+":
        if (curCoord[0] + 1, curCoord[1]) in grid and (curCoord[0] + 1, curCoord[1]) not in traversed: 
            queue.append((curCoord[0] + 1,  curCoord[1]))
            direction = "R"
        if (curCoord[0] - 1, curCoord[1]) in grid and (curCoord[0] - 1, curCoord[1]) not in traversed: 
            queue.append((curCoord[0] - 1,  curCoord[1]))
            direction = "L"
        if (curCoord[0], curCoord[1] + 1) in grid and (curCoord[0], curCoord[1] + 1) not in traversed: 
            queue.append((curCoord[0],  curCoord[1] + 1))
            direction = "D"
        if (curCoord[0], curCoord[1] - 1) in grid and (curCoord[0], curCoord[1] - 1) not in traversed: 
            queue.append((curCoord[0],  curCoord[1] - 1))
            direction = "U"
        continue 

    if grid[curCoord] != "-" and grid[curCoord] != "|":
        letterOrder += grid[curCoord]

    if direction == "R" and (curCoord[0] + 1, curCoord[1]) in grid: 
        queue.append((curCoord[0] + 1, curCoord[1]))
    elif direction == "L" and (curCoord[0] - 1, curCoord[1]) in grid:
        queue.append((curCoord[0] - 1, curCoord[1]))
    elif direction == "D" and (curCoord[0], curCoord[1] + 1) in grid: 
        queue.append((curCoord[0], curCoord[1] + 1))
    elif direction == "U" and (curCoord[0], curCoord[1] - 1) in grid:
        queue.append((curCoord[0], curCoord[1] - 1))

print(steps)