# Part 1 Solution
f1 = open("day8.txt")

def findTreeVisible(X, Y):
    visible = False 
    if (Y > 0):
        for i in range(0, Y): 
            if trees[Y][X] > trees[i][X]:
                visible = True 
            else: 
                visible = False 
                break 
        if visible == True: 
            return 1
    if (X > 0):
        for i in range(0, X): 
            if trees[Y][X] > trees[Y][i]:
                visible = True 
            else: 
                visible = False 
                break 
        if visible == True: 
            return 1
    if (X < len(trees[0]) - 1):
        for i in range(X + 1, len(trees)): 
            if trees[Y][X] > trees[Y][i]:
                visible = True 
            else: 
                visible = False 
                break 
        if visible == True: 
            return 1
    if (Y < len(trees) - 1):
        for i in range(Y + 1, len(trees[0])): 
            if trees[Y][X] > trees[i][X]:
                visible = True 
            else: 
                visible = False 
                break 
        if visible == True: 
            return 1

    return 0

trees = []
visibleCount = 0

for line in f1:
    treeLine = []
    for i in line.strip(): 
        treeLine.append(int(i))
    trees.append(treeLine)

for indx, treeLine in enumerate(trees): 
        for index, j in enumerate(treeLine): 
            if (index == 0 or index == len(treeLine) - 1) or (indx == 0 or indx == len(trees) - 1):
                visibleCount += 1
            else: 
                visibleCount += findTreeVisible(index, indx)

print(visibleCount)

# Part 2 Solution
f1 = open("day8.txt")

def findTreeScore(X, Y):
    viewingDistance = []
    if (Y > 0):
        upView = 0
        for i in range(Y - 1 , -1, -1):
            if trees[Y][X] > trees[i][X]:
                upView += 1
            else: 
                upView += 1
                break 
        viewingDistance.append(upView)  
    if (X > 0):
        leftView = 0
        for i in range(X - 1, -1, -1): 
            if trees[Y][X] > trees[Y][i]:
                leftView += 1
            else: 
                leftView += 1
                break 
        viewingDistance.append(leftView)  
    if (X < len(trees[0]) - 1):
        rightView = 0 
        for i in range(X + 1, len(trees[0])): 
            if trees[Y][X] > trees[Y][i]:
                rightView += 1
            else: 
                rightView += 1
                break 
        viewingDistance.append(rightView)  
    if (Y < len(trees) - 1):
        downView = 0
        for i in range(Y + 1, len(trees)): 
            if trees[Y][X] > trees[i][X]:
                downView += 1
            else: 
                downView += 1
                break
        viewingDistance.append(downView)  
    
    return viewingDistance 

trees = []
highestTreeCount = 0 

for line in f1:
    treeLine = []
    for i in line.strip(): 
        treeLine.append(int(i))
    trees.append(treeLine)

for indx, treeLine in enumerate(trees): 
        for index, j in enumerate(treeLine): 
            viewingDist = findTreeScore(index, indx)
            totalDist = 1
            for i in viewingDist: 
                totalDist = totalDist * i 
            if totalDist > highestTreeCount: 
                highestTreeCount = totalDist

print(highestTreeCount)