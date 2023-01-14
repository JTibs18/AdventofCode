# Part 1 Solution
f1 = open("day23.txt")
instructions = []
curInstructionIndx = 0 
a = 0
b = 0

for line in f1:
    parsedInstruction = line.strip().split(" ")
    instructions.append(parsedInstruction)

while curInstructionIndx < len(instructions): 
    curInstruction = instructions[curInstructionIndx]
    
    if curInstruction[0] == 'hlf':
        if curInstruction[1][0] == "a": 
            a = a / 2 
        else: 
            b = b / 2 
        curInstructionIndx += 1
    elif curInstruction[0] == 'tpl':
        if curInstruction[1][0] == "a": 
            a = a * 3 
        else: 
            b = b * 3
        curInstructionIndx += 1
    elif curInstruction[0] == "inc": 
        if curInstruction[1][0] == "a": 
            a += 1 
        else: 
            b += 1
        curInstructionIndx += 1
    elif curInstruction[0] == "jmp":
        offset = int(curInstruction[1])
        curInstructionIndx += offset 
    elif curInstruction[0] == "jie":
        if curInstruction[1][0] == "a": 
            if a % 2 == 0: 
                offset = int(curInstruction[2])
                curInstructionIndx += offset
            else: 
                curInstructionIndx += 1 
        else: 
            if b % 2 == 0: 
                offset = int(curInstruction[2])
                curInstructionIndx += offset
            else: 
                curInstructionIndx += 1 
    else: 
        if curInstruction[1][0] == "a": 
            if a == 1: 
                offset = int(curInstruction[2])
                curInstructionIndx += offset
            else: 
                curInstructionIndx += 1 
        else: 
            if b == 1: 
                offset = int(curInstruction[2])
                curInstructionIndx += offset
            else: 
                curInstructionIndx += 1 

print(b)

# Part 2 Solution
f1 = open("day23.txt")
instructions = []
curInstructionIndx = 0 
a = 1
b = 0

for line in f1:
    parsedInstruction = line.strip().split(" ")
    instructions.append(parsedInstruction)

while curInstructionIndx < len(instructions): 
    curInstruction = instructions[curInstructionIndx]
    
    if curInstruction[0] == 'hlf':
        if curInstruction[1][0] == "a": 
            a = a / 2 
        else: 
            b = b / 2 
        curInstructionIndx += 1
    elif curInstruction[0] == 'tpl':
        if curInstruction[1][0] == "a": 
            a = a * 3 
        else: 
            b = b * 3
        curInstructionIndx += 1
    elif curInstruction[0] == "inc": 
        if curInstruction[1][0] == "a": 
            a += 1 
        else: 
            b += 1
        curInstructionIndx += 1
    elif curInstruction[0] == "jmp":
        offset = int(curInstruction[1])
        curInstructionIndx += offset 
    elif curInstruction[0] == "jie":
        if curInstruction[1][0] == "a": 
            if a % 2 == 0: 
                offset = int(curInstruction[2])
                curInstructionIndx += offset
            else: 
                curInstructionIndx += 1 
        else: 
            if b % 2 == 0: 
                offset = int(curInstruction[2])
                curInstructionIndx += offset
            else: 
                curInstructionIndx += 1 
    else: 
        if curInstruction[1][0] == "a": 
            if a == 1: 
                offset = int(curInstruction[2])
                curInstructionIndx += offset
            else: 
                curInstructionIndx += 1 
        else: 
            if b == 1: 
                offset = int(curInstruction[2])
                curInstructionIndx += offset
            else: 
                curInstructionIndx += 1 

print(b)