import copy
# Part 1 Solution
f1 = open("day9.txt")

def moveTail(prevHead, head, tail): 
    if head == tail or [head[0] - 1, head[1] + 1] == tail or [head[0] - 1, head[1]] == tail or [head[0] - 1, head[1] - 1] == tail or [head[0], head[1] + 1] == tail or [head[0], head[1] - 1] == tail or [head[0] + 1, head[1] + 1] == tail or [head[0] + 1, head[1]] == tail or [head[0] + 1, head[1] - 1] == tail:
        return tail 
    
    return prevHead 

head = [0,0]
tail = [0,0]
tailPositions = set()
motions = []
prevHead = head[:]

for line in f1:
    motions.append(line.strip().split(' '))

for i in motions: 
    for j in range(0, int(i[1])):
        prevHead = head[:]
        if i[0] == "R": 
            head[0] += 1
        elif i[0] == "L": 
            head[0] -= 1
        elif i[0] == "U": 
            head[1] += 1
        else: 
            head[1] -= 1
        
        tail = moveTail(prevHead, head, tail)
        tailPositions.add(f'{tail[0],tail[1]}')
       
print(len(tailPositions))

# Part 2 Solution
f1 = open("day9.txt")

def changeKnotPosition(prevPositions, knot, prevKnotPos, knots, direction): 
    if knots[prevKnotPos] == knot or [knots[prevKnotPos][0] - 1, knots[prevKnotPos][1] + 1] == knot or [knots[prevKnotPos][0] - 1, knots[prevKnotPos][1]] == knot or [knots[prevKnotPos][0] - 1, knots[prevKnotPos][1] - 1] == knot or [knots[prevKnotPos][0], knots[prevKnotPos][1] + 1] == knot or [knots[prevKnotPos][0], knots[prevKnotPos][1] - 1] == knot or [knots[prevKnotPos][0] + 1, knots[prevKnotPos][1] + 1] == knot or [knots[prevKnotPos][0] + 1, knots[prevKnotPos][1]] == knot or [knots[prevKnotPos][0] + 1, knots[prevKnotPos][1] - 1] == knot:
        return knot

    if knot[0] == knots[prevKnotPos][0]: 
        knot[1] += knots[prevKnotPos][1] - prevPositions[prevKnotPos][1]
    elif knot[1] == knots[prevKnotPos][1]:
        knot[0] += knots[prevKnotPos][0] - prevPositions[prevKnotPos][0]
    else: 
        if knots[prevKnotPos][1] - knot[1] > 0: 
            knot[1] += 1
        else: 
            knot[1] -= 1
      
        if knots[prevKnotPos][0] - knot[0] > 0: 
            knot[0] += 1
        else: 
            knot[0] -= 1
    return knot 

def moveKnot(direction, knot): 
    if direction == "R": 
        knot[0] += 1
    elif direction == "L": 
        knot[0] -= 1
    elif direction == "U": 
        knot[1] += 1
    else: 
        knot[1] -= 1
    return knot[:]

knots = [[0, 0] for y in range(10)]
tailPositions = set()
motions = []
prevPositions = copy.deepcopy(knots)

for line in f1:
    motions.append(line.strip().split(' '))

for i in motions: 
    for j in range(0, int(i[1])):
        prevPositions = copy.deepcopy(knots)
        knots[0] = moveKnot(i[0], knots[0])
        
        for indx, val in enumerate(knots): 
            if indx > 0:
                knots[indx] = changeKnotPosition(prevPositions, val, indx - 1, knots, i[0])
                if indx == len(knots) - 1: 
                    tailPositions.add(f'{knots[len(knots) - 1][0],knots[len(knots) - 1][1]}')
print(len(tailPositions))
