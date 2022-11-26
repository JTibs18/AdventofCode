# Part 1 Solution
f1 = open("day20.txt")

listOfRanges = []
stack = []

# parsing input data
for line in f1:
    range = line.strip().split("-")
    range = [int(x) for x in range]
    listOfRanges.append(range)

listOfRanges.sort()
stack.append(listOfRanges[0])

# merging overlapping ranges
for i in listOfRanges[1:]:
    if stack[-1][0] <= i[0] <= stack[-1][-1]:
        stack[-1][-1] = max(stack[-1][-1], i[-1])
    else:
        stack.append(i)

# 0 is the lowest number if the ranges don't begin with 0
if stack[0][0] > 0:
    print(0)

# Finding two ranges that have at least a difference of one number between them.
# The second number in the lower range, plus 1 is the lowest number that is not in a range
for indx, val in enumerate(stack):
    if stack[indx][1] + 1 != stack[indx + 1][0]:
        print(stack[indx][1] + 1)
        break

# Part 2 Solution
f1 = open("day20.txt")

listOfRanges = []
stack = []

# parsing input data
for line in f1:
    range = line.strip().split("-")
    range = [int(x) for x in range]
    listOfRanges.append(range)

listOfRanges.sort()
stack.append(listOfRanges[0])
allowedIps = 0
maxRange = 4294967295

# merging overlapping ranges
for i in listOfRanges[1:]:
    if stack[-1][0] <= i[0] <= stack[-1][-1]:
        stack[-1][-1] = max(stack[-1][-1], i[-1])
    else:
        stack.append(i)

# finding numbers between 0 and first range
if stack[0][0] > 0:
    allowedIps += stack[0][0]

# finding the number of numbers between each range
for indx, val in enumerate(stack):
    if indx < len(stack) - 1:
        diff = (stack[indx + 1][0] - stack[indx][1]) - 1
    else:
        diff = maxRange - stack[indx][1]
    if diff > 0:
        allowedIps += diff
print(allowedIps)
