#Part 1 Solution
f1 = open("day2.txt")

two = 0
three = 0

for line in f1:
    line = line.strip("\n")

    letter = {}
    for l in line:
        if l in letter:
            val = letter.get(l)
            letter[l] = val + 1
        else:
            letter[l] = 1
    if 2 in letter.values():
        two += 1
    if 3 in letter.values():
        three += 1
print(two * three)

#Part 2 Solution
f1 = open("day2.txt")

allLines = []

for line in f1:
    line = line.strip("\n")
    allLines.append(line)

for l in allLines:
    for x in allLines[allLines.index(l) + 1:]:
        letters = ""
        for indx, val in enumerate(l):
            off = False
            if val != x[indx] and off == False:
                off = True
            elif off == True:
                letters = ""
                break
            else:
                letters += val
        if len(letters) == len(x) - 1:
            print(letters)
