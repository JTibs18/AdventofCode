#Part 1 Solution
f1 = open("day12.txt")

vertical = 0
horizontal = 0
facingDirection = "E"
facingDirNum = 0

for line in f1:
    if line[0] == "F":
        curDirection = facingDirection
    elif line[0] != "L" and line[0] != "R" :
        curDirection = line[0]

    if line[0] == "R" or line[0] == "L":
        turnDeg = int(line[1: len(line) - 1]) / 90

        if line[0] == "R":
            facingDirNum += turnDeg
        else:
            facingDirNum -= turnDeg

        facingDirNum = facingDirNum % 4

        if facingDirNum == 0:
            curDirection = "E"
            facingDirection = "E"
        elif facingDirNum == 1:
            curDirection = "S"
            facingDirection = "S"
        elif facingDirNum == 2:
            curDirection = "W"
            facingDirection = "W"
        else:
            curDirection = "N"
            facingDirection = "N"
    elif curDirection == "N":
        vertical += int(line[1: len(line) - 1])
    elif curDirection == "E":
        horizontal += int(line[1: len(line) + 1])
    elif curDirection == "S":
        vertical -= int(line[1: len(line) + 1])
    elif curDirection == "W":
        horizontal -= int(line[1: len(line) + 1])

print(abs(horizontal) + abs(vertical))

#Part 2 Solution
f1 = open("day12.txt")

vertical = 0
horizontal = 0
wayPointX = 10
wayPointY = 1

for line in f1:
    if line[0] != "L" and line[0] != "R" and line[0] != "F":
        curDirection = line[0]

    if line[0] == "F":
        horizontal += wayPointX * int(line[1: len(line) - 1])
        vertical += wayPointY * int(line[1: len(line) - 1])
    elif line[0] == "R" or line[0] == "L":
        turnDeg = int(line[1: len(line) - 1]) / 90

        if (line[0] == "R" and turnDeg == 1) or (line[0] == "L" and turnDeg == 3):
            newDir = -1 * wayPointX
            wayPointX = wayPointY
            wayPointY = newDir
        elif (line[0] == "R" and turnDeg == 3) or (line[0] == "L" and turnDeg == 1):
            newDir = -1 * wayPointY
            wayPointY = wayPointX
            wayPointX = newDir
        else:
            wayPointY = -1 * wayPointY
            wayPointX = -1 * wayPointX
    elif curDirection == "N":
        wayPointY += int(line[1: len(line) - 1])
    elif curDirection == "E":
        wayPointX += int(line[1: len(line) + 1])
    elif curDirection == "S":
        wayPointY -= int(line[1: len(line) + 1])
    elif curDirection == "W":
        wayPointX -= int(line[1: len(line) + 1])

print(abs(horizontal) + abs(vertical))
