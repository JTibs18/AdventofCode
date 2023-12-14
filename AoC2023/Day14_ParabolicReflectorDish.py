#Part 1 Solution  
f1 = open("day14.txt")

grid = []
load = 0

for line in f1:
    row = list(line.strip())
    grid.append(row)

for indx, row in enumerate(grid):
    if indx == 0:
        continue 

    for x, val in enumerate(row):
        curIndx = indx
        while val == "O" and grid[curIndx - 1][x] == "." and curIndx > 0:
            grid[curIndx - 1][x] = val 
            grid[curIndx][x] = "."
            curIndx -= 1 

for i in range(len(grid)):
    load += (len(grid) - i) * grid[i].count("O")

print(load)

#Part 2 Solution  
f1 = open("day14.txt")

grid = []
load = 0

# calculated with equation: cycles = pattern offset aka the first cycle index where a pattern begins + ((number of cycles required - pattern offset) % size of pattern before repeats)
cycles = 171 + ((1000000000 - 171) % 28)

for line in f1:
    row = list(line.strip())
    grid.append(row)

while cycles:
    # north 
    for indx, row in enumerate(grid):
        if indx == 0:
            continue 

        for x, val in enumerate(row):
            curIndx = indx
            while val == "O" and grid[curIndx - 1][x] == "." and curIndx > 0:
                grid[curIndx - 1][x] = val 
                grid[curIndx][x] = "."
                curIndx -= 1 

    # west
    for indx, row in enumerate(grid):
        for x, val in enumerate(row):
            if x == 0: 
                continue
            
            curIndx = x 

            while val == "O" and grid[indx][curIndx - 1] == "." and curIndx > 0:
                grid[indx][curIndx - 1] = val 
                grid[indx][curIndx] = "."
                curIndx -= 1 

    # south 
    for indx in range(len(grid) - 1, -1, -1):
        if indx == len(grid) - 1:
            continue

        for x, val in enumerate(grid[indx]): 
            curIndx = indx 
            while val == "O" and curIndx < len(grid) - 1 and grid[curIndx + 1][x] == ".":
                grid[curIndx + 1][x] = val 
                grid[curIndx][x] = "."
                curIndx += 1 
    # east        
    for indx, row in enumerate(grid):
        for x in range(len(row) - 1, -1, -1):
            if x == len(row) - 1:
                continue 

            val = grid[indx][x]
            curIndx = x 

            while val == "O" and curIndx < len(row) - 1 and grid[indx][curIndx + 1] == "." :
                grid[indx][curIndx + 1] = val 
                grid[indx][curIndx] = "."
                curIndx += 1

    cycles -= 1
    load = 0

    for i in range(len(grid)):
        load += (len(grid) - i) * grid[i].count("O")
    
print(load)