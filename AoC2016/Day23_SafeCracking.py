#Part 1 Solution
f1 = open("day23.txt")

instructions = []
registers = {"a": 7, "b": 0, "c": 0, "d": 0}
instructionNumber = 0

for line in f1:
    instructions.append(line.strip().split(" "))

while instructionNumber < len(instructions): 
    if instructions[instructionNumber][0] == "cpy":
        if instructions[instructionNumber][1].strip("-").isnumeric(): 
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
    elif instructions[instructionNumber][0] == "tgl": 
        offset = registers[instructions[instructionNumber][1]] + instructionNumber

        if offset >= len(instructions): 
            instructionNumber += 1 
            continue 
        
        if instructions[offset][0] == "inc": 
            instructions[offset][0] = "dec"
        elif len(instructions[offset]) == 2: 
            instructions[offset][0] = "inc"
        elif instructions[offset][0] == "jnz":
            instructions[offset][0] = "cpy"
        elif len(instructions[offset]) == 3: 
            instructions[offset][0] = "jnz"
        
        instructionNumber += 1 

    else: 
        if (instructions[instructionNumber][1].isnumeric() and int(instructions[instructionNumber][1]) != 0) or registers[instructions[instructionNumber][1]] != 0:
            if instructions[instructionNumber][2].strip("-").isnumeric(): 
                instructionNumber += int(instructions[instructionNumber][2])
            else: 
                instructionNumber += registers[instructions[instructionNumber][2]]
        else: 
            instructionNumber += 1
    
print(registers["a"])

#Part 2 Solution
f1 = open("day23.txt")

instructions = []
registers = {"a": 12, "b": 0, "c": 0, "d": 0}
instructionNumber = 0

for line in f1:
    instructions.append(line.strip().split(" "))

while instructionNumber < len(instructions): 
    if instructions[instructionNumber][0] == "cpy":
        if instructions[instructionNumber][1].strip("-").isnumeric(): 
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
    elif instructions[instructionNumber][0] == "tgl": 
        offset = registers[instructions[instructionNumber][1]] + instructionNumber

        if offset >= len(instructions): 
            instructionNumber += 1 
            continue 
        
        if instructions[offset][0] == "inc": 
            instructions[offset][0] = "dec"
        elif len(instructions[offset]) == 2: 
            instructions[offset][0] = "inc"
        elif instructions[offset][0] == "jnz":
            instructions[offset][0] = "cpy"
        elif len(instructions[offset]) == 3: 
            instructions[offset][0] = "jnz"
        
        instructionNumber += 1 

    else: 
        if (instructions[instructionNumber][1].isnumeric() and int(instructions[instructionNumber][1]) != 0) or registers[instructions[instructionNumber][1]] != 0:
            if instructions[instructionNumber][2].strip("-").isnumeric(): 
                instructionNumber += int(instructions[instructionNumber][2])
            else: 
                instructionNumber += registers[instructions[instructionNumber][2]]
        else: 
            instructionNumber += 1
    
print(registers["a"])

# need to do some sort of optimization https://www.reddit.com/r/adventofcode/comments/7dvao2/2016_day_23_part_2_getting_an_infinite_loop/