#Part 1 Solution
f1 = open("day2.txt")

code = []
prev = 5

for line in f1:
    line = line.strip("\n")
    for dir in line:
        if dir == "U":
            cur = prev - 3
            if cur > 0:
                prev = cur
        elif dir == "D":
            cur = prev + 3
            if cur < 10:
                prev = cur
        elif dir == "L" and prev != 1 and prev != 4 and prev != 7:
            prev = prev - 1
        elif dir == "R" and prev != 3 and prev != 6 and prev != 9:
            prev = prev + 1
    code.append(prev)
    
print(code)

#Part 2 Solution
f1 = open("day2.txt")

code = []
prev = 5

for line in f1:
    line = line.strip("\n")
    for dir in line:
        if dir == "U" and prev != 1 and prev != 2 and prev != 4 and prev != 5 and prev != 9:
            if prev == 3 or prev == 13:
                prev -= 2
            else:
                prev -= 4
        elif dir == "D" and prev != 5 and prev != 9 and prev != 10 and prev != 12 and prev != 13:
            if prev == 1 or prev == 11:
                prev += 2
            else:
                prev += 4
        elif dir == "L" and prev != 1 and prev != 2 and prev != 5 and prev != 10 and prev != 13:
            prev -= 1
        elif dir == "R" and prev != 1 and prev != 4 and prev != 9 and prev != 12 and prev != 13:
            prev += 1
    if prev == 10:
        code.append("A")
    elif prev == 11:
        code.append("B")
    elif prev == 12:
        code.append("C")
    elif prev == 13:
        code.append("D")
    else:
        code.append(prev)

print(code)
