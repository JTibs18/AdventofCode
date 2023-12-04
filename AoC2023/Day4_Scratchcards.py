# Part 1 Solution  
f1 = open("day4.txt")

points = 0 

for line in f1:
    parsed = line.strip().split(": ")[1]
    listOfNums = parsed.split(" | ")
    winningNums = listOfNums[0].split(" ")
    myNums = listOfNums[1].split(" ")

    curPoints = 0
    
    for i in myNums:
        if i != "" and i in winningNums: 
            if curPoints == 0:
                curPoints += 1
            else: 
                curPoints *= 2

    points += curPoints

print(points)

# Part 2 Solution  
f1 = open("day4.txt")

totalScratchCards = dict()
cards = dict() 

for line in f1:
    cardNum = line.strip("Card ").split(": ")[0]
    parsed = line.strip().split(": ")[1]
    listOfNums = parsed.split(" | ")
    winningNums = listOfNums[0].split(" ")
    myNums = listOfNums[1].split(" ")

    cards[int(cardNum)] = (winningNums, myNums)
    totalScratchCards[int(cardNum)] = 1

sortedCards = sorted(cards.keys())

for key in sortedCards: 
    curPoints = 0
    
    for nums in cards[key][1]:
        if nums != "" and nums in cards[key][0]: 
            curPoints += 1

    for card in range(key + 1, curPoints + key + 1):
        totalScratchCards[card] += totalScratchCards[key]

print(sum(totalScratchCards.values()))