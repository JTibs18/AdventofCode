# Part 1 Solution
f1 = open("day6.txt")
cycles = 0
previousBanks = []

for line in f1:
    bank = line.strip().split()

for indx, val in enumerate(bank):
    bank[indx] = int(val)

while bank not in previousBanks: 
    previousBanks.append(bank[:])
    highestNum = max(bank)
    indx = bank.index(highestNum)
    bank[indx] = 0
    addToIndex = indx + 1

    if addToIndex == len(bank):
        addToIndex = 0

    while highestNum: 
        bank[addToIndex] += 1
        addToIndex += 1 
        highestNum -= 1
        if addToIndex == len(bank): 
            addToIndex = 0
    cycles += 1 

print(cycles)   

# Part 2 Solution
f1 = open("day6.txt")
previousBanks = []

for line in f1:
    bank = line.strip().split()

for indx, val in enumerate(bank):
    bank[indx] = int(val)

while bank not in previousBanks: 
    previousBanks.append(bank[:])
    highestNum = max(bank)
    indx = bank.index(highestNum)
    bank[indx] = 0
    addToIndex = indx + 1

    if addToIndex == len(bank):
        addToIndex = 0

    while highestNum: 
        bank[addToIndex] += 1
        addToIndex += 1 
        highestNum -= 1
        if addToIndex == len(bank): 
            addToIndex = 0

print(len(previousBanks) - previousBanks.index(bank))
    