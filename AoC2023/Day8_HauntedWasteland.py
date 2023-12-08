# #Part 1 Solution
f1 = open("day8.txt")

nodes = dict()
directions = []
start = "AAA"
end = "ZZZ"
curDirection = 0 
steps = 0 

for line in f1:
    if directions and line != "\n":
        parsed = line.strip().split(" = ")
        left, right = parsed[1].strip("()").split(", ")
        nodes[parsed[0]] = (left, right)
    elif line != "\n": 
        directions = list(line.strip())

while start != end:
    if directions[curDirection] == "L":
        start = nodes[start][0]  
    else: 
        start = nodes[start][1]
    
    curDirection += 1 
    steps += 1 

    if curDirection >= len(directions):
        curDirection = 0 
    
print(steps)

#Part 2 Solution
import math 
f1 = open("day8.txt")

nodes = dict()
directions = []
nodesWithA = []
steps = []
end = "Z"
totalSteps = 1

for line in f1:
    if directions and line != "\n":
        parsed = line.strip().split(" = ")
        left, right = parsed[1].strip("()").split(", ")
        nodes[parsed[0]] = (left, right)
        
        if parsed[0][2] == "A":
            nodesWithA.append(parsed[0])
    elif line != "\n": 
        directions = list(line.strip())

for start in nodesWithA: 
    curDirection = 0 
    curSteps = 0 

    while start[2] != end:
        if directions[curDirection] == "L":
            start = nodes[start][0]  
        else: 
            start = nodes[start][1]
        
        curDirection += 1 
        curSteps += 1 

        if curDirection >= len(directions):
            curDirection = 0 
    
    steps.append(curSteps)

print(math.lcm(*steps))
