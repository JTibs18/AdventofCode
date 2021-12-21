#Part 1 Solution
import math
f1 = open("day7.txt")

crabs = []
fuel = {}

for line in f1:
    crabs = line.strip().split(",")

for indx, val in enumerate(crabs):
    crabs[indx] = int(crabs[indx])

for val in set(crabs):
    for c in crabs:
        if val != c:
            diff = abs(val - c)
            if val in fuel:
                fuel[val] += diff
            else:
                fuel[val] = diff

for key, val in fuel.items():
    if val == min(fuel.values()):
        print (val)

#Part 2 Solution
import math
f1 = open("day7.txt")

crabs = []
fuel = {}

for line in f1:
    crabs = line.strip().split(",")

for indx, val in enumerate(crabs):
    crabs[indx] = int(crabs[indx])

for indx in range(min(crabs), max(crabs)):
    for c in crabs:
        if indx != c:
            diff = abs(indx - c)
            f = (diff * (diff + 1)) / 2
            if indx in fuel:
                fuel[indx] += f
            else:
                fuel[indx] = f

for key, val in fuel.items():
    if val == min(fuel.values()):
        print (val)
