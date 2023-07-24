# Part 1 Solution
# with help from https://stackoverflow.com/questions/34517540/find-all-combinations-of-a-list-of-numbers-with-a-given-sum

import itertools
f1 = open("day17.txt")

containers = []
target = 150 

for line in f1:
    containers.append(int(line.strip()))

numberOfWays = len([seq for i in range(len(containers))
                    for seq in itertools.combinations(containers, i)
                    if sum(seq) == target
                    ])

print(numberOfWays)

# Part 2 Solution
import itertools
f1 = open("day17.txt")

containers = []
target = 150 
minContainers = 1000000
minCount = 0 

for line in f1:
    containers.append(int(line.strip()))

combinations = [(seq, i) for i in range(len(containers))
                    for seq in itertools.combinations(containers, i)
                    if sum(seq) == target
                ]

for i in combinations: 
    if i[1] < minContainers:
        minContainers = i[1]
        minCount = 1 
    elif i[1] == minContainers: 
        minCount += 1

print(minCount)