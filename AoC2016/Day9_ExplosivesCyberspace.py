#Part 1 Solution
f1 = open("day9.txt")

decompressedLength = 0
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
        decompressedLength += skipVal * multi
    elif marker == True and char == ")":
        marker = False
    elif skip > 0 and marker == False:
        skip -= 1
    elif marker == False:
        decompressedLength += 1
print(decompressedLength)

#Part 2 Solution
f1 = open("day9.txt")

decompressedLength = 0
marker = False
multipliers = dict()

for line in f1:
    line = line.strip("\n")

for indx, char in enumerate(line): 
    if char == "(": 
        marker = True 

        mark = line[indx + 1:].split("x")
        distance = int(mark[0])
        multi = int(mark[1].split(")")[0])
    elif char == ")": 
        marker = False 
        endLocation = distance + indx 

        if endLocation in multipliers:
            multipliers[endLocation] *= multi 
        else: 
            multipliers[endLocation] = multi 
    elif marker == False: 
        charMulti = 1 

        for key, value in multipliers.items(): 
            if indx <= key:
                charMulti *= value
        
        decompressedLength += charMulti

print(decompressedLength)  
