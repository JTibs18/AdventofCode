#Part 1 Solution
f1 = open("day10.txt")

for line in f1:
    data = line.strip()

for i in range(40):
    prev = data[0]
    count = 0
    newNum = ''

    for (indx, val) in enumerate(data):
        if (indx != 0) and (prev == val):
            count += 1
        elif (indx != 0) and (prev != val):
            newNum = newNum + str(count) + str(prev)
            count = 1
        else:
            count = 1

        prev = val

    newNum = newNum + str(count) + str(prev)
    data = newNum

print(len(newNum))

#Part 2 Solution
f1 = open("day10.txt")

for line in f1:
    data = list(line.strip())

print(data)

for i in range(50):
    prev = data[0]
    count = 0
    newNum = ''

    for (indx, val) in enumerate(data):
        if (indx != 0) and (prev == val):
            count += 1
        elif (indx != 0) and (prev != val):
            newNum = newNum + str(count) + str(prev)
            count = 1
        else:
            count = 1

        prev = val

    newNum = newNum + str(count) + str(prev)
    data = newNum

print(len(newNum))
