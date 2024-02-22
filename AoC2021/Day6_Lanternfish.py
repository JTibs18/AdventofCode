# Part 1 Solution
f1 = open("day6.txt")

fishState = [0] * 9
numDays = 80

for line in f1:
    parsedNum = line.strip().split(",")
    nums = [int(x) for x in parsedNum]

for i in nums:
    fishState[i] += 1

for i in range(numDays): 
    resetFishCount = fishState.pop(0)
    fishState[6] += resetFishCount
    fishState.append(resetFishCount)

print(sum(fishState))

# Part 2 Solution
f1 = open("day6.txt")

fishState = [0] * 9
numDays = 256

for line in f1:
    parsedNum = line.strip().split(",")
    nums = [int(x) for x in parsedNum]

for i in nums:
    fishState[i] += 1

for i in range(numDays): 
    resetFishCount = fishState.pop(0)
    fishState[6] += resetFishCount
    fishState.append(resetFishCount)

print(sum(fishState))