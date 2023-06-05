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