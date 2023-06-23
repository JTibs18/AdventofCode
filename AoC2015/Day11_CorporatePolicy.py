#Part 1 Solution
f1 = open("day11.txt")

passwordAsNumbers = []
requirements = 0

# finding next number 
def findNextNumber(curPassword, index): 
    if curPassword[index] + 1 > 122: 
        curPassword[index] = 97
        return findNextNumber(curPassword, index - 1)
    else: 
        curPassword[index] += 1 
        return curPassword

# get current password
for line in f1: 
    currentPassword = line.strip()

# convert letters to numbers 
for letter in currentPassword:
    passwordAsNumbers.append(ord(letter))

while requirements != 3: 
    requirements = 0 

    # requirement 1 
    for i in range(len(passwordAsNumbers) - 2): 
        if passwordAsNumbers[i] - passwordAsNumbers[i + 1] == -1 and passwordAsNumbers[i + 1] - passwordAsNumbers[i + 2] == -1: 
            requirements += 1 
            break
 
    # requirement 2 
    if 105 not in passwordAsNumbers and 108 not in passwordAsNumbers and 111 not in passwordAsNumbers: 
        requirements += 1 

    # requirement 3 
    ptr1 = 0
    ptr2 = 1
    doubleLetterCount = 0 
    while ptr2 < len(passwordAsNumbers): 
        if passwordAsNumbers[ptr1] == passwordAsNumbers[ptr2]: 
            doubleLetterCount += 1 
            ptr1 = ptr2 + 1
            ptr2 = ptr1 + 1 
        else: 
            ptr1 += 1
            ptr2 += 1 

    if doubleLetterCount >= 2: 
        requirements += 1 

    # increase old password 
    if requirements != 3: 
        passwordAsNumbers = findNextNumber(passwordAsNumbers, 7)

# convert back to letters 
nextPassword = ''
for i in passwordAsNumbers: 
    nextPassword += chr(i)

print(nextPassword)

#Part 2 Solution
f1 = open("day11.txt")

passwordAsNumbers = []
passwordFound = 0 

# finding next number 
def findNextNumber(curPassword, index): 
    if curPassword[index] + 1 > 122: 
        curPassword[index] = 97
        return findNextNumber(curPassword, index - 1)
    else: 
        curPassword[index] += 1 
        return curPassword

# get current password
for line in f1: 
    currentPassword = line.strip()

# convert letters to numbers 
for letter in currentPassword:
    passwordAsNumbers.append(ord(letter))

while passwordFound < 2: 
    requirements = 0 

    # requirement 1 
    for i in range(len(passwordAsNumbers) - 2): 
        if passwordAsNumbers[i] - passwordAsNumbers[i + 1] == -1 and passwordAsNumbers[i + 1] - passwordAsNumbers[i + 2] == -1: 
            requirements += 1 
            break
 
    # requirement 2 
    if 105 not in passwordAsNumbers and 108 not in passwordAsNumbers and 111 not in passwordAsNumbers: 
        requirements += 1 

    # requirement 3 
    ptr1 = 0
    ptr2 = 1
    doubleLetterCount = 0 
    while ptr2 < len(passwordAsNumbers): 
        if passwordAsNumbers[ptr1] == passwordAsNumbers[ptr2]: 
            doubleLetterCount += 1 
            ptr1 = ptr2 + 1
            ptr2 = ptr1 + 1 
        else: 
            ptr1 += 1
            ptr2 += 1 

    if doubleLetterCount >= 2: 
        requirements += 1 

    # increase old password 
    if requirements == 3: 
        passwordFound += 1 

    if passwordFound != 2: 
        passwordAsNumbers = findNextNumber(passwordAsNumbers, 7)

# convert back to letters 
nextPassword = ''
for i in passwordAsNumbers: 
    nextPassword += chr(i)

print(nextPassword)