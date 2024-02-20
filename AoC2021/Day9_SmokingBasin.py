#Part 1 Solution
f1 = open("day9.txt")
fullMap = []
lowPoints = []

for line in f1:
    map = list(line.strip())
    for indx, val in enumerate(map):
        map[indx] = int(val)
    fullMap.append(map)

for indxI, val in enumerate(fullMap):
    for indxJ, v in enumerate(fullMap[indxI]):
        scoreCard = []

        if indxJ + 1 < len(fullMap[indxI]) and v >= fullMap[indxI][indxJ + 1]:
            scoreCard.append(False)
        if indxJ - 1 >= 0 and v >= fullMap[indxI][indxJ - 1]:
            scoreCard.append(False)
        if indxI + 1 < len(fullMap) and v >= fullMap[indxI + 1][indxJ]:
            scoreCard.append(False)
        if indxI - 1 >= 0 and v >= fullMap[indxI - 1][indxJ]:
            scoreCard.append(False)

        if False not in scoreCard:
            lowPoints.append(v)

riskLevel = sum(lowPoints) + len(lowPoints)
print(riskLevel)

#Part 2 Solution
f1 = open("day9.txt")
fullMap = []
queue = []
basins = dict()
visited = set()
basinCount = 0

for line in f1:
    map = list(line.strip())
    for indx, val in enumerate(map):
        map[indx] = int(val)
    fullMap.append(map)

for indxI, val in enumerate(fullMap):
    for indxJ, v in enumerate(fullMap[indxI]):
        scoreCard = []

        if indxJ + 1 < len(fullMap[indxI]) and v >= fullMap[indxI][indxJ + 1]:
            scoreCard.append(False)
        if indxJ - 1 >= 0 and v >= fullMap[indxI][indxJ - 1]:
            scoreCard.append(False)
        if indxI + 1 < len(fullMap) and v >= fullMap[indxI + 1][indxJ]:
            scoreCard.append(False)
        if indxI - 1 >= 0 and v >= fullMap[indxI - 1][indxJ]:
            scoreCard.append(False)

        if False not in scoreCard:
            queue.append(((indxI, indxJ), basinCount))
            basinCount += 1 

while queue:
    coord, basinNum = queue.pop(0)
    visited.add(tuple(coord))

    if basinNum in basins:
        basins[basinNum].append(fullMap[coord[0]][coord[1]])
    else:
        basins[basinNum] = [fullMap[coord[0]][coord[1]]]

    if coord[1] + 1 < len(fullMap[coord[0]]) and fullMap[coord[0]][coord[1] + 1] != 9 and (coord[0], coord[1] + 1) not in visited:
        queue.append(((coord[0], coord[1] + 1), basinNum))
        visited.add((coord[0], coord[1] + 1))
    if coord[1] - 1 >= 0 and fullMap[coord[0]][coord[1] - 1] != 9 and (coord[0], coord[1] - 1) not in visited:
        queue.append(((coord[0], coord[1] - 1), basinNum))
        visited.add((coord[0], coord[1] - 1))
    if coord[0] + 1 < len(fullMap) and fullMap[coord[0] + 1][coord[1]] != 9 and (coord[0] + 1, coord[1]) not in visited:
        queue.append(((coord[0] + 1, coord[1]), basinNum))
        visited.add((coord[0] + 1, coord[1]))
    if coord[0] - 1 >= 0 and fullMap[coord[0] - 1][coord[1]] != 9 and (coord[0] - 1, coord[1]) not in visited:
        queue.append(((coord[0] - 1, coord[1]), basinNum))
        visited.add((coord[0] - 1, coord[1]))

basinSize = [len(x) for x in basins.values()]
basinSize.sort()
basinSize = basinSize[::-1]

print(basinSize[0] * basinSize[1] * basinSize[2])