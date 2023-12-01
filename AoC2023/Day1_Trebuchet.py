# Part 1 Solution  
f1 = open("day1.txt")

total = 0

for line in f1:
    foundNums = []

    for char in line: 
        if char.isnumeric():
            foundNums.append(char)
        
    total += int(foundNums[0] + foundNums[-1])
    
print(total)

# Part 2 Solution  
f1 = open("day1.txt")

total = 0

for line in f1:
    foundNums = []
    
    for indx, char in enumerate(line): 
        if char.isnumeric():
            foundNums.append(char)
        elif char == "o" and indx + 2 <= len(line) and line[indx + 1] == "n" and line[indx + 2] == "e":
            foundNums.append("1")
        elif char == "t" and indx + 2 <= len(line) and line[indx + 1] == "w" and line[indx + 2] == "o":
            foundNums.append("2")
        elif char == "t" and indx + 4 <= len(line) and line[indx + 1] == "h" and line[indx + 2] == "r" and line[indx + 3] == "e" and line[indx + 4] == "e":
            foundNums.append("3")
        elif char == "f" and indx + 3 <= len(line) and line[indx + 1] == "o" and line[indx + 2] == "u" and line[indx + 3] == "r":
            foundNums.append("4")
        elif char == "f" and indx + 3 <= len(line) and line[indx + 1] == "i" and line[indx + 2] == "v" and line[indx + 3] == "e":
            foundNums.append("5")
        elif char == "s" and indx + 2 <= len(line) and line[indx + 1] == "i" and line[indx + 2] == "x":
            foundNums.append("6")
        elif char == "s" and indx + 4 <= len(line) and line[indx + 1] == "e" and line[indx + 2] == "v" and line[indx + 3] == "e" and line[indx + 4] == "n":
            foundNums.append("7")
        elif char == "e" and indx + 4 <= len(line) and line[indx + 1] == "i" and line[indx + 2] == "g" and line[indx + 3] == "h" and line[indx + 4] == "t":
            foundNums.append("8")
        elif char == "n" and indx + 3 <= len(line) and line[indx + 1] == "i" and line[indx + 2] == "n" and line[indx +3] == "e":
            foundNums.append("9")
        
    total += int(foundNums[0] + foundNums[-1])

print(total)