# Part 1 Solution
f1 = open("day11.txt")

gridSerialNumber = 0
mostPower = 0 
grid = []
coord = ()

# parsing input
for line in f1: 
    gridSerialNumber = int(line.strip())

# finding power level of each cell 
for y in range(1, 301):
    row = []

    for x in range(1, 301): 
        rackId = x + 10 
        powerLevel = rackId * y 
        powerLevel += gridSerialNumber
        powerLevel *= rackId
        digits = list(str(powerLevel))
        
        if len(digits) < 3: 
            powerLevel = 0 
        else: 
            powerLevel = int(digits[len(digits) - 3])
        
        powerLevel -= 5 
        row.append(powerLevel)
    
    grid.append(row)

# finding 3x3 square with largest total power 
for y in range(1, 298): 
    for x in range(1, 298): 
        power = grid[y][x] + grid[y + 1][x] + grid[y + 2][x] + grid[y][x + 1] + grid[y + 1][x + 1] + grid[y + 2][x + 1] + grid[y][x + 2] + grid[y + 1][x + 2] + grid[y + 2][x + 2]
        
        if power > mostPower: 
            mostPower = power
            coord = (x + 1, y + 1)

print(coord)