#Part 1 Solution 
f1 = open("day6.txt") 
onLights = set()
for line in f1: 
    line = line.rstrip() 
    if "turn off" in line: 
        instruction = line[9: len(line)]
        instruction = instruction.split(" through ")
        start = instruction[0].split(",")
        end = instruction[1].split(",")
        for i in range (int(start[0]), int(end[0]) + 1):
            for j in range (int(start[1]), int(end[1]) + 1):
                onLights.discard((i, j))        
    elif "turn on" in line: 
        instruction = line[8: len(line)]
        instruction = instruction.split(" through ")
        start = instruction[0].split(",")
        end = instruction[1].split(",")
        for i in range (int(start[0]), int(end[0]) + 1):
            for j in range (int(start[1]), int(end[1]) + 1):
                onLights.add((i, j))  
    elif "toggle" in line: 
        instruction = line[7: len(line)]
        instruction = instruction.split(" through ")
        start = instruction[0].split(",")
        end = instruction[1].split(",")
        for i in range (int(start[0]), int(end[0]) + 1):
            for j in range (int(start[1]), int(end[1]) + 1):
                newSet = (i, j)
                if newSet in onLights: 
                    onLights.discard((i, j)) 
                else: 
                    onLights.add((i, j))  
print (len(onLights))

#Part 2 Solution 
f1 = open("day6.txt") 
onLights ={}
for line in f1: 
    line = line.rstrip() 
    if "turn off" in line: 
        instruction = line[9: len(line)]
        instruction = instruction.split(" through ")
        start = instruction[0].split(",")
        end = instruction[1].split(",")
        for i in range (int(start[0]), int(end[0]) + 1):
            for j in range (int(start[1]), int(end[1]) + 1):
                newSet = (i, j)
                if newSet not in onLights: 
                    onLights[newSet] = 0
                elif newSet in onLights and onLights.get(newSet) != 0:
                    val = onLights.get(newSet)
                    onLights[newSet]= val - 1        
    elif "turn on" in line: 
        instruction = line[8: len(line)]
        instruction = instruction.split(" through ")
        start = instruction[0].split(",")
        end = instruction[1].split(",")
        for i in range (int(start[0]), int(end[0]) + 1):
            for j in range (int(start[1]), int(end[1]) + 1):
                newSet = (i, j)
                if newSet not in onLights: 
                    onLights[newSet] = 1 
                else: 
                    val = onLights.get(newSet)
                    onLights[newSet]= val + 1 
    elif "toggle" in line: 
        instruction = line[7: len(line)]
        instruction = instruction.split(" through ")
        start = instruction[0].split(",")
        end = instruction[1].split(",")
        for i in range (int(start[0]), int(end[0]) + 1):
            for j in range (int(start[1]), int(end[1]) + 1):
                newSet = (i, j)
                if newSet not in onLights: 
                    onLights[newSet] = 2 
                else: 
                    val = onLights.get(newSet)
                    onLights[newSet]= val + 2
brightness = onLights.values()
bTotal = 0
for i in brightness: 
    bTotal = bTotal + i 
print (bTotal)