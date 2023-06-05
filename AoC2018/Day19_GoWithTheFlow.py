# Part 1 Solution 
f1 = open("day19.txt")

ip = 0
regPtr = -1 
instructions = []
register = [0, 0, 0, 0, 0, 0]

# parse input
for line in f1: 
    if regPtr == -1: 
        regPtr = int(line.strip().split(" ")[1])
    else: 
        temp = line.strip().split(" ")
        temp[1] = int(temp[1])
        temp[2] = int(temp[2])
        temp[3] = int(temp[3])
        instructions.append(temp)

# intcode machine functions (opcodes)
def addr(beforeRegisters, instructionValues): 
    after = beforeRegisters[:]
    after[instructionValues[3]] = beforeRegisters[instructionValues[1]] + beforeRegisters[instructionValues[2]]
    return after

def addi(beforeRegisters, instructionValues): 
    after = beforeRegisters[:]
    after[instructionValues[3]] = beforeRegisters[instructionValues[1]] + instructionValues[2]
    return after

def mulr(beforeRegisters, instructionValues):
    after = beforeRegisters[:]
    after[instructionValues[3]] = beforeRegisters[instructionValues[1]] * beforeRegisters[instructionValues[2]]
    return after

def muli(beforeRegisters, instructionValues): 
    after = beforeRegisters[:]
    after[instructionValues[3]] = beforeRegisters[instructionValues[1]] * instructionValues[2]
    return after

def banr(beforeRegisters, instructionValues): 
    after = beforeRegisters[:]
    after[instructionValues[3]] = beforeRegisters[instructionValues[1]] & beforeRegisters[instructionValues[2]]
    return after

def bani(beforeRegisters, instructionValues): 
    after = beforeRegisters[:]
    after[instructionValues[3]] = beforeRegisters[instructionValues[1]] & instructionValues[2]
    return after

def borr(beforeRegisters, instructionValues): 
    after = beforeRegisters[:]
    after[instructionValues[3]] = beforeRegisters[instructionValues[1]] | beforeRegisters[instructionValues[2]]
    return after

def bori(beforeRegisters, instructionValues):
    after = beforeRegisters[:]
    after[instructionValues[3]] = beforeRegisters[instructionValues[1]] | instructionValues[2]
    return after

def setr(beforeRegisters, instructionValues): 
    after = beforeRegisters[:]
    after[instructionValues[3]] = beforeRegisters[instructionValues[1]]
    return after

def seti(beforeRegisters, instructionValues):
    after = beforeRegisters[:]
    after[instructionValues[3]] = instructionValues[1]
    return after

def gtir(beforeRegisters, instructionValues):
    after = beforeRegisters[:]
    if instructionValues[1] > beforeRegisters[instructionValues[2]]: 
        after[instructionValues[3]] = 1
    else:
        after[instructionValues[3]] = 0 
    return after

def gtri(beforeRegisters, instructionValues):
    after = beforeRegisters[:]
    if beforeRegisters[instructionValues[1]] > instructionValues[2]:
        after[instructionValues[3]] = 1
    else: 
        after[instructionValues[3]] = 0 
    return after

def gtrr(beforeRegisters, instructionValues): 
    after = beforeRegisters[:]
    if beforeRegisters[instructionValues[1]] > beforeRegisters[instructionValues[2]]:
        after[instructionValues[3]] = 1
    else: 
        after[instructionValues[3]] = 0 
    return after

def eqir(beforeRegisters, instructionValues): 
    after = beforeRegisters[:]
    if instructionValues[1] == beforeRegisters[instructionValues[2]]:
        after[instructionValues[3]] = 1 
    else:
        after[instructionValues[3]] = 0 
    return after

def eqri(beforeRegisters, instructionValues):
    after = beforeRegisters[:]
    if beforeRegisters[instructionValues[1]] == instructionValues[2]: 
        after[instructionValues[3]] = 1
    else:
        after[instructionValues[3]] = 0 
    return after

def eqrr(beforeRegisters, instructionValues):
    after = beforeRegisters[:]
    if beforeRegisters[instructionValues[1]] == beforeRegisters[instructionValues[2]]:
        after[instructionValues[3]] = 1
    else:
        after[instructionValues[3]] = 0
    return after

# controller to run the instructions 
while ip < len(instructions):
    register[regPtr] = ip 

    if instructions[ip][0] == "addr":
        register = addr(register, instructions[ip])
    elif instructions[ip][0] == "addi": 
        register = addi(register, instructions[ip])
    elif instructions[ip][0] == "mulr":
        register = mulr(register, instructions[ip])
    elif instructions[ip][0] == "muli": 
        register = muli(register, instructions[ip])
    elif instructions[ip][0] == "banr": 
        register = banr(register, instructions[ip])
    elif instructions[ip][0] == "bani": 
        register = bani(register, instructions[ip])
    elif instructions[ip][0] == "borr":
        register = borr(register, instructions[ip])
    elif instructions[ip][0] == "bori":
        register = bori(register, instructions[ip])
    elif instructions[ip][0] == "setr":
        register = setr(register, instructions[ip])
    elif instructions[ip][0] == "seti": 
        register = seti(register, instructions[ip])
    elif instructions[ip][0] == "gtir": 
        register = gtir(register, instructions[ip])
    elif instructions[ip][0] == "gtri": 
        register = gtri(register, instructions[ip])
    elif instructions[ip][0] == "gtrr": 
        register = gtrr(register, instructions[ip])
    elif instructions[ip][0] == "eqir":  
        register = eqir(register, instructions[ip])
    elif instructions[ip][0] == "eqri":
        register = eqri(register, instructions[ip])
    elif instructions[ip][0] == "eqrr": 
        register = eqrr(register, instructions[ip])

    ip = register[regPtr]
    ip += 1 

print(register[0])

# Part 2 Solution 
f1 = open("day19.txt")

ip = 0
regPtr = -1 
instructions = []
register = [1, 0, 0, 0, 0, 0]

# parse input
for line in f1: 
    if regPtr == -1: 
        regPtr = int(line.strip().split(" ")[1])
    else: 
        temp = line.strip().split(" ")
        temp[1] = int(temp[1])
        temp[2] = int(temp[2])
        temp[3] = int(temp[3])
        instructions.append(temp)

# intcode machine functions (opcodes)
def addr(beforeRegisters, instructionValues): 
    after = beforeRegisters[:]
    after[instructionValues[3]] = beforeRegisters[instructionValues[1]] + beforeRegisters[instructionValues[2]]
    return after

def addi(beforeRegisters, instructionValues): 
    after = beforeRegisters[:]
    after[instructionValues[3]] = beforeRegisters[instructionValues[1]] + instructionValues[2]
    return after

def mulr(beforeRegisters, instructionValues):
    after = beforeRegisters[:]
    after[instructionValues[3]] = beforeRegisters[instructionValues[1]] * beforeRegisters[instructionValues[2]]
    return after

def muli(beforeRegisters, instructionValues): 
    after = beforeRegisters[:]
    after[instructionValues[3]] = beforeRegisters[instructionValues[1]] * instructionValues[2]
    return after

def banr(beforeRegisters, instructionValues): 
    after = beforeRegisters[:]
    after[instructionValues[3]] = beforeRegisters[instructionValues[1]] & beforeRegisters[instructionValues[2]]
    return after

def bani(beforeRegisters, instructionValues): 
    after = beforeRegisters[:]
    after[instructionValues[3]] = beforeRegisters[instructionValues[1]] & instructionValues[2]
    return after

def borr(beforeRegisters, instructionValues): 
    after = beforeRegisters[:]
    after[instructionValues[3]] = beforeRegisters[instructionValues[1]] | beforeRegisters[instructionValues[2]]
    return after

def bori(beforeRegisters, instructionValues):
    after = beforeRegisters[:]
    after[instructionValues[3]] = beforeRegisters[instructionValues[1]] | instructionValues[2]
    return after

def setr(beforeRegisters, instructionValues): 
    after = beforeRegisters[:]
    after[instructionValues[3]] = beforeRegisters[instructionValues[1]]
    return after

def seti(beforeRegisters, instructionValues):
    after = beforeRegisters[:]
    after[instructionValues[3]] = instructionValues[1]
    return after

def gtir(beforeRegisters, instructionValues):
    after = beforeRegisters[:]
    if instructionValues[1] > beforeRegisters[instructionValues[2]]: 
        after[instructionValues[3]] = 1
    else:
        after[instructionValues[3]] = 0 
    return after

def gtri(beforeRegisters, instructionValues):
    after = beforeRegisters[:]
    if beforeRegisters[instructionValues[1]] > instructionValues[2]:
        after[instructionValues[3]] = 1
    else: 
        after[instructionValues[3]] = 0 
    return after

def gtrr(beforeRegisters, instructionValues): 
    after = beforeRegisters[:]
    if beforeRegisters[instructionValues[1]] > beforeRegisters[instructionValues[2]]:
        after[instructionValues[3]] = 1
    else: 
        after[instructionValues[3]] = 0 
    return after

def eqir(beforeRegisters, instructionValues): 
    after = beforeRegisters[:]
    if instructionValues[1] == beforeRegisters[instructionValues[2]]:
        after[instructionValues[3]] = 1 
    else:
        after[instructionValues[3]] = 0 
    return after

def eqri(beforeRegisters, instructionValues):
    after = beforeRegisters[:]
    if beforeRegisters[instructionValues[1]] == instructionValues[2]: 
        after[instructionValues[3]] = 1
    else:
        after[instructionValues[3]] = 0 
    return after

def eqrr(beforeRegisters, instructionValues):
    after = beforeRegisters[:]
    if beforeRegisters[instructionValues[1]] == beforeRegisters[instructionValues[2]]:
        after[instructionValues[3]] = 1
    else:
        after[instructionValues[3]] = 0
    return after

# controller to run the instructions 
while ip < len(instructions):
    register[regPtr] = ip 
    print("F", instructions[ip][0], instructions[ip])

    if instructions[ip][0] == "addr":
        register = addr(register, instructions[ip])
    elif instructions[ip][0] == "addi": 
        register = addi(register, instructions[ip])
    elif instructions[ip][0] == "mulr":
        register = mulr(register, instructions[ip])
    elif instructions[ip][0] == "muli": 
        register = muli(register, instructions[ip])
    elif instructions[ip][0] == "banr": 
        register = banr(register, instructions[ip])
    elif instructions[ip][0] == "bani": 
        register = bani(register, instructions[ip])
    elif instructions[ip][0] == "borr":
        register = borr(register, instructions[ip])
    elif instructions[ip][0] == "bori":
        register = bori(register, instructions[ip])
    elif instructions[ip][0] == "setr":
        register = setr(register, instructions[ip])
    elif instructions[ip][0] == "seti": 
        register = seti(register, instructions[ip])
    elif instructions[ip][0] == "gtir": 
        register = gtir(register, instructions[ip])
    elif instructions[ip][0] == "gtri": 
        register = gtri(register, instructions[ip])
    elif instructions[ip][0] == "gtrr": 
        register = gtrr(register, instructions[ip])
    elif instructions[ip][0] == "eqir":  
        register = eqir(register, instructions[ip])
    elif instructions[ip][0] == "eqri":
        register = eqri(register, instructions[ip])
    elif instructions[ip][0] == "eqrr": 
        register = eqrr(register, instructions[ip])

    ip = register[regPtr]
    print("2", register)
    ip += 1 
    print("3",ip)

print(register[0])

# there is a loop here
# need to reverse engineer this one! yay