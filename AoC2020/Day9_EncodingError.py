#Part 1 Solution
f1 = open("day9.txt")

queue = []

for line in f1:
    queue.append(int(line.strip()))

startQ = 0
endQ = 25
cont = True

while (cont):
    sortedSub = sorted(queue[startQ:endQ])
    targetSum = queue[endQ]
    ptr1 = 0
    ptr2 = 24
    sumFound = False

    while (ptr1 < ptr2):
        if (sortedSub[ptr1] + sortedSub[ptr2] > targetSum):
            ptr2 -= 1
        elif(sortedSub[ptr1] + sortedSub[ptr2] < targetSum):
            ptr1 += 1
        else:
            sumFound = True
            break

    if sumFound == False:
        cont = False
        print(targetSum)
    else:
        startQ += 1
        endQ += 1

#Part 2 Solution
f1 = open("day9.txt")

invalidNumber = 41682220
queue = []

for line in f1:
    queue.append(int(line.strip()))

ptr1 = 0
ptr2 = 1

while (ptr1 < ptr2):
    subset = queue[ptr1:ptr2]
    if (sum(subset) > invalidNumber):
        ptr1 += 1
    elif (sum(subset) < invalidNumber):
        ptr2 += 1
    else:
        print(min(subset) + max(subset))
        break
