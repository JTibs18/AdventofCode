#Part 1 Solution
f1 = open("day2.txt")

hor = 0
depth = 0

for line in f1:
    line = line.strip("\n").split()
    if line[0] == 'forward':
        hor += int(line[1])
    elif line[0] == 'down':
        depth += int(line[1])
    elif line[0] == 'up':
        depth -= int(line[1])

print(depth * hor)

#Part 2 Solution
f1 = open("day2.txt")

hor = 0
depth = 0
aim = 0

for line in f1:
    line = line.strip("\n").split()
    if line[0] == 'forward':
        hor += int(line[1])
        depth += int(line[1]) * aim
    elif line[0] == 'down':
        aim += int(line[1])
    elif line[0] == 'up':
        aim -= int(line[1])

print(depth * hor)
