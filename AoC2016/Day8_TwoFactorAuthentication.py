#Part 1 Solution
f1 = open("day8.txt")

onPixels = []
xCord = []
yCord = []
r = []

for line in f1:
    line = line.strip("\n")
    if "rect" in line:
        r = []
        cords = line[5:].split("x")
        for y in range(int(cords[0])):
            for x in range(int(cords[1])):
                onPixels.append((x, y))
        onPixels = list(set(onPixels))
    elif "row" in line:
        r = []
        cords = line[13:].split(" by ")
        for indx, val in enumerate(xCord):
            if int(cords[0]) == val:
                r.append((xCord[indx], yCord[indx]))
                newY = yCord[indx] + int(cords[1])
                if newY > 49:
                    newY = newY - 50
                onPixels.append((xCord[indx], newY))
    else:
        r = []
        cords = line[16:].split(" by ")
        for indx, val in enumerate(yCord):
            if int(cords[0]) == val:
                r.append((xCord[indx], yCord[indx]))
                newX = xCord[indx] + int(cords[1])
                if newX > 5:
                    newX = newX - 6
                onPixels.append((newX, yCord[indx]))
    xCord = []
    yCord = []
    for cd in r:
        if cd in onPixels:
            onPixels.remove(cd)
    for coord in onPixels:
        xCord.append(coord[0])
        yCord.append(coord[1])

print(len(onPixels))

#Part 2 Solution
f1 = open("day8.txt")

onPixels = []
xCord = []
yCord = []
r = []

for line in f1:
    line = line.strip("\n")
    if "rect" in line:
        r = []
        cords = line[5:].split("x")
        for y in range(int(cords[0])):
            for x in range(int(cords[1])):
                onPixels.append((x, y))
        onPixels = list(set(onPixels))
    elif "row" in line:
        r = []
        cords = line[13:].split(" by ")
        for indx, val in enumerate(xCord):
            if int(cords[0]) == val:
                r.append((xCord[indx], yCord[indx]))
                newY = yCord[indx] + int(cords[1])
                if newY > 49:
                    newY = newY - 50
                onPixels.append((xCord[indx], newY))
    else:
        r = []
        cords = line[16:].split(" by ")
        for indx, val in enumerate(yCord):
            if int(cords[0]) == val:
                r.append((xCord[indx], yCord[indx]))
                newX = xCord[indx] + int(cords[1])
                if newX > 5:
                    newX = newX - 6
                onPixels.append((newX, yCord[indx]))
    xCord = []
    yCord = []
    for cd in r:
        if cd in onPixels:
            onPixels.remove(cd)
    for coord in onPixels:
        xCord.append(coord[0])
        yCord.append(coord[1])

for x in range(6):
    for y in range(50):
        if (x, y) in onPixels:
            print("#", end= "")
        else:
            print(" ", end= "")
    print("\n")
