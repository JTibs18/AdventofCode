# Part 1 Solution
f1 = open("day8.txt")

# parsing input
for line in f1:
    tree = line.strip().split(' ')

tree = [int(x) for x in tree]

# finding metadata entries for each node 
def findMetadataForNode(index):
    nodeMetadataCount = 0 
    numChildNodes = tree[index]
    numMetaData = tree[index + 1]
    index += 2 

    while numChildNodes: 
        childNodeMetadataCount, index = findMetadataForNode(index)
        nodeMetadataCount += childNodeMetadataCount
        numChildNodes -= 1 

    while numMetaData: 
        nodeMetadataCount += tree[index]
        index += 1 
        numMetaData -= 1

    return nodeMetadataCount, index 

print(findMetadataForNode(0)[0])

# Part 2 Solution
f1 = open("day8.txt")

# parsing input
for line in f1:
    tree = line.strip().split(' ')

tree = [int(x) for x in tree]

# finding metadata entries for each node 
def findMetadataForNode(index):
    nodeMetadataCount = 0 
    numChildNodes = tree[index]
    numMetaData = tree[index + 1]
    childNodes = []
    index += 2 

    while numChildNodes: 
        childNodeMetadataCount, index = findMetadataForNode(index)
        childNodes.append(childNodeMetadataCount)
        numChildNodes -= 1 
    
    if len(childNodes) > 0:
        while numMetaData: 
            if tree[index] <= len(childNodes) and tree[index] != 0:
                nodeMetadataCount += childNodes[tree[index] - 1]
            index += 1 
            numMetaData -= 1 
    else: 
        while numMetaData: 
            nodeMetadataCount += tree[index]
            index += 1 
            numMetaData -= 1 

    return nodeMetadataCount, index 

print(findMetadataForNode(0)[0])