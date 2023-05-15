# Part 1 Solution
f1 = open("day12.txt")

instructions = []
registers = {"a": 0, "b": 0, "c": 0, "d": 0}
instructionNumber = 0

for line in f1:
    instructions.append(line.strip().split(" "))

while instructionNumber < len(instructions): 
    if instructions[instructionNumber][0] == "cpy":
        if instructions[instructionNumber][1].isnumeric(): 
            registers[instructions[instructionNumber][2]] = int(instructions[instructionNumber][1])
        else: 
            registers[instructions[instructionNumber][2]] = registers[instructions[instructionNumber][1]]
        instructionNumber += 1
    elif instructions[instructionNumber][0] == "inc": 
        registers[instructions[instructionNumber][1]] += 1
        instructionNumber += 1
    elif instructions[instructionNumber][0] == "dec": 
        registers[instructions[instructionNumber][1]] -= 1
        instructionNumber += 1 
    else: 
        if (instructions[instructionNumber][1].isnumeric() and int(instructions[instructionNumber][1]) != 0) or registers[instructions[instructionNumber][1]] != 0:
            instructionNumber += int(instructions[instructionNumber][2])
        else: 
            instructionNumber += 1
    
print(registers["a"])

# Part 2 Solution
f1 = open("day12.txt")

instructions = []
registers = {"a": 0, "b": 0, "c": 1, "d": 0}
instructionNumber = 0

for line in f1:
    instructions.append(line.strip().split(" "))

while instructionNumber < len(instructions): 
    if instructions[instructionNumber][0] == "cpy":
        if instructions[instructionNumber][1].isnumeric(): 
            registers[instructions[instructionNumber][2]] = int(instructions[instructionNumber][1])
        else: 
            registers[instructions[instructionNumber][2]] = registers[instructions[instructionNumber][1]]
        instructionNumber += 1
    elif instructions[instructionNumber][0] == "inc": 
        registers[instructions[instructionNumber][1]] += 1
        instructionNumber += 1
    elif instructions[instructionNumber][0] == "dec": 
        registers[instructions[instructionNumber][1]] -= 1
        instructionNumber += 1 
    else: 
        if (instructions[instructionNumber][1].isnumeric() and int(instructions[instructionNumber][1]) != 0) or registers[instructions[instructionNumber][1]] != 0:
            instructionNumber += int(instructions[instructionNumber][2])
        else: 
            instructionNumber += 1
    
print(registers["a"])
