from ast import literal_eval

# Part 1 Solution
f1 = open("day13.txt")

correctPairs = set() 
input = []
pairIndex = 1
ptr1 = 0 
ptr2 = 1

def comparePackets(left, right): 
    print(left, right)
    for indx, val in enumerate(right): 
        if indx >= len(left):
            return True 
        print("ERE", val, left[indx])
        # if type(val) == list and type(left[indx]) == list and len(left[indx]) > len(val): 
        #     print("F!")
        #     return False 
        if type(left[indx]) != list and type(val) != list: 
            if val < left[indx]: 
                return False 
            elif val != left[indx]: 
                return True
        elif type(left[indx]) == list and type(val) == list: 
            if comparePackets(left[indx], val) != None: 
                return comparePackets(left[indx], val)
        elif type(left[indx])!= list and type(val) == list: 
            if comparePackets([left[indx]], val) != None: 
                return comparePackets([left[indx]], val)
        elif comparePackets(left[indx], [val]) != None:
            return comparePackets(left[indx], [val])
    print("HIT", left, right)
    # return True 

for line in f1:
    if line != "\n":
        line = literal_eval(line.strip())
        input.append(line)

while ptr2 < len(input): 
    print("PAIR", pairIndex)
    print("LENNY", len(input[ptr1]), len(input[ptr2]))
    if len(input[ptr1]) <= len(input[ptr2]): 
        if comparePackets(input[ptr1], input[ptr2]) == True: 
            correctPairs.add(pairIndex)
    pairIndex += 1 
    ptr1 += 2
    ptr2 += 2

print(sum(correctPairs))
print(correctPairs)
