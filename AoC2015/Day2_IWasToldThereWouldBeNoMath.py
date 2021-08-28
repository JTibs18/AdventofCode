#Part 1 Solution
f1 = open("day2.txt") 

bigTotal = 0

for line in f1: 

    totalArea = 0
    surfaceA = []
    line = line.rstrip() 
    dimensions = line.split("x")        

    surfaceA.append(int(dimensions[0]) * int(dimensions[1]))
    surfaceA.append(int(dimensions[1]) * int(dimensions[2]))
    surfaceA.append(int(dimensions[0]) * int(dimensions[2])) 
        
    for i, area in enumerate(surfaceA):
        totalArea = (area * 2) + totalArea
    

    totalArea = (min(surfaceA)) + totalArea
    
    bigTotal = bigTotal + totalArea

print(bigTotal)

#Part 2 Solution
f1 = open("day2.txt") 

bigTotal = 0

for line in f1: 

    totalRibbon = 0
    distance = []
    line = line.rstrip() 
    dimensions = line.split("x")  

    distance.append((int(dimensions[0]) + int(dimensions[1])) * 2)
    distance.append((int(dimensions[1]) + int(dimensions[2])) * 2)
    distance.append((int(dimensions[0]) + int(dimensions[2])) * 2)
    bonusRib = (int(dimensions[0]) * int(dimensions[1]) * int(dimensions[2]))
    totalRibbon = min(distance) + bonusRib

    bigTotal = bigTotal + totalRibbon

print(bigTotal)