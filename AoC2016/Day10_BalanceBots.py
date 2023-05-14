#Part 1 Solution
import copy 
f1 = open("day10.txt")

instructions = dict() 
bots = dict() 
newBots = dict() 
iter = True 

# parsing input
for line in f1: 
    temp = line.strip().split(" ")
    
    if "value" in line: 
        if temp[5] in bots: 
            bots[temp[5]].append(int(temp[1]))
        else: 
            bots[temp[5]] = [int(temp[1])]
    else: 
        instructions[temp[1]] = [(temp[5], temp[6]), (temp[10], temp[11])]    

newBots = copy.deepcopy(bots)

# executing bots instructions 
while iter: 
    for key, value in bots.items(): 
        if len(value) == 2: 
            if 17 in value and 61 in value: 
                print(key)
                iter = False 
                break 
        
            if instructions[key][0][0] != "output":
                if instructions[key][0][1] in newBots: 
                    newBots[instructions[key][0][1]].append(min(value)) 
                else: 
                    newBots[instructions[key][0][1]] = [min(value)]
            
            if instructions[key][1][0] != "output":
                if instructions[key][1][1] in newBots: 
                    newBots[instructions[key][1][1]].append(max(value)) 
                else: 
                    newBots[instructions[key][1][1]] = [max(value)]

            newBots[key] = []

    bots = copy.deepcopy(newBots)

#Part 2 Solution
import copy 
f1 = open("day10.txt")

instructions = dict() 
bots = dict() 
outputBin = dict()
newBots = dict() 
iter = True 
outputFound = 0 

# parsing input
for line in f1: 
    temp = line.strip().split(" ")
    
    if "value" in line: 
        if temp[5] in bots: 
            bots[temp[5]].append(int(temp[1]))
        else: 
            bots[temp[5]] = [int(temp[1])]
    else: 
        instructions[temp[1]] = [(temp[5], temp[6]), (temp[10], temp[11])]    

newBots = copy.deepcopy(bots)

# executing bots instructions 
while outputFound < 3: 
    for key, value in bots.items(): 
        if len(value) == 2: 
            if instructions[key][0][0] != "output":
                if instructions[key][0][1] in newBots: 
                    newBots[instructions[key][0][1]].append(min(value)) 
                else: 
                    newBots[instructions[key][0][1]] = [min(value)]
            else:
                outputBin[instructions[key][0][1]] = min(value)
                
                if instructions[key][0][1] == "0" or instructions[key][0][1] == "1" or instructions[key][0][1] == "2": 
                    outputFound += 1  
            
            if instructions[key][1][0] != "output":
                if instructions[key][1][1] in newBots: 
                    newBots[instructions[key][1][1]].append(max(value)) 
                else: 
                    newBots[instructions[key][1][1]] = [max(value)]
            else: 
                outputBin[instructions[key][1][1]] = max(value)

                if instructions[key][1][1] == "0" or instructions[key][1][1] == "1" or instructions[key][1][1] == "2": 
                    outputFound += 1  

            newBots[key] = []

    bots = copy.deepcopy(newBots)

print(outputBin["0"] * outputBin["1"] * outputBin["2"])