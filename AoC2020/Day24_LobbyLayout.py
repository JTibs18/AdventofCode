# Part 1 Solution
f1 = open("day24.txt")

flippedTiles = dict()
blackCount = 0 

for line in f1:
    directions = line.strip()
    ptr1 = 0 
    curTileX = 0 
    curTileY = 0 

    while ptr1 < len(directions): 
        if directions[ptr1] == "e":
            curTileX += 1
            ptr1 += 1
        elif directions[ptr1] == "w": 
            curTileX -= 1
            ptr1 += 1
        elif directions[ptr1] == "s" and directions[ptr1 + 1] == "w":
            curTileX -= 0.5
            curTileY -= 1
            ptr1 += 2
        elif directions[ptr1] == "s" and directions[ptr1 + 1] == "e": 
            curTileX += 0.5
            curTileY -= 1 
            ptr1 += 2
        elif directions[ptr1] == "n" and directions[ptr1 + 1] == "w":
            curTileX -= 0.5 
            curTileY += 1
            ptr1 += 2
        elif directions[ptr1] == "n" and directions[ptr1 + 1] == "e": 
            curTileX += 0.5
            curTileY += 1 
            ptr1 += 2

    if (curTileX, curTileY) in flippedTiles: 
        if flippedTiles[(curTileX, curTileY)] == 0: 
            flippedTiles[(curTileX, curTileY)] = 1
        else: 
            flippedTiles[(curTileX, curTileY)] = 0
    else: 
        flippedTiles[(curTileX, curTileY)] = 0

for color in flippedTiles.values(): 
    if color == 0: 
        blackCount += 1 

print(blackCount)

# Part 2 Solution (takes about 30 seconds to run)
import copy

f1 = open("day24.txt")

flippedTiles = dict()
blackTilesAfterDays = 0 
maxX = 0
maxY = 0 
minX = 0 
minY = 0 

# parsing input, getting initial floor layout
for line in f1:
    directions = line.strip()
    ptr1 = 0 
    curTileX = 0 
    curTileY = 0 

    while ptr1 < len(directions): 
        if directions[ptr1] == "e":
            curTileX += 1
            ptr1 += 1
        elif directions[ptr1] == "w": 
            curTileX -= 1
            ptr1 += 1
        elif directions[ptr1] == "s" and directions[ptr1 + 1] == "w":
            curTileX -= 0.5
            curTileY -= 1
            ptr1 += 2
        elif directions[ptr1] == "s" and directions[ptr1 + 1] == "e": 
            curTileX += 0.5
            curTileY -= 1 
            ptr1 += 2
        elif directions[ptr1] == "n" and directions[ptr1 + 1] == "w":
            curTileX -= 0.5 
            curTileY += 1
            ptr1 += 2
        elif directions[ptr1] == "n" and directions[ptr1 + 1] == "e": 
            curTileX += 0.5
            curTileY += 1 
            ptr1 += 2
            
    if (curTileX, curTileY) in flippedTiles: 
        if flippedTiles[(curTileX, curTileY)] == 0: 
            flippedTiles[(curTileX, curTileY)] = 1
        else: 
            flippedTiles[(curTileX, curTileY)] = 0
    else: 
        flippedTiles[(curTileX, curTileY)] = 0

# finding the range of floor tiles
for x, y in flippedTiles.keys():  
    if x < minX: 
        minX = x 
    
    if x > maxX: 
        maxX = x 

    if y < minY: 
        minY = y
    
    if y > maxY: 
        maxY = y 
    
    if minX % 1 == 0: 
        minX -= 1.5 

    if maxX % 1 == 0: 
        maxX += 1.5 

# simulating flipping tiles each day
for day in range(0, 100): 
    minX -= 1 
    maxX += 1 
    minY -= 1
    maxY += 1

    # filling in white tiles that are not accounted for (border and internal)
    for x in range(int(minX) - 1, int(maxX) + 1):
        for y in range(minY - 1, maxY + 1): 
            if y % 2 != 0: 
                xCoord = x + 0.5
            else: 
                xCoord = x 

            if (xCoord, y) not in flippedTiles: 
                flippedTiles[(xCoord, y)] = 1 

    tempFlippedTiles = copy.deepcopy(flippedTiles)

    # iterating through each tile and deciding whether to flip 
    for key, value in flippedTiles.items():
        blackCount = 0 

        if (key[0] + 0.5, key[1] + 1) in flippedTiles: 
            if flippedTiles[(key[0] + 0.5, key[1] + 1)] == 0: 
                blackCount += 1 
         
        if (key[0] + 1, key[1]) in flippedTiles:
            if flippedTiles[(key[0] + 1, key[1])] == 0: 
                blackCount += 1
        
        if (key[0] + 0.5, key[1] - 1) in flippedTiles:
            if flippedTiles[(key[0] + 0.5, key[1] - 1)] == 0: 
                blackCount += 1

        if (key[0] - 0.5, key[1] - 1) in flippedTiles:
            if flippedTiles[(key[0] - 0.5, key[1] - 1)] == 0: 
                blackCount += 1

        if (key[0] - 1, key[1]) in flippedTiles:
            if flippedTiles[(key[0] - 1, key[1])] == 0: 
                blackCount += 1

        if (key[0] - 0.5, key[1] + 1) in flippedTiles:
            if flippedTiles[(key[0] - 0.5, key[1] + 1)] == 0: 
                blackCount += 1

        if (blackCount == 0 or blackCount > 2) and value == 0: 
            tempFlippedTiles[key] = 1

        if blackCount == 2 and value == 1: 
            tempFlippedTiles[key] = 0

    flippedTiles = copy.deepcopy(tempFlippedTiles)

# counting and displaying the number of black tiles after day 100
for color in flippedTiles.values(): 
    if color == 0: 
        blackTilesAfterDays += 1 

print(blackTilesAfterDays)