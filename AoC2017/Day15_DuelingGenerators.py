# Part 1 Solution (takes a few minutes)
f1 = open("day15.txt")

a = ''
b = ''
matchCount = 0

for line in f1:
    input = line.strip().split(' ')
    if a == '':
        a = int(input[4])
    else:
        b = int(input[4])

for i in range(0, 40000000):
    a = (a * 16807) % 2147483647
    b = (b * 48271) % 2147483647
    binaryA = "{0:032b}".format(a)
    binaryB = "{0:032b}".format(b)

    if binaryA[16:] == binaryB[16:]:
        matchCount += 1

print(matchCount)

# Part 2 Solution (takes a minute)
f1 = open("day15.txt")

a = ''
b = ''
valueA = ''
valueB = ''
matchCount = 0

for line in f1:
    input = line.strip().split(' ')
    if a == '':
        a = int(input[4])
    else:
        b = int(input[4])

for i in range(0, 5000000):
    while valueA == '':
        a = (a * 16807) % 2147483647

        if a % 4 == 0:
            valueA = a

    while valueB == '':
        b = (b * 48271) % 2147483647

        if b % 8 == 0:
            valueB = b

    if valueA != '' and valueB != '':
        binaryA = "{0:032b}".format(valueA)
        binaryB = "{0:032b}".format(valueB)

        if binaryA[16:] == binaryB[16:]:
            matchCount += 1

        valueA = ''
        valueB = ''

print(matchCount)
