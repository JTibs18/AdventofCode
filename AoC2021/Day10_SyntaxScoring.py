#Part 1 Solution
f1 = open("day10.txt")

chunk = {"(": ")", "[" : "]", "{": "}", "<": ">"}
charToPoint = {")": 3, "]": 57, "}":1197, ">":25137}
points = 0

for line in f1:
    line = line.strip()
    brackets = []
    for i in line:
        if i in chunk:
            brackets.append(i)
        else:
            if i == chunk.get(brackets[len(brackets) - 1]):
                brackets.pop()
            else:
                points += charToPoint.get(i)
                break

print(points)

#Part 2 Solution
import math
f1 = open("day10.txt")

chunk = {"(": ")", "[" : "]", "{": "}", "<": ">"}
charToPoint = {")": 1, "]": 2, "}":3, ">":4}
lineScores = []

for line in f1:
    corrupt = False
    points = 0
    line = line.strip()
    brackets = []
    for i in line:
        if i in chunk:
            brackets.append(i)
        else:
            if i == chunk.get(brackets[len(brackets) - 1]):
                brackets.pop()
            else:
                corrupt = True

    if corrupt == False:
        brackets.reverse()

        for i in brackets:
            points = (5 * points) + charToPoint.get(chunk.get(i))

        lineScores.append(points)

half = math.floor(len(lineScores) / 2)
lineScores.sort()
print(lineScores[half])
