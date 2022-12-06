# Part 1 Solution
f1 = open("day6.txt")

indx1 = 0
indx2 = 4

for line in f1:
    dataStream = line

while len(set(dataStream[indx1: indx2])) != 4:
    indx1 += 1
    indx2 += 1

print(indx2)

# Part 2 Solution
f1 = open("day6.txt")

indx1 = 0
indx2 = 14

for line in f1:
    dataStream = line

while len(set(dataStream[indx1: indx2])) != 14:
    indx1 += 1
    indx2 += 1

print(indx2)
