#Part 1 Solution
f1 = open("day1.txt")

for line in f1:
    line = line.strip("\n")

sum = 0

for indx, num in enumerate(line):
    if indx + 1 == len(line) and num == line[0]:
        sum += int(num)
    elif indx + 1 < len(line) and num == line[indx + 1]:
        sum += int(num)
print(sum)

#Part 2 Solution
f1 = open("day1.txt")

for line in f1:
    line = line.strip("\n")

sum = 0
half = int(len(line) / 2)

for indx, num in enumerate(line):
    if num == line[half]:
        sum += int(num)
    half += 1
    if half == len(line):
        half = 0
print(sum)
