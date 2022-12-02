# Part 1 Solution
f1 = open("day2.txt")

totalScore = 0
myPoints = {"X": 1, "Y": 2, "Z": 3}
translate = {"A": "X", "B": "Y", "C": "Z"}

for line in f1:
    round = line.strip().split(" ")

    oppHand = round[0]
    myHand = round[1]

    if translate[oppHand] == myHand:
        totalScore += myPoints[myHand] + 3
    elif (oppHand == "A" and myHand == "Z") or (oppHand == "C" and myHand == "Y") or (oppHand == "B" and myHand == "X"):
        totalScore += myPoints[myHand]
    else:
        totalScore += myPoints[myHand] + 6

print(totalScore)

# Part 2 Solution
f1 = open("day2.txt")

totalScore = 0
myPoints = {"X": 1, "Y": 2, "Z": 3}
translate = {"A": "X", "B": "Y", "C": "Z"}
ruleMappingLose = {"A": "Z", "C": "Y", "B": "X"} # key beats value
ruleMappingWin = {"B": "Z", "C": "X", "A": "Y"} # key loses to value

for line in f1:
    round = line.strip().split(" ")

    oppHand = round[0]
    outcome = round[1]

    if outcome == "Y":
        totalScore += myPoints[translate[oppHand]] + 3
    elif outcome == "X":
        totalScore += myPoints[ruleMappingLose[oppHand]]
    else:
        totalScore += myPoints[ruleMappingWin[oppHand]] + 6

print(totalScore)
