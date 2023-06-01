# Part 1 Solution
f1 = open("day8.txt")

registers = dict() 
instructions = []

for line in f1: 
    instruction = line.strip().split(" ")
    
    if instruction[0] not in registers: 
        registers[instruction[0]] = 0 
    
    if instruction[4] not in registers: 
        registers[instruction[4]] = 0 

    instructions.append([instruction[0], instruction[1], int(instruction[2]), instruction[4], instruction[5], int(instruction[6])])

for i in instructions: 
    if i[4] == "<":
        if registers[i[3]] < i[5] and i[1] == "inc":
            registers[i[0]] += i[2]
        if registers[i[3]] < i[5] and i[1] == "dec": 
            registers[i[0]] -= i[2]
    if i[4] == ">": 
        if registers[i[3]] > i[5] and i[1] == "inc":
            registers[i[0]] += i[2]
        if registers[i[3]] > i[5] and i[1] == "dec": 
            registers[i[0]] -= i[2]
    if i[4] == "<=":
        if registers[i[3]] <= i[5] and i[1] == "inc":
            registers[i[0]] += i[2]
        if registers[i[3]] <= i[5] and i[1] == "dec": 
            registers[i[0]] -= i[2]
    if i[4] == ">=": 
        if registers[i[3]] >= i[5] and i[1] == "inc":
            registers[i[0]] += i[2]
        if registers[i[3]] >= i[5] and i[1] == "dec": 
            registers[i[0]] -= i[2]
    if i[4] == "==": 
        if registers[i[3]] == i[5] and i[1] == "inc":
            registers[i[0]] += i[2]
        if registers[i[3]] == i[5] and i[1] == "dec": 
            registers[i[0]] -= i[2]
    if i[4] == "!=":
        if registers[i[3]] != i[5] and i[1] == "inc":
            registers[i[0]] += i[2]
        if registers[i[3]] != i[5] and i[1] == "dec": 
            registers[i[0]] -= i[2]
    
print(max(registers.values()))

# Part 2 Solution
f1 = open("day8.txt")

registers = dict() 
instructions = []
highestValue = 0

for line in f1: 
    instruction = line.strip().split(" ")
    
    if instruction[0] not in registers: 
        registers[instruction[0]] = 0 
    
    if instruction[4] not in registers: 
        registers[instruction[4]] = 0 

    instructions.append([instruction[0], instruction[1], int(instruction[2]), instruction[4], instruction[5], int(instruction[6])])

for i in instructions: 
    if i[4] == "<":
        if registers[i[3]] < i[5] and i[1] == "inc":
            registers[i[0]] += i[2]
        if registers[i[3]] < i[5] and i[1] == "dec": 
            registers[i[0]] -= i[2]
    if i[4] == ">": 
        if registers[i[3]] > i[5] and i[1] == "inc":
            registers[i[0]] += i[2]
        if registers[i[3]] > i[5] and i[1] == "dec": 
            registers[i[0]] -= i[2]
    if i[4] == "<=":
        if registers[i[3]] <= i[5] and i[1] == "inc":
            registers[i[0]] += i[2]
        if registers[i[3]] <= i[5] and i[1] == "dec": 
            registers[i[0]] -= i[2]
    if i[4] == ">=": 
        if registers[i[3]] >= i[5] and i[1] == "inc":
            registers[i[0]] += i[2]
        if registers[i[3]] >= i[5] and i[1] == "dec": 
            registers[i[0]] -= i[2]
    if i[4] == "==": 
        if registers[i[3]] == i[5] and i[1] == "inc":
            registers[i[0]] += i[2]
        if registers[i[3]] == i[5] and i[1] == "dec": 
            registers[i[0]] -= i[2]
    if i[4] == "!=":
        if registers[i[3]] != i[5] and i[1] == "inc":
            registers[i[0]] += i[2]
        if registers[i[3]] != i[5] and i[1] == "dec": 
            registers[i[0]] -= i[2]

    if max(registers.values()) > highestValue: 
        highestValue = max(registers.values())
    
print(highestValue)