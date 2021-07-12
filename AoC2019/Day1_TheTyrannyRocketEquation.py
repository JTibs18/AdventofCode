#Part 1 Solution
f1 = open("day1.txt")

total = 0

for line in f1:
    line = line.strip("\n")
    total += (int(line) // 3) - 2
print(total)

#Part 2 Solution
f1 = open("day1.txt")
total = []

for line in f1:
    count = 0
    line = line.strip("\n")
    fuelAmount = (int(line) // 3) - 2

    while fuelAmount > 0:
        count += fuelAmount
        fuelAmount = (fuelAmount // 3) - 2
    total.append(count)
print(sum(total))
