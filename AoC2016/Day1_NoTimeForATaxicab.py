#Part 1 solution

f1 = open("day1.txt")
x = 0
y = 0
prevD = "N"

for line in f1:
    line = line.strip("\n")
    cord = line.split(",")

for c in cord:
    c = c.lstrip()

    if prevD == "N":
        if c[0] == "L":
            x -= int(c[1:])
            prevD = "W"
        else:
            x += int(c[1:])
            prevD = "E"
    elif prevD == "E":
        if c[0] == "L":
            y += int(c[1:])
            prevD = "N"
        else:
            y -= int(c[1:])
            prevD = "S"
    elif prevD == "S":
        if c[0] == "L":
            x += int(c[1:])
            prevD = "E"
        else:
            x -= int(c[1:])
            prevD = "W"
    else:
        if c[0] == "L":
            y -= int(c[1:])
            prevD = "S"
        else:
            y += int(c[1:])
            prevD = "N"
print(abs(x) + abs(y))

# Part 2 solution
f1 = open("day1.txt")
x = 0
y = 0
paths = set()
prevD = "N"

for line in f1:
    line = line.strip("\n")
    cord = line.split(",")

for c in cord:
    c = c.lstrip()

    if prevD == "N":
        if c[0] == "L":
            for i in range(1, 1 + int(c[1:])):
                x -= 1
                coord = (x, y)
                if coord in paths:
                    print(abs(x) + abs(y))
                    break
                else:
                    paths.add(coord)
            prevD = "W"
        else:
            for i in range(1, 1 + int(c[1:])):
                x += 1
                coord = (x, y)
                if coord in paths:
                    print(abs(x) + abs(y))
                    break
                else:
                    paths.add(coord)
            prevD = "E"
    elif prevD == "E":
        if c[0] == "L":
            for i in range(1, 1 + int(c[1:])):
                y += 1
                coord = (x, y)
                if coord in paths:
                    print(abs(x) + abs(y))
                    break
                else:
                    paths.add(coord)
            prevD = "N"
        else:
            for i in range(1, 1 + int(c[1:])):
                y -= 1
                coord = (x, y)
                if coord in paths:
                    print(abs(x) + abs(y))
                    break
                else:
                    paths.add(coord)
            prevD = "S"
    elif prevD == "S":
        if c[0] == "L":
            for i in range(1, 1 + int(c[1:])):
                x += 1
                coord = (x, y)
                if coord in paths:
                    print(abs(x) + abs(y))
                    break
                else:
                    paths.add(coord)
            prevD = "E"
        else:
            for i in range(1, 1 + int(c[1:])):
                x -= 1
                coord = (x, y)
                if coord in paths:
                    print(abs(x) + abs(y))
                    break
                else:
                    paths.add(coord)
            prevD = "W"
    else:
        if c[0] == "L":
            for i in range(1, 1 + int(c[1:])):
                y -= 1
                coord = (x, y)
                if coord in paths:
                    print(abs(x) + abs(y))
                    break
                else:
                    paths.add(coord)
            prevD = "S"
        else:
            for i in range(1, 1 + int(c[1:])):
                y += 1
                coord = (x, y)
                if coord in paths:
                    print(abs(x) + abs(y))
                    break
                else:
                    paths.add(coord)
            prevD = "N"
