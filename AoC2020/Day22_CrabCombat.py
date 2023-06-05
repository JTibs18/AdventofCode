#Part 1 Solution
f1 = open("day22.txt")

player1 = []
player2 = []
parseP1 = True 
score = 0 

# Parse input
for line in f1:
    line = line.rstrip()
    if line == "Player 2:": 
        parseP1 = False 
        continue
    elif line == "Player 1:" or line == "": 
        continue 
    
    if parseP1 == True: 
        player1.append(int(line))
    else: 
        player2.append(int(line))

# Playing the card game until one player has no cards left
while len(player1) != 0 and len(player2) != 0: 
    p1Card = player1.pop(0)
    p2Card = player2.pop(0)

    if p1Card > p2Card: 
        player1.append(p1Card)
        player1.append(p2Card)
    else: 
        player2.append(p2Card)
        player2.append(p1Card)

# Finding which player won
if len(player1) != 0: 
    multiplier = len(player1)
    winningDeck = player1
else: 
    multiplier = len(player2)
    winningDeck = player2 

# Counting the score
for i in winningDeck: 
    score += i * multiplier
    multiplier -= 1

print(score)