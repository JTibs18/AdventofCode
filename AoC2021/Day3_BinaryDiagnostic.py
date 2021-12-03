#Part 1 Solution
f1 = open("day3.txt")

ones = [0,0,0,0,0,0,0,0,0,0,0,0]
gamma = ""
epsilon = ""
count = 0

for line in f1:
    line = line.strip("\n")
    for i, val in enumerate(str(line)):
        if val == "1":
            ones[i] += 1
    count += 1

for i in ones:
    if i > (count / 2):
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print(int(gamma, 2) * int(epsilon, 2))


#Part 2 Solution
f1 = open("day3.txt")

ones = [0,0,0,0,0,0,0,0,0,0,0,0]
count = 0
og = []
co2 = []

for line in f1:
    line = line.strip("\n")
    og.append(str(line))
    co2.append(str(line))

while len(og) > 1 and count < 12:

    for i in og:
        if i[count] == "1":
            ones[count] += 1

    if ones[count] >= (len(og) / 2):
        cur = "1"
    else:
        cur = "0"

    og = [x for x in og if x[count] != cur]
    count += 1

count = 0
ones = [0,0,0,0,0,0,0,0,0,0,0,0]

while len(co2) > 1 and count < 12:

    for i in co2:
        if i[count] == "1":
            ones[count] += 1

    if ones[count] < (len(co2) / 2):
        cur = "1"
    else:
        cur = "0"

    co2 = [x for x in co2 if x[count] != cur]
    count += 1

print(int(og[0], 2) * int(co2[0], 2))
