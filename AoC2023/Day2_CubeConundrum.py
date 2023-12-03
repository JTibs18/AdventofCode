# Part 1 Solution  
f1 = open("day2.txt")

redCubes = 12
greenCubes = 13
blueCubes = 14
idCount = 0 

for line in f1:
    id, line = line.strip().split(": ")
    id = int(id.split(" ")[1])
    subsets = line.split("; ")
    correct = 0 
    numCubes = 0
    
    for i in subsets: 
        cubes = i.split(", ")
        for c in cubes:
            numCubes += 1 
            count, color = c.split(" ")
            if color == 'red' and int(count) <= redCubes:
                correct += 1 
            elif color == 'blue' and int(count) <= blueCubes:
                correct += 1 
            elif color == "green" and int(count) <= greenCubes: 
                correct += 1 

    if numCubes == correct:
        idCount += id 

print(idCount)

# Part 2 Solution  
f1 = open("day2.txt")

sumOfPowerSets = 0 

for line in f1:
    id, line = line.strip().split(": ")
    subsets = line.split("; ")
    redCubes = 0
    greenCubes = 0
    blueCubes = 0
    
    for i in subsets: 
        cubes = i.split(", ")
        for c in cubes:
            count, color = c.split(" ")
            if color == 'red' and int(count) > redCubes:
                redCubes = int(count)
            elif color == 'blue' and int(count) > blueCubes:
                blueCubes = int(count)
            elif color == "green" and int(count) > greenCubes: 
                greenCubes = int(count) 

    sumOfPowerSets += redCubes * blueCubes * greenCubes

print(sumOfPowerSets)