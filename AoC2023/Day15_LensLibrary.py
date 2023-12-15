# Part 1 Solution
f1 = open("day15.txt")

sequence = []
runningSum = 0 

for line in f1:
    sequence = line.strip().split(",")

for i in sequence: 
    currentValue = 0

    for c in i: 
        currentValue += ord(c)
        currentValue *= 17 
        currentValue = currentValue % 256

    runningSum += currentValue

print(runningSum) 

# Part 2 Solution
f1 = open("day15.txt")

focusingPower = 0
sequence = []
boxes = dict() 

for line in f1:
    sequence = line.strip().split(",")

for i in sequence: 
    label = 0
    indx = 0 
    curSequence = ''

    while i[indx] != "-" and i[indx] != "=":
        label += ord(i[indx])
        label *= 17 
        label = label % 256
        curSequence += i[indx]
        indx += 1
    
    if i[indx] == "-" and label in boxes and any(curSequence in x for x in boxes[label]):
        count = 0

        for j in boxes[label]:
            key = list(j.keys())[0]
            count += 1
            
            if key == curSequence:
                break 

        boxes[label].pop(count - 1)

    elif i[indx] == "=" and label in boxes and any(curSequence in x for x in boxes[label]):
        count = 0 

        for j in boxes[label]:
            key = list(j.keys())[0]
            count += 1 

            if key == curSequence:
                break

        boxes[label][count - 1] = {curSequence: int(i[indx + 1])}

    elif i[indx] == "=":
        if label in boxes: 
            boxes[label].append({curSequence: int(i[indx + 1])})
        else:
            boxes[label] = [{curSequence: int(i[indx + 1])}]

for key, value in boxes.items():
    for indx, val in enumerate(value):
        lens = list(val.values())[0]
        focusingPower += (key + 1) * (indx + 1) * lens

print(focusingPower) 