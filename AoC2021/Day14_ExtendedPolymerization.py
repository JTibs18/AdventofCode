# Part 1 Solution
f1 = open("day14.txt")

polymerTemplate = ""
insertionRules = dict()
commonElements = dict()
STEPS = 10
minQuantity = 1000000000
maxQuantity = 0

for line in f1:
    if polymerTemplate == "": 
        polymerTemplate = line.strip()
    elif line != "\n": 
        rules = line.strip().split(" -> ")
        insertionRules[rules[0]] = rules[1]
    
while STEPS: 
    temp = ""
    ptr1 = 0
    ptr2 = 1 
    
    while ptr2 < len(polymerTemplate): 
        checkPair = polymerTemplate[ptr1] + polymerTemplate[ptr2]
        if checkPair in insertionRules:
            temp += polymerTemplate[ptr1] + insertionRules[checkPair] 
        else: 
            temp += polymerTemplate[ptr1]
        
        ptr1 += 1
        ptr2 += 1
    
    temp += polymerTemplate[ptr2 - 1]
    polymerTemplate = temp
    STEPS -= 1 

for i in polymerTemplate: 
    if i in commonElements: 
        commonElements[i] += 1
    else:
        commonElements[i] = 1 

for key, value in commonElements.items(): 
    if value < minQuantity: 
        minQuantity = value 
    if value > maxQuantity: 
        maxQuantity = value

print(maxQuantity - minQuantity)

# Part 2 Solution # TOO SLOW
f1 = open("day14.txt")

polymerTemplate = ""
insertionRules = dict()
commonElements = dict()
STEPS = 10 
minQuantity = 1000000000
maxQuantity = 0

for line in f1:
    if polymerTemplate == "": 
        polymerTemplate = line.strip()
    elif line != "\n": 
        rules = line.strip().split(" -> ")
        insertionRules[rules[0]] = rules[1]
    
while STEPS: 
    temp = ""
    ptr1 = 0
    ptr2 = 1 
    
    while ptr2 < len(polymerTemplate): 
        checkPair = polymerTemplate[ptr1] + polymerTemplate[ptr2]
        if checkPair in insertionRules:
            temp += polymerTemplate[ptr1] + insertionRules[checkPair] 
        else: 
            temp += polymerTemplate[ptr1]
        
        ptr1 += 1
        ptr2 += 1
    
    temp += polymerTemplate[ptr2 - 1]
    polymerTemplate = temp
    STEPS -= 1 

for i in polymerTemplate: 
    if i in commonElements: 
        commonElements[i] += 1
    else:
        commonElements[i] = 1 

for key, value in commonElements.items(): 
    if value < minQuantity: 
        minQuantity = value 
    if value > maxQuantity: 
        maxQuantity = value

print((maxQuantity * 4) - (minQuantity * 4))

#12232 is too low 