#Part 1 Solution
import copy 
f1 = open("day10.txt")

listNums = []
currentPosition = 0 
skipSize = 0

for i in range(0, 256): 
    listNums.append(i)

for line in f1: 
    lengths = line.strip().split(",")
    lengths = [int(x) for x in lengths]

for i in lengths: 
    if i > len(listNums): 
        continue 

    endingPoint = i + currentPosition

    if endingPoint > len(listNums): 

        startingPoint = endingPoint % len(listNums) 
        reverseEnd = listNums[0:startingPoint]
        middleList = listNums[startingPoint:currentPosition]
        reverseStart = listNums[currentPosition: len(listNums)]

        reverseList = []
        reverseList.extend(reverseStart)
        reverseList.extend(reverseEnd)
        reverseList.reverse() 

        newListNums = []
        newListNums.extend(reverseList[len(reverseList) - startingPoint: len(reverseList)])
        newListNums.extend(middleList)
        newListNums.extend(reverseList[0: len(reverseList) - startingPoint])

    elif endingPoint != currentPosition:
        startList = listNums[0: currentPosition]
        reverseList = listNums[currentPosition: endingPoint]
        endList = listNums[endingPoint: len(listNums)]

        reverseList.reverse() 

        newListNums = []
        newListNums.extend(startList)
        newListNums.extend(reverseList)
        newListNums.extend(endList)

    listNums = copy.deepcopy(newListNums)

    currentPosition += i + skipSize
    if currentPosition > len(listNums): 
        currentPosition = currentPosition % len(listNums)
    skipSize += 1 

print(listNums[0] * listNums[1])

