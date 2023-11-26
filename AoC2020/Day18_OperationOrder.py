# Part 1 Solution
f1 = open("day18.txt")

def doMath(arr):
    total = int(arr[0])
    indx = 1

    while indx < len(arr):
        if arr[indx] == "+":
            total += int(arr[indx + 1])
        else: 
            total *= int(arr[indx + 1])
        indx += 2
    
    return total
            
lines = []
overallSum = 0

for line in f1:
    lines.append(line.strip().replace(" ", ""))

for mathEquation in lines: 
    stack = []
    
    for element in mathEquation:
        if element == ")":
            subEquation = []
            total = 0

            while stack and stack[-1] != "(":
                e = stack.pop()
                subEquation.append(e)
            
            stack.pop()

            subEquation = subEquation[::-1]
            total = doMath(subEquation)
            stack.append(total)

        else:
            stack.append(element)
    
    if len(stack) != 1:
        total = doMath(stack)

    overallSum += total

print(overallSum)

# Part 2 Solution
f1 = open("day18.txt")

def doMath2(arr):
    newArray = [int(arr[0])]
    indx = 1

    while indx < len(arr):
        if arr[indx] == "+":
            prev = newArray.pop()
            newArray.append(int(prev) + int(arr[indx + 1]))
            indx += 2
        else:
            newArray.append(arr[indx])
            indx += 1
    
    total = int(newArray[0])
    indx = 1
    
    while indx < len(newArray):
            if newArray[indx] == "*":
                total *= int(newArray[indx + 1])
                indx += 2
            else:
                indx += 1
    
    return total
            
lines = []
overallSum = 0

for line in f1:
    lines.append(line.strip().replace(" ", ""))

for mathEquation in lines: 
    stack = []
    
    for element in mathEquation:
        if element == ")":
            subEquation = []
            total = 0

            while stack and stack[-1] != "(":
                e = stack.pop()
                subEquation.append(e)
            
            stack.pop()

            subEquation = subEquation[::-1]
            total = doMath2(subEquation)
            stack.append(total)

        else:
            stack.append(element)
    
    if len(stack) != 1:
        total = doMath2(stack)

    overallSum += total

print(overallSum)