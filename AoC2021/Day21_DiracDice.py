# Part 1 Solution
f1 = open("day21.txt")
p1Position = 0
p2Position = 0
rollCount = 0 
p1Score = 0 
p2Score = 0
dice = 1

# parse input
for line in f1:
    if p1Position == 0: 
        p1Position = int(line.split(": ")[1])
    else: 
        p2Position = int(line.split(": ")[1])

# function for rolling dice 
def takeTurn(dice, position): 
    roll = 0 
    for i in range(3): 
        roll += dice
        dice += 1 
        if dice > 100: 
            dice = 1

    if roll > 10: 
        position += roll % 10 
    else: 
        position += roll

    if position > 10: 
        position = position % 10
    
    return dice, position

# take turns until one player score is 1000 or more
while p1Score < 1000 and p2Score < 1000: 
    dice, p1Position = takeTurn(dice, p1Position)
    p1Score += p1Position
    rollCount += 3 

    if p1Score >= 1000: 
        break 

    dice, p2Position = takeTurn(dice, p2Position)
    p2Score += p2Position
    rollCount += 3 

print(min(p1Score, p2Score) * rollCount)

# Part 2 Solution NEEDS DYNAMIC PROGRAMMING
f1 = open("day21.txt")
p1Position = 0
p2Position = 0
rollCount = 0 
p1Score = 0 
p2Score = 0
dice = 1

# parse input
for line in f1:
    if p1Position == 0: 
        p1Position = int(line.split(": ")[1])
    else: 
        p2Position = int(line.split(": ")[1])

# function for rolling dice 
def takeTurn(dice, position): 
    roll = 0 
    for i in range(3): 
        roll += dice
        dice += 1 
        if dice > 100: 
            dice = 1

    if roll > 10: 
        position += roll % 10 
    else: 
        position += roll

    if position > 10: 
        position = position % 10
    
    return dice, position

# take turns until one player score is 21 or more
while p1Score < 21 and p2Score < 21: 
    dice, p1Position = takeTurn(dice, p1Position)

    p1Score += p1Position
    rollCount += 3 

    if p1Score >= 1000: 
        break 

    dice, p2Position = takeTurn(dice, p2Position)
        
    p2Score += p2Position
    rollCount += 3 

print(min(p1Score, p2Score) * rollCount)