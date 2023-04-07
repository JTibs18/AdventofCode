#Part 1 Solution
f1 = open("day17.txt")

index = 1
val = 1
spinLock = [0, 1]

for line in f1:
    steps = int(line.strip())

while index < 2018: 
    val += 1

    if len(spinLock) < steps: 
        numSteps = steps % len(spinLock)
    else: 
        numSteps = steps

    if index + numSteps < len(spinLock): 
        index = index + numSteps + 1 
    else: 
        index = ((index + numSteps) - len(spinLock)) + 1

    spinLock.insert(index, val)

print(spinLock[spinLock.index(2017) + 1])

#Part 2 Solution (takes about 30 seconds to run)
f1 = open("day17.txt")

index = 1
val = 1
spinLock = dict()
spinLock[0] = 0
spinLock[1] = 1 
lenSpinLock = 1

for line in f1:
    steps = int(line.strip())

while index <= 50000000: 
    val += 1
    lenSpinLock += 1

    if lenSpinLock < steps: 
        numSteps = steps % lenSpinLock
    else: 
        numSteps = steps

    if index + numSteps < lenSpinLock: 
        index = index + numSteps + 1 
    else: 
        index = ((index + numSteps) - lenSpinLock) + 1

    spinLock[index] = val 

print(spinLock[1])
