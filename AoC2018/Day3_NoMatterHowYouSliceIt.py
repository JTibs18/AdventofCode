#Part 1 Solution
f1 = open("day3.txt")

fabric = dict()

for line in f1:
    line = line.strip("\n")
    line = line.split("@")
    left = line[1].split(",")[0].strip()
    top = line[1].split(",")[1].split(":")[0].strip()
    x = line[1].split(",")[1].split(":")[1].split("x")[0].strip()
    y = line[1].split(",")[1].split(":")[1].split("x")[1].strip()

    cordX = int(left)
    for val in range(int(x)):
        cordY = int(top)
        for yVal in range(int(y)):
            if (cordX, cordY) not in fabric:
                fabric[(cordX, cordY)] = 1
            else:
                fabric[(cordX, cordY)] += 1
            cordY += 1
        cordX += 1

count = 0
for key, val in fabric.items():
    if val > 1:
        count += 1
print(count)

#Part 2 Solution
f1 = open("day3.txt")

fabric = dict()
claims = dict()

for line in f1:
    line = line.strip("\n")
    line = line.split("@")
    id = line[0].strip()
    left = line[1].split(",")[0].strip()
    top = line[1].split(",")[1].split(":")[0].strip()
    x = line[1].split(",")[1].split(":")[1].split("x")[0].strip()
    y = line[1].split(",")[1].split(":")[1].split("x")[1].strip()

    cordX = int(left)
    if id not in claims:
        claims[id] = []

    for val in range(int(x)):
        cordY = int(top)
        for yVal in range(int(y)):
            if (cordX, cordY) not in fabric:
                fabric[(cordX, cordY)] = 1
            else:
                fabric[(cordX, cordY)] += 1
            claims[id].append((cordX, cordY))
            cordY += 1
        cordX += 1

for key, val in claims.items():
    overlap = False
    for cord in val:
        if fabric[cord] != 1:
            overlap = True
            break
    if overlap == False:
        print(key)
