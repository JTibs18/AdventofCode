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

for


#find low points
#find points around low pounts (above, below, left, right)
#not including low point, test if surround points are low points
#if a low point, add surrounding points to queue to test
