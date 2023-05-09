#Part 1 Solution
f1 = open("day8.txt")

appearanceCount = 0 
digitOutputValues = [2, 4, 3, 7]

for line in f1:
    results = line.strip().split(" | ")
    outputValLine = results[1].split(" ")

    for i in outputValLine: 
        if len(i) in digitOutputValues: 
            appearanceCount += 1 
    
print(appearanceCount)

#Part 2 Solution
f1 = open("day8.txt")

totalOutputValue = 0 

for line in f1:
    numMapping = dict() 
    wordToNumMapping = dict() 
    sixLetters = [] 
    fiveLetters = [] 
    num = ""

    results = line.strip().split(" | ")
    inputVal = results[0].split(" ")
    outputValLine = results[1].split(" ")
    
    for i in inputVal: 
        if len(i) == 2: 
            numMapping["1"] = i 
            wordToNumMapping[''.join(sorted(i))] = "1"
        if len(i) == 4: 
            numMapping["4"] = i 
            wordToNumMapping[''.join(sorted(i))] = "4"
        if len(i) == 7:
            numMapping["8"] = i
            wordToNumMapping[''.join(sorted(i))] = "8"
        if len(i) == 3:
            numMapping["7"] = i 
            wordToNumMapping[''.join(sorted(i))] = "7"
        if len(i) == 5: 
            fiveLetters.append(i)
        if len(i) == 6: 
            sixLetters.append(i)

    for i in sixLetters: 
        if len(list(set(numMapping["4"]) & set(i))) == 4:
            numMapping["9"] = i 
            wordToNumMapping[''.join(sorted(i))] = "9"
        elif len(list(set(numMapping["1"]) & set(i))) == 2: 
            numMapping["0"] = i 
            wordToNumMapping[''.join(sorted(i))] = "0"
        else: 
            numMapping["6"] = i 
            wordToNumMapping[''.join(sorted(i))] = "6"
    
    for i in numMapping["8"]: 
        if i not in numMapping["9"]:
            missingLetter = i
            
    for i in fiveLetters: 
        if len(list(set(numMapping["1"]) & set(i))) == 2:
            numMapping["3"] = i 
            wordToNumMapping[''.join(sorted(i))] = "3"
        elif missingLetter in i: 
            numMapping["2"] = i 
            wordToNumMapping[''.join(sorted(i))] = "2"
        else: 
            numMapping["5"] = i 
            wordToNumMapping[''.join(sorted(i))] = "5" 
            
    for i in outputValLine: 
        num += wordToNumMapping[''.join(sorted(i))]
    
    totalOutputValue += int(num)
            
print(totalOutputValue)