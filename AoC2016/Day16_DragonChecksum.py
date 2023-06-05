# Part 1 Solution
f1 = open("day16.txt")

def CheckSum(data): 
    ptr1 = 0
    ptr2 = 1 
    checkSum = ""
    
    while ptr2 < len(data): 
        pair = data[ptr1] + data[ptr2]
        if pair == "11" or pair == "00": 
            checkSum += "1"
        else: 
            checkSum += "0"
        ptr1 += 2
        ptr2 += 2
    return checkSum

DISK_LENGTH = 272

for line in f1:
    initialState = line.strip()

while len(initialState) < DISK_LENGTH: 
    b = initialState[:]
    b = b[::-1]
    for indx, val in enumerate(b): 
        if val == "0": 
            b = b[:indx] + "1" + b[indx + 1:]
        else: 
            b = b[:indx] + "0" + b[indx + 1:]
    
    initialState = initialState + "0" + b

initialState = initialState[:DISK_LENGTH]
checkSum = CheckSum(initialState)

while len(checkSum) % 2 == 0: 
    checkSum = CheckSum(checkSum)

print(checkSum)

# Part 2 Solution TOO SLOW
f1 = open("day16.txt")

def CheckSum2(data): 
    ptr1 = 0
    ptr2 = 1 
    checkSum = ""
    
    while ptr2 < len(data): 
        pair = data[ptr1] + data[ptr2]
        if pair == "11" or pair == "00": 
            checkSum += "1"
        else: 
            checkSum += "0"
        ptr1 += 2
        ptr2 += 2
    return checkSum

DISK_LENGTH = 35651584

for line in f1:
    initialState = line.strip()

while len(initialState) < DISK_LENGTH: 
    b = initialState[:]
    b = b[::-1]
    for indx, val in enumerate(b): 
        if val == "0": 
            b = b[:indx] + "1" + b[indx + 1:]
        else: 
            b = b[:indx] + "0" + b[indx + 1:]
    
    initialState = initialState + "0" + b

initialState = initialState[:DISK_LENGTH]
checkSum = CheckSum2(initialState)

while len(checkSum) % 2 == 0: 
    checkSum = CheckSum2(checkSum)

print(checkSum)