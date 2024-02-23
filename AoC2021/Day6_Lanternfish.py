# Part 1 Solution
fishState = [0] * 9
numDays = 80

nums = [int(x) for x in open("day6.txt").read().strip().split(",")]

for i in nums:
    fishState[i] += 1

for _ in range(numDays): 
    resetFishCount = fishState.pop(0)
    fishState[6] += resetFishCount
    fishState.append(resetFishCount)

print(sum(fishState))

# Part 2 Solution
fishState = [0] * 9
numDays = 256

nums = [int(x) for x in open("day6.txt").read().strip().split(",")]

for i in nums:
    fishState[i] += 1

for _ in range(numDays): 
    resetFishCount = fishState.pop(0)
    fishState[6] += resetFishCount
    fishState.append(resetFishCount)

print(sum(fishState))