#Part 1 Solution
f1 = open("day24.txt")

gifts = [] 
possibleFirstGroups = []
smallestLengthFirstGroups = []
smallestQuantumEntanglement = 10000000000000 

# parsing input
for line in f1:
    gifts.append(int(line.strip()))

gifts = sorted(gifts, reverse=True)

# finding one third the total gift weight 
groupOneWeight = sum(gifts) / 3
startingPtr = 0
print(groupOneWeight)

# finding groups of gifts that sum to one third the total weight
while startingPtr < len(gifts):
    currentGroup = []
    curSum = 0 

    for i in range(startingPtr, len(gifts)):
        if gifts[i] + curSum < groupOneWeight:
            currentGroup.append(gifts[i])
            curSum += gifts[i]
        elif gifts[i] + curSum == groupOneWeight: 
            currentGroup.append(gifts[i])
            possibleFirstGroups.append(currentGroup)
            print(sum(currentGroup))
            break

    startingPtr += 1 

# filtering out all possibilities except the smallest amount of gifts  
shortestLength = len(gifts)

for i in possibleFirstGroups: 
    if len(i) < shortestLength:
        smallestLengthFirstGroups = [i]
        shortestLength = len(i)
    elif len(i) == shortestLength: 
        smallestLengthFirstGroups.append(i)

print(smallestLengthFirstGroups)

# finding the smallest quantum entanglement
for i in possibleFirstGroups: 
    quantumEntanglement = 1
    
    for j in i: 
        quantumEntanglement *= j 
    
    print(quantumEntanglement)
    
    if quantumEntanglement < smallestQuantumEntanglement:
        smallestQuantumEntanglement = quantumEntanglement

print(smallestQuantumEntanglement)

# too high: 70614169998
# 67601337186
# 35307084999
# 221020192639

# need to ensure the rest of the packages can fit to sum even weight in other two sections 