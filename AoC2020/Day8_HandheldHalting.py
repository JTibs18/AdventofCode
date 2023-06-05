#Part 1 Solution
f1 = open("day8.txt")

instructions = []

for line in f1:
    line = line.rstrip()
    instructions.append(line)

ptr = 0
accumulator = 0
travelled = set()

while instructions:
    travelled.add(ptr)
    instruct = instructions[ptr][:3]
    num = instructions[ptr][4:]

    if instruct == "acc":
        if num[0] == "+":
            accumulator += int(num[1:])
        else:
            accumulator -= int(num[1:])
        ptr += 1
    elif instruct == "jmp":
        if num[0] == "+":
            ptr += int(num[1:])
        else:
            ptr -= int(num[1:])
    else:
        ptr += 1

    if ptr in travelled:
        print(accumulator)
        break

#Part 2 Solution
f1 = open("day8.txt")

instructions = []

for line in f1:
    line = line.rstrip()
    instructions.append(line)

ptr = 0
accumulator = 0
travelled = []

while instructions:
    travelled.append(ptr)
    print(ptr)
    instruct = instructions[ptr][:3]
    num = instructions[ptr][4:]

    if instruct == "acc":
        if num[0] == "+":
            accumulator += int(num[1:])
        else:
            accumulator -= int(num[1:])
        ptr += 1
    elif instruct == "jmp":
        if num[0] == "+":
            ptr += int(num[1:])
        else:
            ptr -= int(num[1:])
    else:
        ptr += 1

    if ptr > len(instructions):
        print(accumulator)
        break
    # 
    # if ptr in travelled:
    #     change = False
    #     while change == False:
    #         ins = travelled.pop()
    #         instruct2 = instructions[ins][:3]
    #         num2 = instructions[ins][4:]
    #
    #         if instruct2 == "acc":
    #             if num2[0] == "+":
    #                 accumulator -= int(num2[1:])
    #             else:
    #                 accumulator += int(num2[1:])
    #             ptr -= 1
    #         elif instruct2 == "jmp":
    #             if num2[0] == "+":
    #                 ptr -= int(num2[1:])
    #             else:
    #                 ptr += int(num2[1:])
    #             ptr += 1
    #             change = True
    #         else:
    #             ptr -= 1
    #             if num2[0] == "+":
    #                 ptr += int(num2[1:])
    #             else:
    #                 ptr -= int(num2[1:])
    #             change = True
