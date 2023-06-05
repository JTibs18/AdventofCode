#Part 1 Solution

f1 = open("day15.txt")

tmpG = []
rowCount = 0

for line in f1:
    tempRow = []
    # num = int(line)
    rowCount += 1
    num = list(line)
    for x in num:
        if x != '\n':
            tempRow.append(int(x))
    tmpG.extend(tempRow)
    colCount = len(tempRow)


grid = [[0 for x in range(colCount)] for y in range(rowCount)]
rCount = 0
cCount = 0

for element in tmpG:
    if cCount == colCount:
        rCount += 1
        cCount = 0
        grid[rCount][cCount] = element
        cCount += 1
    else:
        grid[rCount][cCount] = element
        cCount += 1

print(grid, cCount, rCount)

goal = (cCount - 1, rCount - 1)
start = (0, 0)
