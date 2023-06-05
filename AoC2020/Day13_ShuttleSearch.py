#Part 1 Solution
f1 = open("day13.txt")

isGoal = True
goalTime = 0
busId = []
validBusId = []
fastestBus = 0

for line in f1:
    if isGoal:
        goalTime = int(line.strip())
        lowestWaitTime = goalTime
        isGoal = False
    else:
        busId = line.strip().split(",")

for i in busId:
    if i != "x":
        validBusId.append(int(i))

for i in validBusId:
    busTime = 0
    while (busTime < goalTime):
        busTime += i
    if (busTime - goalTime < lowestWaitTime):
        lowestWaitTime = busTime - goalTime
        fastestBus = i

print(lowestWaitTime * fastestBus)

#Part 2 Solution
f1 = open("day13.txt")
