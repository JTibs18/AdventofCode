# Part 1 Solution
f1 = open("day24.txt")

grid = []
allGrids = []
indx = 0
biodiversityRating = 0

for line in f1:
    line = line.strip()
    row = []
    for i in line:
        row.append(i)
    grid.append(row)
allGrids.append(grid)

while (True):
    newGrid = [["." for x in range(5)] for y in range(5)]
    for x in range(5):
        for y in range(5):
            bugCount = 0
            if x + 1 < 5 and grid[x + 1][y] == "#":
                bugCount += 1
            if x - 1 >= 0 and grid[x - 1][y] == "#":
                bugCount += 1
            if y + 1 < 5 and grid[x][y + 1] == "#":
                bugCount += 1
            if y - 1 >= 0 and grid[x][y - 1] == "#":
                bugCount += 1
            if grid[x][y] == "#" and bugCount != 1:
                newGrid[x][y] = "."
            elif bugCount > 0 and bugCount < 3:
                newGrid[x][y] = "#"

    grid = newGrid
    if grid not in allGrids:
        allGrids.append(grid)
    else:
        break

for x in grid:
    for y in x:
        if y == "#":
            biodiversityRating += pow(2, indx)
        indx += 1

print(biodiversityRating)
