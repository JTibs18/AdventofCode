#Part 1 Solution
f1 = open("day5.txt")

board = {}

for line in f1:
    line = line.strip("\n").split("->")

    coords = []

    for indx, val in enumerate(line):
        coords.append(line[indx].strip().split(","))

    if int(coords[0][0]) == int(coords[1][0]):
        if int(coords[0][1]) < int(coords[1][1]):
            cur = int(coords[0][1])
            while cur <= int(coords[1][1]):
                if (int(coords[0][0]), cur) not in board:
                    board[(int(coords[0][0]), cur)] = 1
                else:
                    board[(int(coords[0][0]), cur)] += 1
                cur += 1
        else:
            cur = int(coords[1][1])
            while cur <= int(coords[0][1]):
                if (int(coords[0][0]), cur) not in board:
                    board[(int(coords[0][0]), cur)] = 1
                else:
                    board[(int(coords[0][0]), cur)] += 1
                cur += 1
    elif int(coords[0][1]) == int(coords[1][1]):
        if int(coords[0][0]) < int(coords[1][0]):
            cur = int(coords[0][0])
            while cur <= int(coords[1][0]):
                if (cur, int(coords[0][1])) not in board:
                    board[(cur, int(coords[0][1]))] = 1
                else:
                    board[(cur, int(coords[0][1]))] += 1
                cur += 1
        else:
            cur = int(coords[1][0])
            while cur <= int(coords[0][0]):
                if (cur, int(coords[0][1]))  not in board:
                    board[(cur, int(coords[0][1]))] = 1
                else:
                    board[(cur, int(coords[0][1])) ] += 1
                cur += 1
count = 0
for key, val in board.items():
    if val >= 2:
        count += 1
print(count)

#Part 2 Solution
f1 = open("day5.txt")

board = {}

for line in f1:
    line = line.strip("\n").split("->")

    coords = []

    for indx, val in enumerate(line):
        coords.append(line[indx].strip().split(","))
    if int(coords[0][0]) == int(coords[1][0]):
        if int(coords[0][1]) < int(coords[1][1]):
            cur = int(coords[0][1])
            while cur <= int(coords[1][1]):
                if (int(coords[0][0]), cur) not in board:
                    board[(int(coords[0][0]), cur)] = 1
                else:
                    board[(int(coords[0][0]), cur)] += 1
                cur += 1
        else:
            cur = int(coords[1][1])
            while cur <= int(coords[0][1]):
                if (int(coords[0][0]), cur) not in board:
                    board[(int(coords[0][0]), cur)] = 1
                else:
                    board[(int(coords[0][0]), cur)] += 1
                cur += 1

    elif int(coords[0][1]) == int(coords[1][1]):
        if int(coords[0][0]) < int(coords[1][0]):
            cur = int(coords[0][0])
            while cur <= int(coords[1][0]):
                if (cur, int(coords[0][1])) not in board:
                    board[(cur, int(coords[0][1]))] = 1
                else:
                    board[(cur, int(coords[0][1]))] += 1
                cur += 1
        else:
            cur = int(coords[1][0])
            while cur <= int(coords[0][0]):
                if (cur, int(coords[0][1])) not in board:
                    board[(cur, int(coords[0][1]))] = 1
                else:
                    board[(cur, int(coords[0][1])) ] += 1
                cur += 1
    else:
        curX = int(coords[0][0])
        curY = int(coords[0][1])
        limX = int(coords[1][0])
        limY = int(coords[1][1])

        if int(coords[0][0]) < int(coords[1][0]):
            incX = True
        else:
            incX = False
        if int(coords[0][1]) < int(coords[1][1]):
            incY = True
        else:
            incY = False

        stop = False
        while stop == False:
            if (curX, curY) not in board:
                board[(curX, curY)] = 1
            else:
                board[(curX, curY)] += 1

            if incX == True:
                curX += 1
            else:
                curX -= 1
            if incY == True:
                curY += 1
            else:
                curY -= 1

            if curX == limX or curY == limY:
                stop = True
                if (curX, curY)  not in board:
                    board[(curX, curY)] = 1
                else:
                    board[(curX, curY)] += 1

count = 0
for key, val in board.items():
    if val >= 2:
        count += 1
print(count)
