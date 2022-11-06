#Part 1 Solution
f1 = open("day8.txt")

codeLength = 0
memoryLength = 0

for line in f1:
    line = line.strip()
    codeLength += len(line)
    prev = line[0]
    removeCount = 2

    for i in line:
        if prev == "\\" and i == "\\":
            removeCount += 1
            prev = '' # To account for cases like \\\\
        elif prev == "\\" and i == '"':
            removeCount += 1
            prev = ''
        elif prev == "\\" and i == "x":
            removeCount += 3
            prev = ''
        else:
            prev = i

    memoryLength += len(line) - removeCount

print(codeLength - memoryLength)

#Part 2 Solution
f1 = open("day8.txt")

newlyEncoded = 0
originalString = 0

for line in f1:
    line = line.strip()
    originalString += len(line)
    prev = line[0]
    addCount = 4

    for i in line:
        if prev == "\\" and i == "\\":
            addCount += 2
            prev = '' # To account for cases like \\\\
        elif prev == "\\" and i == '"':
            addCount += 2
            prev = ''
        elif prev == "\\" and i == "x":
            addCount += 1
            prev = ''
        else:
            prev = i

    newlyEncoded += len(line) + addCount

print(newlyEncoded - originalString)
