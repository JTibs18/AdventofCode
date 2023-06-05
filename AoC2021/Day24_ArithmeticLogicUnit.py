# Part 1 Solution
import math 

f1 = open("day24.txt")

variables = {'w':0, 'x':0, 'y':0, 'z':0}
instructionList = []
input = '99999999999999'
inputIndx = 0

for line in f1:
    instruction = line.strip().split(' ')
    instructionList.append(instruction)
    if instruction[0] == 'inp':
        variables[instruction[1]] = int(input[inputIndx])
        inputIndx += 1
    elif instruction[0] == 'add':
        if instruction[2].lstrip('-').isdigit():
            variables[instruction[1]] = variables[instruction[1]] + int(instruction[2])
        else:
            variables[instruction[1]] = variables[instruction[1]] + variables[instruction[2]]
    elif instruction[0] == 'mul':
        if instruction[2].lstrip('-').isdigit():
            variables[instruction[1]] = variables[instruction[1]] * int(instruction[2])
        else:
            variables[instruction[1]] = variables[instruction[1]] * variables[instruction[2]]
    elif instruction[0] == 'div':
        if instruction[2].lstrip('-').isdigit() and int(variables[instruction[2]]) != 0:
            variables[instruction[1]] = math.floor(variables[instruction[1]] / int(instruction[2]))
        elif variables[instruction[2]] != 0:
                variables[instruction[1]] = math.floor(variables[instruction[1]] / variables[instruction[2]])
    elif instruction[0] == 'mod':
        if instruction[2].lstrip('-').isdigit() and variables[instruction[1]] > 0 and int(variables[instruction[2]]) > 0:
            variables[instruction[1]] = variables[instruction[1]] % int(instruction[2])
        elif variables[instruction[1]] > 0 and variables[instruction[2]] > 0:
            variables[instruction[1]] = variables[instruction[1]] % variables[instruction[2]]
    elif instruction[0] == 'eql':
        if variables[instruction[1]] == variables[instruction[2]]:
            variables[instruction[1]] = 1
        else:
            variables[instruction[1]] = 0
    print(variables)

# while int(input) > 0:
#     break
