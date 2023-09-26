#Part 1 Solution
f1 = open("day16.txt")

programs = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]

for line in f1:
    danceMoves = line.strip().split(',')

for i in danceMoves: 
    if i[0] == "s": 
        spinSize = int(i[1:])
        programs = programs[-spinSize:] + programs[:-spinSize]
    elif i[0] == "x": 
        data = i[1:].split('/')

        indx1 = int(data[0])
        indx2 = int(data[1])

        temp = programs[indx1]
        programs[indx1] = programs[indx2]
        programs[indx2] = temp 
    else: 
        indx1 = programs.index(i[1])
        indx2 = programs.index(i[3])
        
        programs[indx1] = i[3]
        programs[indx2] = i[1]

print(''.join(programs))

#Part 2 Solution
f1 = open("day16.txt")

originalPrograms = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]
programs = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]
count = 0

for line in f1:
    danceMoves = line.strip().split(',')

# finding the count of the number of iterations until the program is in it's original position 
while programs != originalPrograms or count == 0: 
    for i in danceMoves: 
        if i[0] == "s": 
            spinSize = int(i[1:])
            programs = programs[-spinSize:] + programs[:-spinSize]
        elif i[0] == "x": 
            data = i[1:].split('/')

            indx1 = int(data[0])
            indx2 = int(data[1])

            temp = programs[indx1]
            programs[indx1] = programs[indx2]
            programs[indx2] = temp 
        else: 
            indx1 = programs.index(i[1])
            indx2 = programs.index(i[3])
            
            programs[indx1] = i[3]
            programs[indx2] = i[1]
    count += 1

# only iterating through the dance moves from the original position the number of times that 1 billion is modulo the count 
for x in range(1000000000 % count):
    for i in danceMoves: 
        if i[0] == "s": 
            spinSize = int(i[1:])
            programs = programs[-spinSize:] + programs[:-spinSize]
        elif i[0] == "x": 
            data = i[1:].split('/')

            indx1 = int(data[0])
            indx2 = int(data[1])

            temp = programs[indx1]
            programs[indx1] = programs[indx2]
            programs[indx2] = temp 
        else: 
            indx1 = programs.index(i[1])
            indx2 = programs.index(i[3])
            
            programs[indx1] = i[3]
            programs[indx2] = i[1]

print(''.join(programs))