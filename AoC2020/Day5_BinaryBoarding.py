#Part 1 Solution
import math
f1 = open("day5.txt")
nums = []
highestID = 0

for line in f1:
    minRow = 0
    maxRow = 127
    row = 0
    minCol = 0
    maxCol = 7
    col = 0
    sID = 0

    line = line.rstrip()
    nums.append(line)

    for count, i in enumerate(line):
        if i == "F" and count < 7:
            maxRow = math.floor((minRow + maxRow)/2)
            minRow = minRow
            if count == 6:
                row = minRow
        elif i == "B" and count < 7:
            minRow = math.ceil((minRow + maxRow)/2)
            maxRow = maxRow
            if count == 6:
                row = maxRow
        elif i == "L" and count > 6:
            maxCol = math.floor((minCol + maxCol)/2)
            minCol = minCol
            if count == 9:
                col = minCol
        elif i == "R" and count > 6:
            minCol = math.ceil((minCol + maxCol)/2)
            maxCol = maxCol
            if count == 9:
                col = maxCol

    sID = (row * 8) + col

    if sID > highestID:
        highestID = sID

print (highestID)


#Part 2 Solution
import math
f1 = open("day5.txt")
nums = []
seatIDs = []

for line in f1:
    minRow = 0
    maxRow = 127
    row = 0
    minCol = 0
    maxCol = 7
    col = 0
    sID = 0

    line = line.rstrip()
    nums.append(line)

    for count, i in enumerate(line):
        if i == "F" and count < 7:
            maxRow = math.floor((minRow + maxRow)/2)
            minRow = minRow
            if count == 6:
                row = minRow
        elif i == "B" and count < 7:
            minRow = math.ceil((minRow + maxRow)/2)
            maxRow = maxRow
            if count == 6:
                row = maxRow
        elif i == "L" and count > 6:
            maxCol = math.floor((minCol + maxCol)/2)
            minCol = minCol
            if count == 9:
                col = minCol
        elif i == "R" and count > 6:
            minCol = math.ceil((minCol + maxCol)/2)
            maxCol = maxCol
            if count == 9:
                col = maxCol

    sID = (row * 8) + col
    seatIDs.append(sID)
seatIDs.sort()

for count, ID in enumerate(seatIDs):
    if count == 0:
        temp = ID
    if count > 0 and count < (len(seatIDs) - 1):
        if (temp != ID):
                print(ID - 1)
                break

    temp = temp + 1
