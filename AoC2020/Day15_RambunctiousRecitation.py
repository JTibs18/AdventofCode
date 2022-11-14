# Part 1 Solution
f1 = open("day15.txt")

turnsNumCalled = dict()
callStack = []
turn = 1

for line in f1:
    startingNums = line.strip().split(",")

for i in startingNums:
    callStack.append(int(i))
    if int(i) in turnsNumCalled:
        turnsNumCalled[int(i)].append(turn)
    else:
        turnsNumCalled[int(i)] = [turn]
    turn += 1

while(turn <= 2020):
    lastCalled = callStack[len(callStack) - 1]
    if len(turnsNumCalled[lastCalled]) > 1:
        newCall = (turn - 1) - turnsNumCalled[lastCalled][len(turnsNumCalled[lastCalled]) - 2]
        if newCall in turnsNumCalled:
            turnsNumCalled[newCall].append(turn)
        else:
            turnsNumCalled[newCall] = [turn]
    else:
        newCall = 0
        turnsNumCalled[newCall].append(turn)
    callStack.append(newCall)
    turn += 1
print(newCall)

# Part 2 Solution (Takes about 90 seconds to run)
# To Do: Improve algorithmic runtime to at least less than a minute
f1 = open("day15.txt")

turnsNumCalled = dict()
callStack = []
turn = 1

for line in f1:
    startingNums = line.strip().split(",")

for i in startingNums:
    callStack.append(int(i))
    if int(i) in turnsNumCalled:
        turnsNumCalled[int(i)].append(turn)
    else:
        turnsNumCalled[int(i)] = [turn]
    turn += 1

while(turn <= 30000000):
    lastCalled = callStack[len(callStack) - 1]
    if len(turnsNumCalled[lastCalled]) > 1:
        newCall = (turn - 1) - turnsNumCalled[lastCalled][len(turnsNumCalled[lastCalled]) - 2]
        if newCall in turnsNumCalled:
            turnsNumCalled[newCall].append(turn)
        else:
            turnsNumCalled[newCall] = [turn]
    else:
        newCall = 0
        turnsNumCalled[newCall].append(turn)
    callStack.append(newCall)
    turn += 1
print(newCall)
