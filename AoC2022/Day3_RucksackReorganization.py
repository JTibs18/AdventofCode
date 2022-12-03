# Part 1 Solution
f1 = open("day3.txt")

rucksacks = []
prioritySum = 0

for line in f1:
    rucksack = line.strip()
    rucksacks.append(rucksack)

for i in rucksacks:
    halfIndx = int(len(i) / 2)
    comp1 = i[0: halfIndx]
    comp2 = i[halfIndx :]
    for j in comp1:
        if j in comp2:
            if j.isupper():
                prioritySum += ord(j) - 38
                break
            else:
                prioritySum += ord(j) - 96
                break

print(prioritySum)

# Part 2 Solution
f1 = open("day3.txt")

rucksacks = []
prioritySum = 0
indx = 0
commonCount = dict()

for line in f1:
    rucksack = line.strip()
    minimizedRucksack = set()
    for i in rucksack:
        minimizedRucksack.add(i)

    rucksacks.append(minimizedRucksack)

for i in rucksacks:
    for j in i:
        if j in commonCount:
            commonCount[j] += 1
        else:
            commonCount[j] = 1
    indx += 1

    if indx == 3:
        indx = 0
        for j in commonCount:
            if commonCount[j] == 3:
                if j.isupper():
                    prioritySum += ord(j) - 38
                    break
                else:
                    prioritySum += ord(j) - 96
                    break
        commonCount = {}

print(prioritySum)
