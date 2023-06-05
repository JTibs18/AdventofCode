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
    
    if instructions[instructionPtr][0] == "jgz" and int(registers[instructions[instructionPtr][1]]) > 0:
        instructionPtr += instruction2
    else: 
        instructionPtr += 1      

