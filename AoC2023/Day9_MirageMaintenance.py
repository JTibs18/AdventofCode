# #Part 1 Solution
f1 = open("day9.txt")

sequences = []
predictedSum = 0

for line in f1:
    parsed = line.strip().split()
    sequences.append([int(x) for x in parsed])

for s in sequences: 
    newSequences = [s]

    while (sum(x == newSequences[-1][0] for x in newSequences[-1]) != len(newSequences[-1])):
        curSequence = []

        for i in range(len(newSequences[-1]) - 1):
            curSequence.append(newSequences[-1][i + 1] - newSequences[-1][i]) 
    
        newSequences.append(curSequence)

    newSequences = newSequences[::-1]

    for i in range(len(newSequences) - 1):
        newSequences[i + 1].append(newSequences[i][-1] + newSequences[i + 1][-1])

    predictedSum += newSequences[-1][-1]    

print(predictedSum)

# #Part 1 Solution
f1 = open("day9.txt")

sequences = []
predictedSum = 0

for line in f1:
    parsed = line.strip().split()
    sequences.append([int(x) for x in parsed])

for s in sequences: 
    newSequences = [s]

    while (sum(x == newSequences[-1][0] for x in newSequences[-1]) != len(newSequences[-1])):
        curSequence = []

        for i in range(len(newSequences[-1]) - 1):
            curSequence.append(newSequences[-1][i + 1] - newSequences[-1][i]) 
    
        newSequences.append(curSequence)

    newSequences = newSequences[::-1]

    for i in range(len(newSequences) - 1):
        newSequences[i + 1] = [newSequences[i + 1][0] - newSequences[i][0]] + newSequences[i + 1]

    predictedSum += newSequences[-1][0]

print(predictedSum)