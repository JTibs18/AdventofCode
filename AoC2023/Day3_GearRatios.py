# Part 1 Solution  
f1 = open("day3.txt")

numCoords = dict()
symbolCoords = dict()
grid = []
partNumSum = 0

for line in f1:
    grid.append(line.strip())

for indxY, line in enumerate(grid): 
    curNum = ''
    for indxX, val in enumerate(line): 
        if val.isnumeric(): 
            curNum += val
            if (indxX + 1 < len(line) and line[indxX + 1].isnumeric() == False) or indxX + 1 >= len(line):
                for i in range(len(curNum)):
                    numCoords[(indxX - i, indxY)] = int(curNum)
                curNum = ''
        elif val != ".":
            if val not in symbolCoords:
                symbolCoords[val] = [(indxX, indxY)]
            else:
                symbolCoords[val].append((indxX, indxY))

for values in symbolCoords.values():
    for valX, valY in values:
        counted = set()

        if ((valX + 1, valY) in numCoords and numCoords[(valX + 1, valY)] not in counted): 
            partNumSum += numCoords[(valX + 1, valY)]
            counted.add(numCoords[(valX + 1, valY)])
        
        if ((valX + 1, valY + 1) in numCoords and numCoords[(valX + 1, valY + 1)] not in counted): 
            partNumSum += numCoords[(valX + 1, valY + 1)]
            counted.add(numCoords[(valX + 1, valY + 1)])
        
        if ((valX, valY + 1) in numCoords and numCoords[(valX, valY + 1)] not in counted):
            partNumSum += numCoords[(valX, valY + 1)]
            counted.add(numCoords[(valX, valY + 1)])
        
        if ((valX - 1, valY - 1) in numCoords and numCoords[(valX - 1, valY - 1)] not in counted):
            partNumSum += numCoords[(valX - 1, valY - 1)]
            counted.add(numCoords[(valX - 1, valY - 1)])
        
        if ((valX - 1, valY) in numCoords and numCoords[(valX - 1, valY)] not in counted):
            partNumSum += numCoords[(valX - 1, valY)]
            counted.add(numCoords[(valX - 1, valY)])
        
        if ((valX, valY - 1) in numCoords and numCoords[(valX, valY - 1)] not in counted):
            partNumSum += numCoords[(valX, valY - 1)]
            counted.add(numCoords[(valX, valY - 1)])
        
        if ((valX - 1, valY + 1) in numCoords and numCoords[(valX - 1, valY + 1)] not in counted):
            partNumSum += numCoords[(valX - 1, valY + 1)]
            counted.add(numCoords[(valX - 1, valY + 1)])
        
        if ((valX + 1, valY - 1) in numCoords and numCoords[(valX + 1, valY - 1)] not in counted):
            partNumSum += numCoords[(valX + 1, valY - 1)]
            counted.add(numCoords[(valX + 1, valY - 1)])

print(partNumSum)

# Part 2 Solution  
f1 = open("day3.txt")

numCoords = dict()
symbolCoords = dict()
grid = []
sumGearRatios = 0

for line in f1:
    grid.append(line.strip())

for indxY, line in enumerate(grid): 
    curNum = ''
    for indxX, val in enumerate(line): 
        if val.isnumeric(): 
            curNum += val
            if (indxX + 1 < len(line) and line[indxX + 1].isnumeric() == False) or indxX + 1 >= len(line):
                for i in range(len(curNum)):
                    numCoords[(indxX - i, indxY)] = int(curNum)
                curNum = ''
        elif val == "*":
            if val not in symbolCoords:
                symbolCoords[val] = [(indxX, indxY)]
            else:
                symbolCoords[val].append((indxX, indxY))

for values in symbolCoords.values():
    for valX, valY in values:
        counted = set()

        if ((valX + 1, valY) in numCoords and numCoords[(valX + 1, valY)] not in counted): 
            partNumSum += numCoords[(valX + 1, valY)]
            counted.add(numCoords[(valX + 1, valY)])
        
        if ((valX + 1, valY + 1) in numCoords and numCoords[(valX + 1, valY + 1)] not in counted): 
            partNumSum += numCoords[(valX + 1, valY + 1)]
            counted.add(numCoords[(valX + 1, valY + 1)])
        
        if ((valX, valY + 1) in numCoords and numCoords[(valX, valY + 1)] not in counted):
            partNumSum += numCoords[(valX, valY + 1)]
            counted.add(numCoords[(valX, valY + 1)])
        
        if ((valX - 1, valY - 1) in numCoords and numCoords[(valX - 1, valY - 1)] not in counted):
            partNumSum += numCoords[(valX - 1, valY - 1)]
            counted.add(numCoords[(valX - 1, valY - 1)])
        
        if ((valX - 1, valY) in numCoords and numCoords[(valX - 1, valY)] not in counted):
            partNumSum += numCoords[(valX - 1, valY)]
            counted.add(numCoords[(valX - 1, valY)])
        
        if ((valX, valY - 1) in numCoords and numCoords[(valX, valY - 1)] not in counted):
            partNumSum += numCoords[(valX, valY - 1)]
            counted.add(numCoords[(valX, valY - 1)])
        
        if ((valX - 1, valY + 1) in numCoords and numCoords[(valX - 1, valY + 1)] not in counted):
            partNumSum += numCoords[(valX - 1, valY + 1)]
            counted.add(numCoords[(valX - 1, valY + 1)])
        
        if ((valX + 1, valY - 1) in numCoords and numCoords[(valX + 1, valY - 1)] not in counted):
            partNumSum += numCoords[(valX + 1, valY - 1)]
            counted.add(numCoords[(valX + 1, valY - 1)])
        
        if len(counted) == 2:
            c = list(counted)
            sumGearRatios += c[0] * c[1]

print(sumGearRatios)
    