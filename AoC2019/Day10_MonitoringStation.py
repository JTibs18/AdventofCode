#Part 1 Solution
f1 = open("day10.txt")

detectedA = []
aLocations = []
surroundingA = dict()

for line in f1:
    line = line.strip("/n").split(",")
    detectedA.append(line)

for indx, x in enumerate(detectedA):
    for j, y in enumerate(x[0]):
        if y == "#":
            aLocations.append((j, indx))

for a in aLocations:
    aSlopes1 = set()
    aSlopes2 = set()
    specialCaseX = set()
    specialCaseY = set()
    for aster in aLocations:
        if a != aster:
            if aster[0] - a[0] == 0:
                if a[1] > aster[1]:
                    specialCaseX.add( -1 * aster[0])
                else:
                    specialCaseX.add(aster[0])
            elif aster[1] - a[1] == 0:
                if a[0] > aster[0]:
                    specialCaseY.add( -1 * aster[1])
                else:
                    specialCaseY.add(aster[1])
            else:
                slope = ((aster[1] - a[1]) / (aster[0] - a[0]))
                if aster[1] > a[1]:
                    aSlopes2.add(slope)
                else:
                    aSlopes1.add(slope)

    surroundingA[a] = len(aSlopes1) + len(aSlopes2) + len(specialCaseX) + len(specialCaseY)

print(max(surroundingA.values()))

#Part 2 Solution
f1 = open("day10.txt")

detectedA = []
aLocations = []
surroundingA = dict()

for line in f1:
    line = line.strip("/n").split(",")
    detectedA.append(line)

for indx, x in enumerate(detectedA):
    for j, y in enumerate(x[0]):
        if y == "#":
            aLocations.append((j, indx))
poiX = 11
poiY = 13


aSlopes1 = dict()
aSlopes2 = dict()
specialCaseX = dict()
specialCaseY = dict()
for aster in aLocations:
    if (poiX, poiY) != aster:
        if aster[0] - poiX == 0:
            #ADD TO DICT HERE
        #     if poiY > aster[1]:
        #         specialCaseX.add( -1 * aster[0])
        #     else:
        #         specialCaseX.add(aster[0])
        # elif aster[1] - poiY == 0:
        #     if poiX > aster[0]:
        #         specialCaseY.add( -1 * aster[1])
        #     else:
        #         specialCaseY.add(aster[1])
        # else:
        #     slope = ((aster[1] - poiY) / (aster[0] -poiX))
        #     if aster[1] > poiY:
        #         aSlopes2.add(slope)
        #     else:
        #         aSlopes1.add(slope)
