# Part 1 Solution 
f1 = open("day22.txt")

direction = 0
infectedCount = 0
grid = dict()

for y, line in enumerate(f1):
    for indx, val in enumerate(line.strip()):
        grid[(indx, y)] = val 

virusCarrier = (indx // 2, y // 2)

for i in range(10000):
    if virusCarrier in grid and grid[virusCarrier] == "#":
        direction += 1 

        if direction == 4:
            direction = 0
        
        grid[virusCarrier] = "."
    else:
        direction -= 1 
        
        if direction == -1:
            direction = 3
        
        infectedCount += 1
        grid[virusCarrier] = "#"
    
    if direction == 0:
        virusCarrier = (virusCarrier[0], virusCarrier[1] - 1)
    elif direction == 1:
        virusCarrier = (virusCarrier[0] + 1, virusCarrier[1])
    elif direction == 2:
        virusCarrier = (virusCarrier[0], virusCarrier[1] + 1)
    else:
        virusCarrier = (virusCarrier[0] - 1, virusCarrier[1])

print(infectedCount)

# Part 2 Solution (takes about 30 seconds to run)
f1 = open("day22.txt")

direction = 0
infectedCount = 0
grid = dict()

for y, line in enumerate(f1):
    for indx, val in enumerate(line.strip()):
        if val == ".":
            grid[(indx, y)] = 0 
        else:
            grid[(indx, y)] = 2

virusCarrier = (indx // 2, y // 2)

for i in range(10000000):
    if virusCarrier in grid and grid[virusCarrier] == 2:
        direction += 1 

        if direction == 4:
            direction = 0
        
        grid[virusCarrier] += 1
    elif virusCarrier not in grid or grid[virusCarrier] == 0: 
        direction -= 1 
        
        if direction == -1:
            direction = 3
        
        grid[virusCarrier] = 1
    elif grid[virusCarrier] == 3:
        direction += 2

        if direction > 3:
            direction -= 4
        
        grid[virusCarrier] = 0
    else:
        grid[virusCarrier] += 1
        infectedCount += 1
        
    if direction == 0:
        virusCarrier = (virusCarrier[0], virusCarrier[1] - 1)
    elif direction == 1:
        virusCarrier = (virusCarrier[0] + 1, virusCarrier[1])
    elif direction == 2:
        virusCarrier = (virusCarrier[0], virusCarrier[1] + 1)
    else:
        virusCarrier = (virusCarrier[0] - 1, virusCarrier[1])

print(infectedCount)