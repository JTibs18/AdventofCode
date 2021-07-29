#Part 1 Solution
f1 = open("day2.txt")
for line in f1:
    line = line.strip("/n").split(",")

line[1] = 12
line[2] = 2
indx = 0

while int(line[indx]) != 99:
    pos1 = int(line[indx + 1])
    pos2 = int(line[indx + 2])
    placement = int(line[indx + 3])

    if int(line[indx]) == 1:
        s = int(line[pos1]) + int(line[pos2])
        line[placement] = s
    elif int(line[indx]) == 2:
        s = int(line[pos1]) * int(line[pos2])
        line[placement] = s

    indx += 4

print(line[0])

#Part 2 Solution
line1 = 0
line2 = 0
line[1] = line1
line[2] = line2

while True:

    f1 = open("day2.txt")
    for line in f1:
        line = line.strip("/n").split(",")

    indx = 0

    if line2 < len(line) - 1:
        line2 += 1
        line[2] = line2
        line[1] = line1
    else:
        line1 += 1
        line2 = 0
        line[1] = line1
        line[2] = line2

    while int(line[indx]) != 99:
        pos1 = int(line[indx + 1])
        pos2 = int(line[indx + 2])
        placement = int(line[indx + 3])

        if int(line[indx]) == 1:
            s = int(line[pos1]) + int(line[pos2])
            line[placement] = s
        elif int(line[indx]) == 2:
            s = int(line[pos1]) * int(line[pos2])
            line[placement] = s

        indx += 4

    if int(line[0]) == 19690720:
        print(100 * line[1] + line[2])
        break
