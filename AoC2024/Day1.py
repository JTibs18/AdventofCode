# Part 1 Solution  
f1 = open("day1.txt")

total = 0
leftList = []
rightList = []

for line in f1:
    twoNums = line.strip().split("   ")
    leftList.append(int(twoNums[0]))
    rightList.append(int(twoNums[1]))

leftList.sort()
rightList.sort()

for indx in range(len(leftList)):
    total += abs(leftList[indx] - rightList[indx])

print(total)

# Part 2 Solution  
f1 = open("day1.txt")

total = 0
leftList = []
rightList = []

for line in f1:
    twoNums = line.strip().split("   ")
    leftList.append(int(twoNums[0]))
    rightList.append(int(twoNums[1]))

leftList.sort()
rightList.sort()

for num in leftList:
    total += num * rightList.count(num)

print(total)