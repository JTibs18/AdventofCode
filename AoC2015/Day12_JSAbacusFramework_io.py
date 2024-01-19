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
curNumber = ""
isNegative = False
skip = False
stack = []
curNums = []

for line in f1:
    for indx, val in enumerate(line):
        if val.isnumeric():
            curNumber = curNumber + val
        elif val == "[" or val == "{":
            stack.append(val)
            curNums.append(0)
        elif val == "r" and line[indx + 1] == "e" and line[indx + 2] == "d":
            if stack[-1] == "{":
                skip = True
                stack.append("R") 
        elif val == "-":
            isNegative = True
        elif val == "," and len(curNumber) > 0:
            if isNegative == True:
                curNums[-1] -= int(curNumber)
            else:
                curNums[-1] += int(curNumber)
            curNumber = ""
            isNegative = False
        elif val == "]" or val == "}":
            if len(curNumber) > 0: 
                if isNegative == True:
                    curNums[-1] -= int(curNumber)
                else:
                    curNums[-1] += int(curNumber)

            if skip == False:
                if len(curNums) > 1:
                    x = curNums.pop()
                    curNums[-1] += x
                else:
                    numCount += curNums.pop()
            else:
                curNums.pop()
            
            curNumber = ""
            isNegative = False

            if stack[-1] == "R":
                stack.pop()
            
            if "R" not in stack:
                skip = False
       
            stack.pop()

print(numCount)
