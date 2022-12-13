# Part 1 Solution
f1 = open("day12.txt")

input = []
queue = []
pred = []
visited = set()
indexY = 0
indexX = 0 

for line in f1:
    input.append(line.strip())

grid = [[0 for x in range(len(input[0]))] for y in range(len(input))]
for gridLine in input: 
    for i in gridLine:
        if i == "S":
            start = (indexX, indexY)
            grid[indexY][indexX] = ord('a')
            queue.append({"node": start, "dist": 0})
            visited.add((indexX, indexY))
        elif i == "E": 
            end = (indexX, indexY)
            grid[indexY][indexX] = ord('z')
        else: 
            grid[indexY][indexX] = ord(i)
        indexX += 1
    indexX = 0 
    indexY += 1

while len(queue) > 0: 
    current = queue.pop(0)

    if current["node"] == end: 
        print(current["dist"])
        break
    
    indexX = current["node"][0]
    indexY = current["node"][1]

    if indexY + 1 < len(grid) and (indexX, indexY + 1) not in visited and (grid[indexY][ indexX] >= grid[indexY + 1][indexX] or grid[indexY][indexX] + 1 == grid[indexY + 1][indexX]): 
        queue.append({"node": (indexX, indexY + 1), "dist": current['dist'] + 1})
        visited.add((indexX, indexY + 1))
    if indexY - 1 >= 0 and (indexX, indexY - 1) not in visited and (grid[indexY][indexX] >= grid[indexY - 1][indexX] or grid[indexY][indexX] + 1 == grid[indexY - 1][indexX]): 
        queue.append({"node": (indexX, indexY - 1), "dist": current['dist'] + 1})
        visited.add((indexX, indexY - 1))
    if indexX + 1 < len(grid[0]) and (indexX + 1, indexY) not in visited and (grid[indexY][indexX] >= grid[indexY][indexX + 1] or grid[indexY][indexX] + 1 == grid[indexY][indexX + 1]): 
        queue.append({"node": (indexX + 1, indexY), "dist": current['dist'] + 1})
        visited.add((indexX + 1, indexY))
    if indexX - 1 >= 0 and (indexX - 1, indexY) not in visited and (grid[indexY][indexX] >= grid[indexY][indexX - 1] or grid[indexY][indexX] + 1 == grid[indexY][indexX - 1]): 
        queue.append({"node": (indexX - 1, indexY), "dist": current['dist'] + 1})
        visited.add((indexX - 1, indexY))

# Part 2 Solution
f1 = open("day12.txt")

input = []
queue = []
pred = []
visited = set()
indexY = 0
indexX = 0 

for line in f1:
    input.append(line.strip())

grid = [[0 for x in range(len(input[0]))] for y in range(len(input))]
for gridLine in input: 
    for i in gridLine:
        if i == "S":
            grid[indexY][indexX] = ord('a')
        elif i == "E": 
            end = (indexX, indexY)
            grid[indexY][indexX] = ord('z')
            queue.append({"node": end, "dist": 0})
            visited.add((indexX, indexY))
        else: 
            grid[indexY][indexX] = ord(i)
        indexX += 1
    indexX = 0 
    indexY += 1

while len(queue) > 0: 
    current = queue.pop(0)
    indexX = current["node"][0]
    indexY = current["node"][1]

    if grid[indexY][indexX] == ord('a'): 
        print(current["dist"])
        break

    if indexY + 1 < len(grid) and (indexX, indexY + 1) not in visited and (grid[indexY][indexX] <= grid[indexY + 1][indexX] or grid[indexY][indexX] - 1 == grid[indexY + 1][indexX]): 
        queue.append({"node": (indexX, indexY + 1), "dist": current['dist'] + 1})
        visited.add((indexX, indexY + 1))
    if indexY - 1 >= 0 and (indexX, indexY - 1) not in visited and (grid[indexY][indexX] <= grid[indexY - 1][indexX] or grid[indexY][indexX] - 1 == grid[indexY - 1][indexX]): 
        queue.append({"node": (indexX, indexY - 1), "dist": current['dist'] + 1})
        visited.add((indexX, indexY - 1))
    if indexX + 1 < len(grid[0]) and (indexX + 1, indexY) not in visited and (grid[indexY][indexX] <= grid[indexY][indexX + 1] or grid[indexY][indexX] - 1 == grid[indexY][indexX + 1]): 
        queue.append({"node": (indexX + 1, indexY), "dist": current['dist'] + 1})
        visited.add((indexX + 1, indexY))
    if indexX - 1 >= 0 and (indexX - 1, indexY) not in visited and (grid[indexY][indexX] <= grid[indexY][indexX - 1] or grid[indexY][indexX] - 1 == grid[indexY][indexX - 1]): 
        queue.append({"node": (indexX - 1, indexY), "dist": current['dist'] + 1})
        visited.add((indexX - 1, indexY))