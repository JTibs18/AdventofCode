#Part 1 Solution
f1 = open("day22.txt")

instructions = []
deck = list(range(0, 10007))

for line in f1:
    instructions.append(line.strip())

for i in instructions: 
    if i == "deal into new stack": 
        deck = deck[::-1]
    elif "cut" in i: 
        offset = int(i.split(" ")[1])
        deck = deck[offset::] + deck[:offset]
    else: 
        offset = int(i.split(" ")[3])
        newDeck = [None for x in range(len(deck))]
        insertIndx = 0 

        for j in deck: 
            newDeck[insertIndx] = j

            if insertIndx + offset >= len(deck):
                insertIndx = (insertIndx + offset) - len(deck)
            else: 
                insertIndx += offset

        deck = newDeck

for indx, val in enumerate(deck): 
    if val == 2019: 
        print(indx)
        break 

#Part 2 Solution
f1 = open("day22.txt")

instructions = []
deck = list(range(0, 119315717514047)) # not enough memory to brute force. check this out: https://www.reddit.com/r/adventofcode/comments/116zqxb/2019_day_22_part_2_math_how_can_i_express_these/

for line in f1:
    instructions.append(line.strip())

for count in range(101741582076661): 
    for i in instructions: 
        if i == "deal into new stack": 
            deck = deck[::-1]
        elif "cut" in i: 
            offset = int(i.split(" ")[1])
            deck = deck[offset::] + deck[:offset]
        else: 
            offset = int(i.split(" ")[3])
            newDeck = [None for x in range(len(deck))]
            insertIndx = 0 

            for j in deck: 
                newDeck[insertIndx] = j

                if insertIndx + offset >= len(deck):
                    insertIndx = (insertIndx + offset) - len(deck)
                else: 
                    insertIndx += offset

            deck = newDeck

print(deck[2020])