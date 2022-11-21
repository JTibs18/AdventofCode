# Part 1 Solution
f1 = open("day5.txt")

message = []
index = 0
steps = 0

for line in f1:
    message.append(int(line.strip()))

while (index < len(message)):
    steps += 1
    jump = message[index]
    message[index] += 1
    index += jump

print(steps)

#Part 2 Solution
f1 = open("day5.txt")

message = []
index = 0
steps = 0

for line in f1:
    message.append(int(line.strip()))

while (index < len(message)):
    steps += 1
    jump = message[index]
    if jump >= 3:
        message[index] -= 1
    else:
        message[index] += 1
    index += jump

print(steps)
