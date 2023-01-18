#Part 1 Solution
import math 
f1 = open("day11.txt")

curStepX = 0
curStepY = 0

for line in f1:
    directions = line.strip().split(',')

for i in directions: 
    if i == "n":
        curStepY += 1 
    elif i == "ne": 
        curStepX += 1
        curStepY += 0.5
    elif i == "se": 
        curStepX += 1
        curStepY -= 0.5
    elif i == "s": 
        curStepY -= 1 
    elif i == "sw": 
        curStepX -= 1
        curStepY -= 0.5
    else: 
        curStepX -= 1 
        curStepY += 0.5

result = max(abs(math.floor(curStepX)), (abs(curStepY) + math.floor(abs(curStepX)/2)))
print(result)

#Part 2 Solution
f1 = open("day11.txt")

distances = set()
curStepX = 0
curStepY = 0

for line in f1:
    directions = line.strip().split(',')

for i in directions: 
    if i == "n":
        curStepY += 1 
    elif i == "ne": 
        curStepX += 1
        curStepY += 0.5
    elif i == "se": 
        curStepX += 1
        curStepY -= 0.5
    elif i == "s": 
        curStepY -= 1 
    elif i == "sw": 
        curStepX -= 1
        curStepY -= 0.5
    else: 
        curStepX -= 1 
        curStepY += 0.5
    
    distances.add(max(abs(math.floor(curStepX)), (abs(curStepY) + math.floor(abs(curStepX)/2))))

print(max(distances))