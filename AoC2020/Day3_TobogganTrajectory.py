#Part 1 Solution
f1 = open("day3.txt")
trees = 0
across = 0

for line in f1:

        line = line.rstrip()
        if across >= len(line):
            across = across - len(line)

        if line[across] == "#":
            trees = trees + 1

        across = across + 3

print(trees)

#Part 2 Solution
f1 = open("day3.txt")

trees = []
lines = []
tree = 0
across = 0

for line in f1:

    line = line.rstrip()
    lines.append(line)
    if across >= len(line):
        across = across - len(line)
    #Right 3 Down 1
    if line[across] == "#":
        tree = tree + 1

    across = across + 3

trees.append(tree)

tree = 0
across = 0
for i, line in enumerate(lines):
    if across >= len(line):
        across = across - len(line)
    #Right 1 Down 1
    if line[across] == "#":
         tree = tree + 1

    across = across + 1
trees.append(tree)

tree = 0
across = 0
for i, line in enumerate(lines):
    if across >= len(line):
        across = across - len(line)
    #Right 1 Down 6
    if line[across] == "#":
        tree = tree + 1

    across = across + 5
trees.append(tree)

tree = 0
across = 0
for i, line in enumerate(lines):
    if across >= len(line):
        across = across - len(line)
    #Right 7 Down 1
    if line[across] == "#":
        tree = tree + 1

    across = across + 7
trees.append(tree)

tree = 0
across = 0
down =True
for i, line in enumerate(lines):
    #Right 1 Down 2
    if down ==True:
        if across >= len(line):
            across = across - len(line)

        if line[across] == "#":
            tree = tree + 1

        across = across + 1
        down = False
    else:
        down =True
trees.append(tree)
total = 1

#Multiplying together
for i, nums in enumerate(trees):
    total = nums * total

print(total)
