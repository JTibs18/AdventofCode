# Part 1 Solution 
f1 = open("day16.txt")
inputCount = 0 
threeOrMorePossibleEpochs = 0 
tempInstrunctionGroup = dict() 
allInstructions = []

# parse input 
for line in f1: 
    if inputCount == 3: 
        inputCount = 0
        continue 

    if inputCount == 1 and line == "\n": 
        break 
    
    if "Before" in line: 
        val = line.strip().split("[") 
        val = val[1].replace("]", "")
        val = val.strip().split(",")
        tempInstrunctionGroup["before"] = val
    elif "After" in line: 
        val = line.strip().split("[")
        val = val[1].replace("]", "")
        val = val.strip().split(",")
        tempInstrunctionGroup["after"] = val
    elif line != "\n": 
        val = line.strip().split(" ")
        tempInstrunctionGroup["instruction"] = val

    inputCount += 1 
    
    if inputCount == 3: 
        allInstructions.append(tempInstrunctionGroup)
        tempInstrunctionGroup = dict()

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

# testing all samples against opcodes to see which sample behaves like the opcode
for samples in allInstructions:
    count = 0 
    results = [int(x) for x in samples["after"]]
    before = [int(x) for x in samples["before"]]
    instructions = [int(x) for x in samples["instruction"]]

    if addr(before, instructions) == results:
        count += 1 
    if addi(before, instructions) == results:
        count += 1
    if mulr(before, instructions) == results:
        count += 1 
    if muli(before, instructions) == results:
        count += 1
    if banr(before, instructions) == results:
        count += 1
    if bani(before, instructions) == results:
        count += 1 
    if borr(before, instructions) == results:
        count += 1
    if bori(before, instructions) == results:
        count += 1 
    if setr(before, instructions) == results:
        count += 1 
    if seti(before, instructions) == results:
        count += 1
    if gtir(before, instructions) == results:
        count += 1
    if gtri(before, instructions) == results:
        count += 1
    if gtrr(before, instructions) == results:
        count += 1
    if eqir(before, instructions) == results:
        count += 1
    if eqri(before, instructions) == results:
        count += 1 
    if eqrr(before, instructions) == results:
        count += 1 

    if count >= 3: 
        threeOrMorePossibleEpochs += 1 

print(threeOrMorePossibleEpochs)

# Part 2 Solution 
f1 = open("day16.txt")
inputCount = 0 
parseTestProgram = False 
tempInstrunctionGroup = dict() 
knownOpcodes = set() 
opcodeMappings = [["addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori", "setr", "seti", "gtir", "gtri", "gtrr", "eqir", "eqri", "eqrr"] for _ in range(16)]
allInstructions = []
testProgram = []
register = [0, 0, 0, 0]

# parse input 
for line in f1: 
    if inputCount == 3: 
        inputCount = 0
        continue 

    if inputCount == 1 and line == "\n": 
        parseTestProgram = True
    
    if parseTestProgram == False: 
        if "Before" in line: 
            val = line.strip().split("[") 
            val = val[1].replace("]", "")
            val = val.strip().split(",")
            tempInstrunctionGroup["before"] = val
        elif "After" in line: 
            val = line.strip().split("[")
            val = val[1].replace("]", "")
            val = val.strip().split(",")
            tempInstrunctionGroup["after"] = val
        elif line != "\n": 
            val = line.strip().split(" ")
            tempInstrunctionGroup["instruction"] = val

        inputCount += 1 
        
        if inputCount == 3: 
            allInstructions.append(tempInstrunctionGroup)
            tempInstrunctionGroup = dict()
    elif line != "\n":
        testProgram.append(line.strip().split(" "))

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

# testing all samples against opcodes and removing opcodes that cannot work
for samples in allInstructions:
    results = [int(x) for x in samples["after"]]
    before = [int(x) for x in samples["before"]]
    instructions = [int(x) for x in samples["instruction"]]

    if "addr" in opcodeMappings[instructions[0]] and addr(before, instructions) != results: 
        opcodeMappings[instructions[0]].remove("addr") 
    if "addi" in opcodeMappings[instructions[0]] and addi(before, instructions) != results: 
        opcodeMappings[instructions[0]].remove("addi") 
    if "mulr" in opcodeMappings[instructions[0]] and mulr(before, instructions) != results: 
        opcodeMappings[instructions[0]].remove("mulr") 
    if "muli" in opcodeMappings[instructions[0]] and muli(before, instructions) != results: 
        opcodeMappings[instructions[0]].remove("muli") 
    if "banr" in opcodeMappings[instructions[0]] and banr(before, instructions) != results: 
        opcodeMappings[instructions[0]].remove("banr") 
    if "bani" in opcodeMappings[instructions[0]] and bani(before, instructions) != results: 
        opcodeMappings[instructions[0]].remove("bani") 
    if "borr" in opcodeMappings[instructions[0]] and borr(before, instructions) != results: 
        opcodeMappings[instructions[0]].remove("borr") 
    if "bori" in opcodeMappings[instructions[0]] and bori(before, instructions) != results: 
        opcodeMappings[instructions[0]].remove("bori") 
    if "setr" in opcodeMappings[instructions[0]] and setr(before, instructions) != results: 
        opcodeMappings[instructions[0]].remove("setr") 
    if "seti" in opcodeMappings[instructions[0]] and seti(before, instructions) != results: 
        opcodeMappings[instructions[0]].remove("seti") 
    if "gtir" in opcodeMappings[instructions[0]] and gtir(before, instructions) != results: 
        opcodeMappings[instructions[0]].remove("gtir") 
    if "gtri" in opcodeMappings[instructions[0]] and gtri(before, instructions) != results: 
        opcodeMappings[instructions[0]].remove("gtri") 
    if "gtrr" in opcodeMappings[instructions[0]] and gtrr(before, instructions) != results: 
        opcodeMappings[instructions[0]].remove("gtrr") 
    if "eqir" in opcodeMappings[instructions[0]] and eqir(before, instructions) != results: 
        opcodeMappings[instructions[0]].remove("eqir") 
    if "eqri" in opcodeMappings[instructions[0]] and eqri(before, instructions) != results: 
        opcodeMappings[instructions[0]].remove("eqri") 
    if "eqrr" in opcodeMappings[instructions[0]] and eqrr(before, instructions) != results: 
        opcodeMappings[instructions[0]].remove("eqrr") 

# finding opcodes to function mappings using processes of elimination
while len(knownOpcodes) < 16: 
    for indx, val in enumerate(opcodeMappings): 
        if len(val) == 1: 
            knownOpcodes.add(val[0])
        else: 
            for j in val: 
                if j in knownOpcodes:
                    opcodeMappings[indx].remove(j)

# executing the test program 
for i in testProgram: 
    instruction = [int(x) for x in i]

    if instruction[0] == opcodeMappings.index(["addr"]):
        register = addr(register, instruction)
    elif instruction[0] == opcodeMappings.index(["addi"]): 
        register = addi(register, instruction)
    elif instruction[0] == opcodeMappings.index(["mulr"]):
        register = mulr(register, instruction)
    elif instruction[0] == opcodeMappings.index(["muli"]): 
        register = muli(register, instruction)
    elif instruction[0] == opcodeMappings.index(["banr"]): 
        register = banr(register, instruction)
    elif instruction[0] == opcodeMappings.index(["bani"]): 
        register = bani(register, instruction)
    elif instruction[0] == opcodeMappings.index(["borr"]):
        register = borr(register, instruction)
    elif instruction[0] == opcodeMappings.index(["bori"]):
        register = bori(register, instruction)
    elif instruction[0] == opcodeMappings.index(["setr"]):
        register = setr(register, instruction)
    elif instruction[0] == opcodeMappings.index(["seti"]): 
        register = seti(register, instruction)
    elif instruction[0] == opcodeMappings.index(["gtir"]): 
        register = gtir(register, instruction)
    elif instruction[0] == opcodeMappings.index(["gtri"]): 
        register = gtri(register, instruction)
    elif instruction[0] == opcodeMappings.index(["gtrr"]): 
        register = gtrr(register, instruction)
    elif instruction[0] == opcodeMappings.index(["eqir"]):  
        register = eqir(register, instruction)
    elif instruction[0] == opcodeMappings.index(["eqri"]):
        register = eqri(register, instruction)
    elif instruction[0] == opcodeMappings.index(["eqrr"]): 
        register = eqrr(register, instruction)

print(register[0])