#Part 1 Solution
f1 = open("day4.txt")
first = True
numbers = []
cards = []
allC = []
lineCount = 0
done = False

for line in f1:
    line = line.strip("\n")
    if first == True:
        numbers.extend(line.split(","))
        first = False
    elif line != "":
        if lineCount < 5:
            cards.append(line.split())
            lineCount += 1
        else:
            lineCount = 1
            allC.append(cards)
            cards = []
            cards.append(line.split())
allC.append(cards)

for i in numbers:
    if done != True:
        for indx, card in enumerate(allC):
            for ind, row in enumerate(card):
                if i in row:
                    allC[indx][ind][allC[indx][ind].index(i)] = "X"
        for indx, card in enumerate(allC):
            verticalCount = [0,0,0,0,0]
            sum = 0
            for ind, row in enumerate(card):
                horCount = 0
                for indexx, num in enumerate(row):
                    if num == "X":
                         verticalCount[indexx] += 1
                         horCount += 1
                    else:
                        sum += int(num)
                if horCount == 5:
                    done = True
            if done == True or 5 in verticalCount:
                print("Part 1: ", sum * int(i))
                done = True
                break

#Part 2 Solution
f1 = open("day4.txt")
first = True
numbers = []
cards = []
allC = []
lineCount = 0
outputs = []
done = False

for line in f1:
    line = line.strip("\n")
    if first == True:
        numbers.extend(line.split(","))
        first = False
    elif line != "":
        if lineCount < 5:
            cards.append(line.split())
            lineCount += 1
        else:
            lineCount = 1
            allC.append(cards)
            cards = []
            cards.append(line.split())
allC.append(cards)

for i in numbers:
    for indx, card in enumerate(allC):
        for ind, row in enumerate(card):
            if i in row:
                allC[indx][ind][allC[indx][ind].index(i)] = "X"
    for indx, card in enumerate(allC):
        verticalCount = [0,0,0,0,0]
        sum = 0
        for ind, row in enumerate(card):
            horCount = 0
            for indexx, num in enumerate(row):
                if num == "X":
                     verticalCount[indexx] += 1
                     horCount += 1
                else:
                    sum += int(num)
            if horCount == 5:
                done = True
        if done == True or 5 in verticalCount:
            allC.remove(card)
            outputs.append(sum * int(i))
            done = False
print("Part 2: ", outputs[len(outputs) -1])
