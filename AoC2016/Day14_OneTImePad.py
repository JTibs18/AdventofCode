# Part 1 Solution
import hashlib

f1 = open("day14.txt")

hashNumber = 0 
toHash = 1000 
foundKeys = list()
tripletIndex = dict() 

for line in f1:
    salt = line.strip()

while hashNumber <= toHash: 
    stringToHash = salt + str(hashNumber)
    hashedString = hashlib.md5(stringToHash.encode('utf-8')).hexdigest()

    # testing three of the same characters in a row
    indx1 = 0 
    indx2 = 3
    
    while indx2 <= len(hashedString):
        if all(c == hashedString[indx1] for c in hashedString[indx1:indx2]): 
            if hashedString[indx1] in tripletIndex: 
                tripletIndex[hashedString[indx1]].append(hashNumber)
            else: 
                tripletIndex[hashedString[indx1]] = [hashNumber]

            if len(foundKeys) < 64:
                toHash = hashNumber + 1000
            
            break
        
        indx1 += 1
        indx2 += 1 

    # testing five of the same characters in a row
    indx1 = 0 
    indx2 = 5
    
    while indx2 <= len(hashedString):
        if all(c == hashedString[indx1] for c in hashedString[indx1:indx2]) and hashedString[indx1] in tripletIndex: 
            for i in tripletIndex[hashedString[indx1]]: 
                if i + 1000 > hashNumber and i != hashNumber and i not in foundKeys: 
                    foundKeys.append(i) 
        
        indx1 += 1
        indx2 += 1 

    hashNumber += 1 

sortedFoundKeys = sorted(list(foundKeys))
print(sortedFoundKeys[63])

# Part 2 Solution (takes about a minute to run)
import hashlib

f1 = open("day14.txt")

hashNumber = 0 
toHash = 1000 
foundKeys = list()
tripletIndex = dict() 

for line in f1:
    salt = line.strip()

while hashNumber <= toHash: 
    hashedString = salt + str(hashNumber)
    
    for i in range(2017):
        hashedString = hashlib.md5(hashedString.encode('utf-8')).hexdigest()

    # testing three of the same characters in a row
    indx1 = 0 
    indx2 = 3
    
    while indx2 <= len(hashedString):
        if all(c == hashedString[indx1] for c in hashedString[indx1:indx2]): 
            if hashedString[indx1] in tripletIndex: 
                tripletIndex[hashedString[indx1]].append(hashNumber)
            else: 
                tripletIndex[hashedString[indx1]] = [hashNumber]

            if len(foundKeys) < 64:
                toHash = hashNumber + 1000
            
            break
        
        indx1 += 1
        indx2 += 1 

    # testing five of the same characters in a row
    indx1 = 0 
    indx2 = 5
    
    while indx2 <= len(hashedString):
        if all(c == hashedString[indx1] for c in hashedString[indx1:indx2]) and hashedString[indx1] in tripletIndex: 
            for i in tripletIndex[hashedString[indx1]]: 
                if i + 1000 > hashNumber and i != hashNumber and i not in foundKeys: 
                    foundKeys.append(i) 
        
        indx1 += 1
        indx2 += 1 

    hashNumber += 1 

sortedFoundKeys = sorted(list(foundKeys))
print(sortedFoundKeys[63])