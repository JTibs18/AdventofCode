#Part 1 Solution
f1 = open("day2.txt")
val = 0

for line in f1:

        letterCount = 0
        line = line.rstrip()
        curPass = line.split()

        for j, letters in enumerate(curPass[2]):
            if (letters == curPass[1][0]):
                letterCount = letterCount + 1

        minMax = curPass[0].split("-")

        if ((letterCount >= int(minMax[0])) and (letterCount <= int(minMax[1]))):
            val = val + 1

print(val)

#Part 2 Solution
f1 = open("day2.txt")
val = 0

for line in f1:

        letterCount = 0
        line = line.rstrip()
        curPass = line.split()
        minMax = curPass[0].split("-")

        for j, letters in enumerate(curPass[2]):
            if ((letters == curPass[1][0]) and ((j + 1) == int(minMax[0]) or (j + 1) == int(minMax[1]))):
                letterCount = letterCount + 1

        if letterCount == 1:
            val = val + 1

print (val)
