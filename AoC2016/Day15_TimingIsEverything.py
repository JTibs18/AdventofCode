# Part 1 Solution
f1 = open("day15.txt")

discs = [] 
startingTime = 0 

for line in f1:
    parsed = line.strip().split(" ")    
    discs.append([int(parsed[3]), int(parsed[11].strip("."))])

while True: 
    time = startingTime + 1 
    passingDiscs = 1
    slot = -1 

    for numPositions, curPos in discs: 
        if time + curPos > numPositions: 
            newPosition = (time + curPos) % numPositions
        else: 
            newPosition = time + curPos
        
        if slot == -1: 
            slot = newPosition
        elif slot == newPosition: 
            passingDiscs += 1 
        else: 
            startingTime += 1 
            break 
        
        time += 1 
    
    if passingDiscs == len(discs): 
        print(startingTime)
        break 

# Part 2 Solution
f1 = open("day15.txt")

discs = [] 
startingTime = 0 

for line in f1:
    parsed = line.strip().split(" ")    
    discs.append([int(parsed[3]), int(parsed[11].strip("."))])

newDisk = [11, 0]
discs.append(newDisk)

while True: 
    time = startingTime + 1 
    passingDiscs = 1
    slot = -1 

    for numPositions, curPos in discs: 
        if time + curPos > numPositions: 
            newPosition = (time + curPos) % numPositions
        else: 
            newPosition = time + curPos
        
        if slot == -1: 
            slot = newPosition
        elif slot == newPosition: 
            passingDiscs += 1 
        else: 
            startingTime += 1 
            break 
        
        time += 1 
    
    if passingDiscs == len(discs): 
        print(startingTime)
        break 
