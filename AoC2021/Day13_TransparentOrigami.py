# Part 1 Solution
f1 = open("day13.txt")

dots = []
instructions = []
newDots = set() 
parseInstructions = False

# parse input
for line in f1:
    if line == "\n":
        parseInstructions = True 
    elif parseInstructions == True: 
        instruction = line.strip("fold along \n")
        instructions.append(instruction)
    else: 
        dot = line.strip().split(",")
        dots.append((int(dot[0]), int(dot[1])))

# fold 
if "y" in instructions[0]: 
    foldLine = int(instructions[0].strip("y="))
    for i in dots: 
        if i[1] > foldLine: 
            newY = foldLine - (i[1] - foldLine)
            if newY >= 0: 
                newDots.add((i[0], newY))
        else: 
            newDots.add(i)
else: 
    foldLine = int(instructions[0].strip("x="))
    for i in dots: 
        if i[0] > foldLine: 
            newX = foldLine - (i[0] - foldLine)
            if newX >= 0: 
                newDots.add((newX, i[1]))
        else: 
            newDots.add(i)

print(len(newDots))

# Part 2 Solution
f1 = open("day13.txt")

maxX = 0 
maxY = 0 
dots = []
instructions = []
parseInstructions = False

# parse input
for line in f1:
    if line == "\n":
        parseInstructions = True 
    elif parseInstructions == True: 
        instruction = line.strip("fold along \n")
        instructions.append(instruction)
    else: 
        dot = line.strip().split(",")
        dots.append((int(dot[0]), int(dot[1])))

# fold 
for instruct in instructions: 
    newDots = set() 

    if "y" in instruct: 
        foldLine = int(instruct.strip("y="))
        for i in dots: 
            if i[1] > foldLine: 
                newY = foldLine - (i[1] - foldLine)
                if newY >= 0: 
                    newDots.add((i[0], newY))
            else: 
                newDots.add(i)
    else: 
        foldLine = int(instruct.strip("x="))
        for i in dots: 
            if i[0] > foldLine: 
                newX = foldLine - (i[0] - foldLine)
                if newX >= 0: 
                    newDots.add((newX, i[1]))
            else: 
                newDots.add(i)
    
    dots = list(newDots)

# find dimensions of grid 
for x, y in newDots: 
    if x > maxX: 
        maxX = x 
    if y > maxY: 
        maxY = y 

# display grid
for y in range(maxY + 2): 
    row = ""

    for x in range(maxX + 2): 
        if (x, y) in newDots: 
            row += "#"
        else: 
            row += "."
            
    print(row)