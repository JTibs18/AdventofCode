# Part 1 Solution
f1 = open("day4.txt")

redundantElfCount = 0

for line in f1:
    pairRanges = line.strip().split(',')
    elfOne = pairRanges[0].split('-')
    elfTwo = pairRanges[1].split('-')

    if (int(elfOne[0]) >= int(elfTwo[0]) and int(elfOne[1]) <= int(elfTwo[1])) or (int(elfTwo[0]) >= int(elfOne[0]) and int(elfTwo[1]) <= int(elfOne[1])):
        redundantElfCount += 1

print(redundantElfCount)

# Part 2 Solution
f1 = open("day4.txt")

redundantElfCount = 0

for line in f1:
    pairRanges = line.strip().split(',')
    elfOne = pairRanges[0].split('-')
    elfTwo = pairRanges[1].split('-')

    for i in range(int(elfOne[0]), int(elfOne[1]) + 1):
        if int(elfTwo[0]) <= i and int(elfTwo[1]) >= i:
            redundantElfCount += 1
            break

print(redundantElfCount)
