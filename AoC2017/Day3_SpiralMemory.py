#Part 1 Solution
import math

f1 = open("day3.txt")
for line in f1:
    num = int(line)

outer = math.ceil((math.ceil(math.sqrt(num)) - 1) / 2)
prevSquare = (((outer * 2) - 1) ** 2)
straight = []

straight.append(prevSquare + outer)
for i in range(1, 4):
    straight.append(straight[i - 1] + (outer * 2))

if num in straight:
    print(outer)
else:
    min = outer
    for i in range(4):
        if abs(straight[i] - num) < min:
            min = abs(straight[i] - num)
    print(outer + min)

#Part 2 Solution
f1 = open("day3.txt")
