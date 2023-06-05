# Part 1 Solution
f1 = open("day20.txt")

encryptedNums = []
numberToPositionMap = dict()
indx = 0
sum = 0 
numCount = 0
indxKeys = []

for line in f1:
    num = line.strip()
    encryptedNums.append(int(num))
    numberToPositionMap[(int(num), indx)] = indx
    indx += 1 

maxIndx = len(encryptedNums) - 1

for index, val in enumerate(encryptedNums): 
    previousIndx = numberToPositionMap[(val, index)]
    
    if val != 0: 
        newIndx = previousIndx + val 
    else: 
        newIndx = previousIndx
    
    if newIndx > maxIndx or newIndx < 0: 
        newIndx = maxIndx - (abs(newIndx) % maxIndx)
    if newIndx == 0: 
        newIndx = maxIndx
    
    numberToPositionMap[(val, index)] = newIndx

    for i, num in enumerate(encryptedNums): 
        if (val, index) != (num, i) and newIndx - previousIndx > 0 and numberToPositionMap[(num, i)] >= previousIndx and numberToPositionMap[(num, i)] <= newIndx: 
            if numberToPositionMap[(num, i)] - 1 < 0: 
                numberToPositionMap[(num, i)] = maxIndx - (abs(numberToPositionMap[(num, i)] - newIndx) % maxIndx)  
            else: 
                numberToPositionMap[(num, i)] -= 1 
        elif (val, index) != (num, i) and newIndx - previousIndx < 0 and numberToPositionMap[(num, i)] <= previousIndx and numberToPositionMap[(num, i)] >= newIndx: 
            if numberToPositionMap[(num, i)] + 1 > maxIndx: 
                numberToPositionMap[(num, i)] = maxIndx - (abs(numberToPositionMap[(num, i)] - newIndx) % maxIndx) 
            else: 
                numberToPositionMap[(num, i)] += 1
    print(numberToPositionMap)
        
print(numberToPositionMap)
for key in numberToPositionMap: 
    if key[0] == 0: 
        for i in range (1, 4): 
            findIndx = 1000 * i 
            if numberToPositionMap[key] + findIndx > maxIndx: 
                findIndx = (abs(numberToPositionMap[key] + findIndx) % (maxIndx + 1)) 
            indxKeys.append(findIndx) 

for key in numberToPositionMap: 
    if numberToPositionMap[key] in indxKeys: 
        sum += key[0]

print(sum)