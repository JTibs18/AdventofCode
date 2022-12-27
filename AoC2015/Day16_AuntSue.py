#Part 1 Solution
f1 = open("day16.txt")

sueList = [] 
giftSue = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}

for line in f1:
    sueDict = dict()
    sueSplit = line.strip().split(" ")
    sueDict[sueSplit[2].strip(":")] = int(sueSplit[3].strip(",")) 
    sueDict[sueSplit[4].strip(":")] = int(sueSplit[5].strip(","))
    sueDict[sueSplit[6].strip(":")] = int(sueSplit[7]) 
    sueList.append(sueDict)

for indx, val in enumerate(sueList):
    match = 0 
    for key, value in val.items(): 
        if giftSue[key] == value: 
            match += 1 
    
    if match == 3:
        print(indx + 1)

#Part 2 Solution
f1 = open("day16.txt")

sueList = [] 
giftSue = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}

for line in f1:
    sueDict = dict()
    sueSplit = line.strip().split(" ")
    sueDict[sueSplit[2].strip(":")] = int(sueSplit[3].strip(",")) 
    sueDict[sueSplit[4].strip(":")] = int(sueSplit[5].strip(","))
    sueDict[sueSplit[6].strip(":")] = int(sueSplit[7]) 
    sueList.append(sueDict)

for indx, val in enumerate(sueList):
    match = 0 
    for key, value in val.items(): 
        if key == "cats" or key == "trees": 
            if giftSue[key] < value: 
                match += 1 
        elif key == "pomeranians" or key == "goldfish": 
            if giftSue[key] > value:
                match += 1 
        else: 
            if giftSue[key] == value: 
                match += 1 
    
    if match == 3:
        print(indx + 1)