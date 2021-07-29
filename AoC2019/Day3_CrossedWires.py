#Part 1 Solution
f1 = open("day3.txt")

for indx, line in enumerate(f1):
    line = line.strip("/n").split(",")
    if indx == 0:
        wire1 = line
    else:
        wire2 = line

w1Visited = set()
w2Visited = set()
crossed = []
distance = []

w1X = 0
w1Y = 0
w2X = 0
w2Y = 0

for coord in wire1:
    if coord[0] == "R":
        for c in range(int(coord[1:])):
            w1X += 1
            w1Visited.add((w1X, w1Y))
    elif coord[0] == "D":
        for c in range(int(coord[1:])):
            w1Y -= 1
            w1Visited.add((w1X, w1Y))
    elif coord[0] == "L":
        for c in range(int(coord[1:])):
            w1X -= 1
            w1Visited.add((w1X, w1Y))
    else:
        for c in range(int(coord[1:])):
            w1Y += 1
            w1Visited.add((w1X, w1Y))

for coord in wire2:
    if coord[0] == "R":
        for c in range(int(coord[1:])):
            w2X += 1
            w2Visited.add((w2X, w2Y))
    elif coord[0] == "D":
        for c in range(int(coord[1:])):
            w2Y -= 1
            w2Visited.add((w2X, w2Y))
    elif coord[0] == "L":
        for c in range(int(coord[1:])):
            w2X -= 1
            w2Visited.add((w2X, w2Y))
    else:
        for c in range(int(coord[1:])):
            w2Y += 1
            w2Visited.add((w2X, w2Y))

for v in w1Visited:
    if v in w2Visited:
        crossed.append(v)

for i in crossed:
    s = abs(int(i[0])) + abs(int(i[1]))
    distance.append(s)

print(min(distance))

#Part 2 Solution
f1 = open("day3.txt")

for indx, line in enumerate(f1):
    line = line.strip("/n").split(",")
    if indx == 0:
        wire1 = line
    else:
        wire2 = line

w1Visited = dict()
w2Visited = dict()
w1Steps = 0
w2Steps = 0
distance = []

w1X = 0
w1Y = 0
w2X = 0
w2Y = 0

for coord in wire1:
    if coord[0] == "R":
        for c in range(int(coord[1:])):
            w1X += 1
            w1Steps += 1
            w1Visited[(w1X, w1Y)] = w1Steps
    elif coord[0] == "D":
        for c in range(int(coord[1:])):
            w1Y -= 1
            w1Steps += 1
            w1Visited[(w1X, w1Y)] = w1Steps
    elif coord[0] == "L":
        for c in range(int(coord[1:])):
            w1X -= 1
            w1Steps += 1
            w1Visited[(w1X, w1Y)] = w1Steps
    else:
        for c in range(int(coord[1:])):
            w1Y += 1
            w1Steps += 1
            w1Visited[(w1X, w1Y)] = w1Steps

for coord in wire2:
    if coord[0] == "R":
        for c in range(int(coord[1:])):
            w2X += 1
            w2Steps += 1
            w2Visited[(w2X, w2Y)] = w2Steps
    elif coord[0] == "D":
        for c in range(int(coord[1:])):
            w2Y -= 1
            w2Steps += 1
            w2Visited[(w2X, w2Y)] = w2Steps
    elif coord[0] == "L":
        for c in range(int(coord[1:])):
            w2X -= 1
            w2Steps += 1
            w2Visited[(w2X, w2Y)] = w2Steps
    else:
        for c in range(int(coord[1:])):
            w2Y += 1
            w2Steps += 1
            w2Visited[(w2X, w2Y)] = w2Steps

for key, val in w1Visited.items():
    if key in w2Visited.keys():
        distance.append(int(w1Visited[key]) + int(w2Visited[key]))

print(min(distance))
