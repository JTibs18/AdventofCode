#Part 1 Solution
f1 = open("day10.txt")

grid = dict()
foundPoints = set()
start = ()
steps = 0

for y, line in enumerate(f1):
    line = line.strip()

    for x, val in enumerate(line): 
        grid[(x, y)] = val 

        if val == "S":
            start = (x, y) 

queue = [start]
foundPoints.add(start)

while queue: 
    curPoint = queue.pop(0)
    foundPoints.add(curPoint)

    if grid[curPoint] == "S" or grid[curPoint] == "|" or grid[curPoint] == "L" or grid[curPoint] == "J":
        nextPoint = (curPoint[0], curPoint[1] - 1) 

        if nextPoint in grid and nextPoint not in foundPoints and nextPoint not in queue and (grid[nextPoint] == "|" or grid[nextPoint] == "7" or grid[nextPoint] == "F"):
            steps += 1
            queue.append(nextPoint)

    if grid[curPoint] == "S" or grid[curPoint] == "|" or grid[curPoint] == "F" or grid[curPoint] == "7":
        nextPoint = (curPoint[0], curPoint[1] + 1) 
        
        if nextPoint in grid and nextPoint not in foundPoints and nextPoint not in queue and (grid[nextPoint] == "|" or grid[nextPoint] == "L" or grid[nextPoint] == "J"): 
            steps += 1
            queue.append(nextPoint)
    
    if grid[curPoint] == "S" or grid[curPoint] == "-" or grid[curPoint] == "L" or grid[curPoint] == "F":
        nextPoint = (curPoint[0] + 1, curPoint[1]) 
        
        if nextPoint in grid  and nextPoint not in foundPoints and nextPoint not in queue and (grid[nextPoint] == "-" or grid[nextPoint] == "7" or grid[nextPoint] == "J"):
            steps += 1
            queue.append(nextPoint)
    
    if grid[curPoint] == "S" or grid[curPoint] == "-" or grid[curPoint] == "7" or grid[curPoint] == "J":
        nextPoint = (curPoint[0] - 1, curPoint[1]) 
        
        if nextPoint in grid and nextPoint not in foundPoints and nextPoint not in queue and (grid[nextPoint] == "-" or grid[nextPoint] == "L" or grid[nextPoint] == "F"): 
            steps += 1
            queue.append(nextPoint)
        
if steps % 2 != 0:
    steps += 1 

print(steps // 2)

#Part 2 Solution (takes a few seconds to complete)
f1 = open("day10.txt")

grid = dict()
start = ()
foundPoints = []
steps = 0
curSumA = 0
curSumB = 0 

for y, line in enumerate(f1):
    line = line.strip()
    
    for x, val in enumerate(line): 
        grid[(x, y)] = val 

        if val == "S":
            start = (x, y) 

queue = [start]

while queue: 
    curPoint = queue.pop() 
    foundPoints.append(curPoint)

    if grid[curPoint] == "S" or grid[curPoint] == "|" or grid[curPoint] == "L" or grid[curPoint] == "J":
        nextPoint = (curPoint[0], curPoint[1] - 1) 
        
        if nextPoint in grid and nextPoint not in queue and nextPoint not in foundPoints and (grid[nextPoint] == "|" or grid[nextPoint] == "7" or grid[nextPoint] == "F"):
            steps += 1
            queue.append(nextPoint)

    if grid[curPoint] == "S" or grid[curPoint] == "-" or grid[curPoint] == "L" or grid[curPoint] == "F":
        nextPoint = (curPoint[0] + 1, curPoint[1]) 
        
        if nextPoint in grid and nextPoint not in queue and nextPoint not in foundPoints and (grid[nextPoint] == "-" or grid[nextPoint] == "7" or grid[nextPoint] == "J"):
            steps += 1
            queue.append(nextPoint)

    if grid[curPoint] == "S" or grid[curPoint] == "|" or grid[curPoint] == "F" or grid[curPoint] == "7":
        nextPoint = (curPoint[0], curPoint[1] + 1) 
        
        if nextPoint in grid and nextPoint not in queue and nextPoint not in foundPoints and (grid[nextPoint] == "|" or grid[nextPoint] == "L" or grid[nextPoint] == "J"): 
            steps += 1
            queue.append(nextPoint)
            
    if grid[curPoint] == "S" or grid[curPoint] == "-" or grid[curPoint] == "7" or grid[curPoint] == "J":
        nextPoint = (curPoint[0] - 1, curPoint[1]) 
        
        if nextPoint in grid and nextPoint not in queue and nextPoint not in foundPoints and (grid[nextPoint] == "-" or grid[nextPoint] == "L" or grid[nextPoint] == "F"): 
            steps += 1
            queue.append(nextPoint)

# using shoelace formula https://www.101computing.net/the-shoelace-algorithm/ 
for i in range(0, len(foundPoints) - 1):
    curSumA += foundPoints[i][0] * foundPoints[i + 1][1]
    curSumB += foundPoints[i][1] * foundPoints[i + 1][0]

curSumA += foundPoints[len(foundPoints) - 1][0] * foundPoints[0][1]
curSumB += foundPoints[0][0] * foundPoints[len(foundPoints) -1][1]

total = abs(curSumA - curSumB) // 2
print(total - (steps // 2))