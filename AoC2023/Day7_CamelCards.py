#Part 1 Solution
f1 = open("day7.txt")

hands = dict()
handType = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[]}
totalWinnings = 0
rank = 1

for line in f1:
    parsed = line.strip().split()
    hands[parsed[0]] = int(parsed[1])
    
for h in hands: 
    kindCount = dict()

    for card in h: 
        if card in kindCount: 
            kindCount[card] += 1
        else:
            kindCount[card] = 1 
    
    if 5 in kindCount.values(): 
        handType[1].append(h)
    elif 4 in kindCount.values(): 
        handType[2].append(h)
    elif 3 in kindCount.values() and 2 in kindCount.values():
        handType[3].append(h)
    elif 3 in kindCount.values():
        handType[4].append(h)
    elif sum(value == 2 for value in kindCount.values()) == 2:
        handType[5].append(h)
    elif 2 in kindCount.values(): 
        handType[6].append(h)
    else: 
        handType[7].append(h)

sortedKeys = sorted(handType.keys(), reverse=True)

for key in sortedKeys:
    order = 'AKQJT98765432'
    newOrder = sorted(handType[key], key=lambda card: [order.index(c) for c in card], reverse=True)
    
    for i in newOrder: 
        totalWinnings += rank * hands[i]
        rank += 1 

print(totalWinnings)

#Part 2 Solution
f1 = open("day7.txt")

hands = dict()
handType = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[]}
totalWinnings = 0
rank = 1

for line in f1:
    parsed = line.strip().split()
    hands[parsed[0]] = int(parsed[1])
    
for h in hands: 
    kindCount = dict()

    for card in h: 
        if card in kindCount: 
            kindCount[card] += 1
        else:
            kindCount[card] = 1 

    if "J" in kindCount and kindCount["J"] != 5:
        wildCard = kindCount["J"] 
        del kindCount["J"]
        maxCard = max(kindCount, key=kindCount.get)
        kindCount[maxCard] += wildCard
    
    if 5 in kindCount.values(): 
        handType[1].append(h)
    elif 4 in kindCount.values(): 
        handType[2].append(h)
    elif 3 in kindCount.values() and 2 in kindCount.values():
        handType[3].append(h)
    elif 3 in kindCount.values():
        handType[4].append(h)
    elif sum(value == 2 for value in kindCount.values()) == 2:
        handType[5].append(h)
    elif 2 in kindCount.values(): 
        handType[6].append(h)
    else: 
        handType[7].append(h)

sortedKeys = sorted(handType.keys(), reverse=True)

for key in sortedKeys:
    order = 'AKQT98765432J'
    newOrder = sorted(handType[key], key=lambda card: [order.index(c) for c in card], reverse=True)

    for i in newOrder: 
        totalWinnings += rank * hands[i]
        rank += 1 

print(totalWinnings)
