# Part 1 Solution 
f1 = open("day18.txt")

lastSound = 0
instructionPtr = 0 
registers = dict() 
instructions = []

for line in f1: 
    instructions.append(line.strip().split(" "))

while instructionPtr < len(instructions): 
    instruction2 = 0 

    if len(instructions[instructionPtr]) == 3 and instructions[instructionPtr][2].strip("-").isnumeric(): 
        instruction2 = int(instructions[instructionPtr][2])
    elif len(instructions[instructionPtr]) == 3: 
        instruction2 = int(registers[instructions[instructionPtr][2]])

    if instructions[instructionPtr][0] == "snd": 
        lastSound = int(registers[instructions[instructionPtr][1]])
    elif instructions[instructionPtr][0] == "set": 
        registers[instructions[instructionPtr][1]] = instruction2
    elif instructions[instructionPtr][0] == "add": 
        registers[instructions[instructionPtr][1]] += instruction2
    elif instructions[instructionPtr][0] == "mul": 
        if instructions[instructionPtr][1] in registers: 
            registers[instructions[instructionPtr][1]] *= instruction2
        else:
            registers[instructions[instructionPtr][1]] = 0
    elif instructions[instructionPtr][0] == "mod": 
        registers[instructions[instructionPtr][1]] = int(registers[instructions[instructionPtr][1]]) % instruction2
    elif instructions[instructionPtr][0] == "rcv" and int(registers[instructions[instructionPtr][1]]) != 0:
        print(lastSound)
        break 
    
    if instructions[instructionPtr][0] == "jgz" and ((instructions[instructionPtr][1].isnumeric() and int(instructions[instructionPtr][1]) > 0) or int(registers[instructions[instructionPtr][1]]) > 0):
        instructionPtr += instruction2
    else: 
        instructionPtr += 1      

# Part 2 Solution 
f1 = open("day18.txt")

deadlockCount = 0 
programOneSentValueCount = 0 
instructions = []
instructionPtr = [0, 0] 
messageQueue = [[], []]
registers = [{"p": 0}, {"p": 1}]  

for line in f1: 
    instructions.append(line.strip().split(" "))

while instructionPtr[0] < len(instructions) and instructionPtr[1] < len(instructions) and deadlockCount < 2: 
    instruction2 = [0, 0] 
    
    for i in range(2): 
        if len(instructions[instructionPtr[i]]) == 3 and instructions[instructionPtr[i]][2].strip("-").isnumeric(): 
            instruction2[i] = int(instructions[instructionPtr[i]][2])
        elif len(instructions[instructionPtr[i]]) == 3: 
            instruction2[i] = int(registers[i][instructions[instructionPtr[i]][2]])

        if instructions[instructionPtr[i]][0] == "snd": 
            if i == 1: 
                messageQueue[0].append(int(registers[i][instructions[instructionPtr[i]][1]]))
                programOneSentValueCount += 1 
            else:
                messageQueue[1].append(int(registers[i][instructions[instructionPtr[i]][1]]))
        elif instructions[instructionPtr[i]][0] == "set": 
            registers[i][instructions[instructionPtr[i]][1]] = instruction2[i]
        elif instructions[instructionPtr[i]][0] == "add": 
            registers[i][instructions[instructionPtr[i]][1]] += instruction2[i]
        elif instructions[instructionPtr[i]][0] == "mul": 
            if instructions[instructionPtr[i]][1] in registers[i]: 
                registers[i][instructions[instructionPtr[i]][1]] *= instruction2[i]
            else:
                registers[i][instructions[instructionPtr[i]][1]] = 0
        elif instructions[instructionPtr[i]][0] == "mod": 
            registers[i][instructions[instructionPtr[i]][1]] = int(registers[i][instructions[instructionPtr[i]][1]]) % instruction2[i]
        elif instructions[instructionPtr[i]][0] == "rcv":
            if len(messageQueue[i]) > 0:
                val = messageQueue[i].pop(0)
                registers[i][instructions[instructionPtr[i]][1]] = val 
            else: 
                deadlockCount += 1 
                continue  
        
        if instructions[instructionPtr[i]][0] == "jgz" and ((instructions[instructionPtr[i]][1].isnumeric() and int(instructions[instructionPtr[i]][1]) > 0) or int(registers[i][instructions[instructionPtr[i]][1]]) > 0):
            instructionPtr[i] += instruction2[i]
        else: 
            instructionPtr[i] += 1 

        if deadlockCount > 0: 
            deadlockCount -= 1      

print(programOneSentValueCount)