# Part 1 Solution
f1 = open("day9.txt")
for line in f1:
    line = line.strip("/n").split(",")

indx = 0
relativeBase = 0
extraSpace = ['0' for i in range(10000)]
line.extend(extraSpace)

while int(line[indx]) != 99:
    if len(line[indx]) > 2:
        instructions = line[indx][:-2][::-1]
        opcode = line[indx][-2:]
    else:
        opcode = line[indx]
        instructions = []
    values = []

    if '1' in opcode or '2' in opcode or '7' in opcode or '8' in opcode:
        iter = 3
    elif '5' in opcode or '6' in opcode:
        iter = 2
    else:
        iter = 1

    for index in range(iter):
        if len(instructions) > index and instructions[index] == '2':
            pos = int(line[index + indx + 1]) + relativeBase
            if '3' in opcode or index == 2:
                values.append(pos)
            else:
                values.append(int(line[pos]))
        elif index == 2:
            values.append(int(line[indx + index + 1]))
        elif len(instructions) > index and instructions[index] == '1':
            values.append(int(line[indx + index + 1]))
        else:
            pos = int(line[index + indx + 1])
            values.append(int(line[pos]))

    if '1' in opcode:
        s = values[0] + values[1]
        line[values[2]] = str(s)
        indx += 4
    elif '2' in opcode:
        s = values[0] * values[1]
        line[values[2]] = str(s)
        indx += 4
    elif '3' in opcode:
        num = input("Please enter a number: ")
        line[values[0]] = str(num)
        indx += 2
    elif '4' in opcode:
        print(values[0])
        indx += 2
    elif '5' in opcode:
        if values[0] != 0:
            indx = int(values[1])
        else:
            indx += 3
    elif '6' in opcode:
        if values[0] == 0:
            indx = int(values[1])
        else:
            indx += 3
    elif '7' in opcode:
        if values[0] < values[1]:
            line[values[2]] = str(1)
        else:
            line[values[2]] = str(0)
        indx += 4
    elif '8' in opcode:
        if values[0] == values[1]:
            line[values[2]] = str(1)
        else:
            line[values[2]] = str(0)
        indx += 4
    elif '9' in opcode:
        relativeBase += values[0]
        indx += 2

# Part 2 Solution (NO CODE DIFFERENCE. JUST INPUT '2' INSTEAD OF '1')
f1 = open("day9.txt")
for line in f1:
    line = line.strip("/n").split(",")

indx = 0
relativeBase = 0
extraSpace = ['0' for i in range(10000)]
line.extend(extraSpace)

while int(line[indx]) != 99:
    if len(line[indx]) > 2:
        instructions = line[indx][:-2][::-1]
        opcode = line[indx][-2:]
    else:
        opcode = line[indx]
        instructions = []
    values = []

    if '1' in opcode or '2' in opcode or '7' in opcode or '8' in opcode:
        iter = 3
    elif '5' in opcode or '6' in opcode:
        iter = 2
    else:
        iter = 1

    for index in range(iter):
        if len(instructions) > index and instructions[index] == '2':
            pos = int(line[index + indx + 1]) + relativeBase
            if '3' in opcode or index == 2:
                values.append(pos)
            else:
                values.append(int(line[pos]))
        elif index == 2:
            values.append(int(line[indx + index + 1]))
        elif len(instructions) > index and instructions[index] == '1':
            values.append(int(line[indx + index + 1]))
        else:
            pos = int(line[index + indx + 1])
            values.append(int(line[pos]))

    if '1' in opcode:
        s = values[0] + values[1]
        line[values[2]] = str(s)
        indx += 4
    elif '2' in opcode:
        s = values[0] * values[1]
        line[values[2]] = str(s)
        indx += 4
    elif '3' in opcode:
        num = input("Please enter a number: ")
        line[values[0]] = str(num)
        indx += 2
    elif '4' in opcode:
        print(values[0])
        indx += 2
    elif '5' in opcode:
        if values[0] != 0:
            indx = int(values[1])
        else:
            indx += 3
    elif '6' in opcode:
        if values[0] == 0:
            indx = int(values[1])
        else:
            indx += 3
    elif '7' in opcode:
        if values[0] < values[1]:
            line[values[2]] = str(1)
        else:
            line[values[2]] = str(0)
        indx += 4
    elif '8' in opcode:
        if values[0] == values[1]:
            line[values[2]] = str(1)
        else:
            line[values[2]] = str(0)
        indx += 4
    elif '9' in opcode:
        relativeBase += values[0]
        indx += 2
