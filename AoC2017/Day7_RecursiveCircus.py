#Part 1 Solution
f1 = open("day7.txt")

programs = {}

for line in f1:
    line = line.strip().split("(")
    child = line[1].strip().split("> ")

    if "-" in line[1]:
        children = child[1].split(", ")
        parent = line[0].strip()
        
        if parent not in programs:
            programs[parent] = 0

        for i in children:
            programs[i] = 1

for key, value in programs.items():
    if value == 0:
        print(key)

#Part 2 Solution
f1 = open("day7.txt")

programsGraph = dict()
programsCount = dict()
programWeights = dict()

# parse input
for line in f1:
    line = line.strip().split("(")
    child = line[1].strip().split("> ")
    weight = int(line[1].split(")")[0])

    parent = line[0].strip()
    programWeights[parent] = weight
    
    if "-" in line[1]:
        children = child[1].split(", ")

        if parent not in programsGraph:
            programsGraph[parent] = children
            programsCount[parent] = 0
        
        for i in children:
            programs[i] = 1 

# find root 
for key, value in programs.items():
    if value == 0:
        root = key         

# find different weight 
def helper(curNode):
    if curNode not in programsGraph:
        return (programWeights[curNode], programWeights[curNode])
    
    weights = []

    for node in programsGraph[curNode]:
        res = helper(node)
        if res == None:
            return 
        
        weights.append(res)

    for totalWeight, _ in weights:
        if totalWeight != weights[0][0]:
            print(weights[0][1] - (weights[0][0] - totalWeight))
            return 
            
    return (sum([x[0] for x in weights]) + programWeights[curNode], programWeights[curNode])
        
helper(root)