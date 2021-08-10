#Part 1 Solution
f1 = open("day7.txt")

for line in f1:
    line = line.strip("/n").split(",")

possibleNums = "01234"
phasePerms = []

def permutations(s, step):
    if step == len(s):
        if s not in phasePerms:
            phasePerms.append(s)

    for i in range(step, len(s)):
        sCopy = [x for x in s]
        sCopy[step], sCopy[i] = sCopy[i], sCopy[step]
        permutations(sCopy, step + 1)

permutations(possibleNums, 0)
outputSigs = []

for phase in phasePerms:
    transferNum = 0

    for p in range(5):
        inputNum = 0
        indx = 0

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
                if index == 2:
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
                if inputNum == 0:
                    line[int(line[indx + 1])] = phase[p]
                    inputNum += 1
                elif inputNum != 0 and p == 0:
                    line[int(line[indx + 1])] = 0
                else:
                    line[int(line[indx + 1])] = str(transferNum)
                indx += 2
            elif '4' in opcode:
                transferNum = values[0]
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
    outputSigs.append(transferNum)

print(max(outputSigs))

#Part 2 Solution
f1 = open("day7.txt")
for line in f1:
    line = line.strip("/n").split(",")

possibleNums = "56789"
phasePerms = []
outputSigs = []

def permutations(s, step):
    if step == len(s):
        if s not in phasePerms:
            phasePerms.append(s)

    for i in range(step, len(s)):
        sCopy = [x for x in s]
        sCopy[step], sCopy[i] = sCopy[i], sCopy[step]
        permutations(sCopy, step + 1)

permutations(possibleNums, 0)

for phase in phasePerms:
    transferNum = 0
    inputNum = [0, 0, 0, 0, 0]
    lastIndx = [0, 0, 0, 0, 0]
    ampLine = [line[:], line[:], line[:], line[:], line[:]]
    indx = 0
    amp = 0

    while int(ampLine[4][indx]) != 99:
        if len(ampLine[amp][indx]) > 2:
            instructions = ampLine[amp][indx][:-2][::-1]
            opcode = ampLine[amp][indx][-2:]
        else:
            opcode = ampLine[amp][indx]
            instructions = []

        values = []
        
        if '1' in opcode or '2' in opcode or '7' in opcode or '8' in opcode:
            iter = 3
        elif '5' in opcode or '6' in opcode:
            iter = 2
        else:
            iter = 1

        for index in range(iter):
            if index == 2:
                values.append(int(ampLine[amp][indx + index + 1]))
            elif len(instructions) > index and instructions[index] == '1':
                values.append(int(ampLine[amp][indx + index + 1]))
            else:
                pos = int(ampLine[amp][index + indx + 1])
                values.append(int(ampLine[amp][pos]))

        if '1' in opcode:
            s = values[0] + values[1]
            ampLine[amp][values[2]] = str(s)
            indx += 4
        elif '2' in opcode:
            s = values[0] * values[1]
            ampLine[amp][values[2]] = str(s)
            indx += 4
        elif '3' in opcode:
            if inputNum[amp] == 0:
                ampLine[amp][int(ampLine[amp][indx + 1])] = phase[amp]
                inputNum[amp] = 1
                indx += 2
            elif inputNum[amp] == 1:
                ampLine[amp][int(ampLine[amp][indx + 1])] = str(transferNum)
                indx += 2
                inputNum[amp] = 2
            elif inputNum[amp] == 2:
                lastIndx[amp] = indx
                inputNum[amp] = -1
                amp += 1
                if amp == 5:
                    amp = 0
                indx = lastIndx[amp]
            else:
                ampLine[amp][int(ampLine[amp][indx + 1])] = str(transferNum)
                inputNum[amp] = 2
                indx += 2
        elif '4' in opcode:
            transferNum = values[0]
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
                ampLine[amp][values[2]] = str(1)
            else:
                ampLine[amp][values[2]] = str(0)
            indx += 4
        elif '8' in opcode:
            if values[0] == values[1]:
                ampLine[amp][values[2]] = str(1)
            else:
                ampLine[amp][values[2]] = str(0)
            indx += 4

        if int(ampLine[amp][indx]) == 99 and amp < 4:
            amp += 1
            if amp == 5:
                amp = 0
            indx = lastIndx[amp]

    outputSigs.append(transferNum)

print(max(outputSigs))
