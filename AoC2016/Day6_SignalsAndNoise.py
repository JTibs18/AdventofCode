import operator

#Part 1 Solution
f1 = open("day6.txt")

lines = []
message = ""

for line in f1:
    line = line.strip("\n")
    lines.append(line)

for i in range(len(lines[0])):
    occurrance = dict()
    for char in lines:
        if char[i] in occurrance:
            count = occurrance.get(char[i])
            count += 1
            occurrance[char[i]] = count
        else:
            occurrance[char[i]] = 1
    message += max(occurrance.items(), key=operator.itemgetter(1))[0]
print(message)

#Part 2 Solution
f1 = open("day6.txt")

lines = []
message = ""

for line in f1:
    line = line.strip("\n")
    lines.append(line)

for i in range(len(lines[0])):
    occurrance = dict()
    for char in lines:
        if char[i] in occurrance:
            count = occurrance.get(char[i])
            count += 1
            occurrance[char[i]] = count
        else:
            occurrance[char[i]] = 1
    message += min(occurrance.items(), key=operator.itemgetter(1))[0]
print(message)
