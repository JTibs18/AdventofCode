#Part 1 Solution
f1 = open("day9.txt")

decomp = 0
marker = False
skip = 0

for line in f1:
    line = line.strip("\n")

for indx, char in enumerate(line):
    if char == "(" and marker == False and skip == 0:
        marker = True
        mark = line[indx + 1:].split("x")
        skipVal = int(mark[0])
        multi = int(mark[1].split(")")[0])
        skip += skipVal
        decomp += skipVal * multi
    elif marker == True and char == ")":
        marker = False
    elif skip > 0 and marker == False:
        skip -= 1
    elif marker == False:
        decomp += 1
print(decomp)

#Part 2 Solution

#WORK ON THIS. OVER COUNTING BECAUSE MULTILYING BEFORE CONFIRMING NEXT CHARACTER NOT MARKER

f1 = open("day9.txt")

decomp = 0
marker = False
skip = 0

for line in f1:
    line = line.strip("\n")

for indx, char in enumerate(line):
    if char == "(" and marker == False:
        marker = True
        mark = line[indx + 1:].split("x")
        skipVal = int(mark[0])
        multi = int(mark[1].split(")")[0])

        if skip > 0:
            print("X", char)

            decomp += (multi * prevMulti)
            skip -= (line.find(")", indx) - indx) + 1
            if skip < 0:
                skip = 0
        else:
            print("Y", char)

            skip += skipVal
            decomp += skipVal * multi
    elif marker == True and char == ")":
        marker = False
        prevMulti = multi
    elif skip > 0 and marker == False:
        skip -= 1
    elif marker == False:
        #POSSIBLY DO MATH HERE
        decomp += 1
        print(char)

    print(decomp)
print(decomp)
