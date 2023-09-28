# Part 1 Solution 
f1 = open("day14.txt")

program = []
memory = dict()
curMask = ''
sum = 0

for line in f1: 
    program.append(line.strip())

for i in program: 
    if 'mask' in i: 
        curMask = i.split(" = ")[1]
    else: 
        newValue = ''

        data = i.split(" = ")
        value = int(data[1])
        memLocation = data[0].strip("mem[]")
        
        binaryValue = "{:036b}".format(value)

        for indx, val in enumerate(binaryValue): 
            if curMask[indx] != "X": 
                newValue += curMask[indx]
            else: 
                newValue += val 
        
        memory[memLocation] = newValue
        
for value in memory.values(): 
    sum += int(value, 2)

print(sum)

# Part 2 Solution 
import itertools 
f1 = open("day14.txt")

program = []
curMaskVariations = []
memory = dict()
curMask = ''
sum = 0

for line in f1: 
    program.append(line.strip())

for i in program: 
    if 'mask' in i: 
        maskXCount = 0 
        curMask = i.split(" = ")[1]
        
        for i in curMask: 
            if i == "X":
                maskXCount += 1 
        
        curMaskVariations = list(itertools.product(range(2), repeat=maskXCount))
    else: 
        data = i.split(" = ")
        value = int(data[1])
        memLocation = int(data[0].strip("mem[]"))
        
        binaryValue = "{:036b}".format(memLocation)

        for x in curMaskVariations: 
            newValue = ''
            xPtr = 0 
            
            for indx, val in enumerate(binaryValue): 
                if curMask[indx] == "1": 
                    newValue += "1"
                elif curMask[indx] == "X":
                    newValue += str(x[xPtr])
                    xPtr += 1 
                else: 
                    newValue += val 

            memory[int(newValue, 2)] = value
        
for value in memory.values(): 
    sum += value

print(sum)
