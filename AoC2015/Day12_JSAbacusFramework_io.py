#Part 1 Solution
f1 = open("day12.txt")

numCount = 0
isNegative = False
curNumber = ""

for line in f1:
    for i in line:
        if i.isnumeric():
            curNumber = curNumber + i
        elif i == "-":
            isNegative = True
        elif (i == "]" or i == "}" or i == ",") and len(curNumber) > 0:
            if isNegative == True:
                numCount -= int(curNumber)
            else:
                numCount += int(curNumber)
            curNumber = ""
            isNegative = False

print(numCount)

#Part 2 Solution
f1 = open("day12.txt")

numCount = 0
totalNum = 0
bracketCount = 0
isNegative = False
curNumber = ""
spellRed = ""
lastBracket = ""
isRed = False

for line in f1:
    for i in line:
        if i.isnumeric():
            curNumber = curNumber + i
        elif i == "[" or i == "{":
            bracketCount += 1
            lastBracket = i
        elif i == "r" or i == "e" or i == "d":
            spellRed = spellRed + i
        elif i == "-":
            isNegative = True
        elif i == "]" or i == "}" or i == ",":
            if isNegative == True and len(curNumber) > 0:
                numCount -= int(curNumber)
            elif len(curNumber) > 0:
                numCount += int(curNumber)
            if i == "]" or i == "}":
                bracketCount -= 1
            curNumber = ""
            isNegative = False

        if "red" in spellRed and lastBracket == "[":
            spellRed == ''
        elif "red" in spellRed and lastBracket == "{":
            isRed = True
            spellRed == ''

        if bracketCount == 0 and isRed == False:
            totalNum += numCount
            numCount = 0
        elif bracketCount == 0 and isRed == True:
            isRed = False
            numCount = 0

print(totalNum)
