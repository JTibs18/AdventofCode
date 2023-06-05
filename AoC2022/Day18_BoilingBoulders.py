# Part 1 Solution
f1 = open("day18.txt")
cubes = []
foundCubes = set()
sideCount = 0

for line in f1:
    cube = line.strip().split(',')
    cubes.append(cube)

for i in cubes: 
    sideCount += 6
    if (int(i[0]) + 1, int(i[1]), int(i[2])) in foundCubes: 
        sideCount -= 2
    if (int(i[0]) - 1, int(i[1]), int(i[2])) in foundCubes: 
        sideCount -= 2
    if (int(i[0]), int(i[1]) + 1, int(i[2])) in foundCubes: 
        sideCount -= 2
    if (int(i[0]), int(i[1]) - 1, int(i[2])) in foundCubes: 
        sideCount -= 2
    if (int(i[0]), int(i[1]), int(i[2]) + 1) in foundCubes: 
        sideCount -= 2
    if (int(i[0]), int(i[1]), int(i[2]) - 1) in foundCubes: 
        sideCount -= 2

    foundCubes.add((int(i[0]), int(i[1]), int(i[2])))

print(sideCount)

# Part 2 Solution
f1 = open("day18.txt")
cubes = []
foundCubes = set()
sideCount = 0
emptySpaceCount = 0
maxX = 0
maxY = 0 
maxZ = 0
minX = 100000000
minY = 100000000
minZ = 100000000

for line in f1:
    cube = line.strip().split(',')
    cubes.append(cube)

for i in cubes: 
    sideCount += 6
    if (int(i[0]) + 1, int(i[1]), int(i[2])) in foundCubes: 
        sideCount -= 2
    if (int(i[0]) - 1, int(i[1]), int(i[2])) in foundCubes: 
        sideCount -= 2
    if (int(i[0]), int(i[1]) + 1, int(i[2])) in foundCubes: 
        sideCount -= 2
    if (int(i[0]), int(i[1]) - 1, int(i[2])) in foundCubes: 
        sideCount -= 2
    if (int(i[0]), int(i[1]), int(i[2]) + 1) in foundCubes: 
        sideCount -= 2
    if (int(i[0]), int(i[1]), int(i[2]) - 1) in foundCubes: 
        sideCount -= 2

    foundCubes.add((int(i[0]), int(i[1]), int(i[2])))
    
    if int(i[0]) > maxX: 
        maxX = int(i[0])
    if int(i[1]) > maxY: 
        maxY = int(i[1])
    if int(i[2]) > maxZ: 
        maxZ = int(i[2])

    if int(i[0]) < minX: 
        minX = int(i[0])
    if int(i[1]) < minY: 
        minY = int(i[1])
    if int(i[2]) < minZ: 
        minZ = int(i[2])

print(maxX, maxY, maxZ)
print(minX, minY, minZ)
blankSpaces = set()

for x in range(maxX + 1): 
    for y in range(maxY + 1): 
        for z in range(maxZ + 1):
            if (x,y,z) not in foundCubes and x > minX and x < maxX and y > minY and y < maxY and z > minZ and z < maxZ: 
                blankSpaces.add((x, y, z)) 

print(blankSpaces)
          
for i in blankSpaces: 
    print(i)
    emptySpaceCount += 6
    if (i[0] + 1, i[1], i[2]) in blankSpaces: 
        print(i, "1")
        emptySpaceCount -= 1
    if (i[0] - 1, i[1], i[2]) in blankSpaces: 
        print(i, "2")
        emptySpaceCount -= 1
    if (i[0], i[1] + 1, i[2]) in blankSpaces: 
        print(i, "3")
        emptySpaceCount -= 1
    if (i[0], i[1] - 1, i[2]) in blankSpaces: 
        print(i, "4")
        emptySpaceCount -= 1
    if (i[0], i[1], i[2] + 1) in blankSpaces: 
        print(i, "5")
        emptySpaceCount -= 1
    if (i[0], i[1], i[2] - 1) in blankSpaces:
        print(i, "6")
        emptySpaceCount -= 1

sideCount -= emptySpaceCount
print(emptySpaceCount)
print(sideCount)