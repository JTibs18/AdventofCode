#Part 1 Solution
f1 = open("day5.txt")

traversed = []
indx = 0

for line in f1:
    line = line.strip()

while indx < len(line) - 1:
    if (ord(line[indx + 1]) + 32 == ord(line[indx])) or (ord(line[indx + 1]) == ord(line[indx]) + 32):
        indx += 2
        while (len(traversed) > 0 and ((ord(traversed[len(traversed) - 1]) + 32 == ord(line[indx])) or (ord(traversed[len(traversed) - 1]) == ord(line[indx]) + 32))):
            traversed.pop()
            indx += 1
    else:
        traversed.append(line[indx])
        indx += 1

traversed.append(line[indx])
print(len(traversed))

#Part 2 Solution
f1 = open("day5.txt")

for line in f1:
    line = line.strip()

minLength = len(line)

for i in range(97, 122):
    newLine = ""
    indx = 0
    traversed = []

    for j in line:
        if ord(j.lower()) != i:
            newLine += j
    while indx < len(newLine) - 1:
        if (ord(newLine[indx + 1]) + 32 == ord(newLine[indx])) or (ord(newLine[indx + 1]) == ord(newLine[indx]) + 32):
            indx += 2
            while (len(traversed) > 0 and indx < len(newLine) - 1 and ((ord(traversed[len(traversed) - 1]) + 32 == ord(newLine[indx])) or (ord(traversed[len(traversed) - 1]) == ord(newLine[indx]) + 32))):
                traversed.pop()
                indx += 1
        else:
            traversed.append(newLine[indx])
            indx += 1

    if indx < len(newLine):
        traversed.append(newLine[indx])
    if len(traversed) < minLength:
        minLength = len(traversed)

print(minLength)
