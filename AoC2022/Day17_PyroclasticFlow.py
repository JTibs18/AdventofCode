# Part 1 Solution
f1 = open("day17.txt")

rockTypes = {"horLine": [(2, 0), (3, 0), (4, 0), (5, 0)], "cross": [(2,1), (3,0), (3,1), (3,2), (4,1)], "backwardsL": [(2,2), (2,3), (2,4), (1,4), (0,4)], "vertLine": [(2,2), (2,3), (2,4), (2,5)], "square": [(2,0), (3,0), (2,1), (3,1)]}
rockLengths = {"horLine": (4, 1), "cross": (3, 3), "backwardsL": (3,3), "vertLine": (1, 4), "square": (2, 2) }
rockToIndxMapping = {0: "horLine", 1: "cross", 2: "backwardsL", 3: "vertLine", 4: "square"}
jetPatternIndx = 0
rockIndx = 0
chamber = [[False for x in range(7)] for y in range(3)]

for line in f1:
    jetPattern = line.strip()

for i in range(2022):
    for j in range(4): 
        

    if rockIndx + 1 == 5: 
        rocKIndx = 0
    else: 
        rockIndx += 1

    if jetPatternIndx + 1 > len(jetPattern) - 1: 
        jetPatternIndx = 0
    else: 
        jetPatternIndx += 1 