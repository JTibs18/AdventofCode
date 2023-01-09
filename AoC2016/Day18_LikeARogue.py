# Part 1 Solution
f1 = open("day18.txt")

safeTiles = 0
lineIndx = 0
rows = 40 - 1
lines = []

for line in f1:
    lines.append(line.strip())

for i in lines[0]: 
    if i == ".":
        safeTiles += 1 

while rows: 
    newline = ''
    indx1 = -1
    indx2 = 1

    while indx1 < len(lines[lineIndx]) - 1:
        if indx1 >= 0: 
            left = lines[lineIndx][indx1]
        else: 
            left = "."
        
        if indx1 + 1 >= 0 and indx1 + 1 < len(lines[lineIndx]): 
            middle = lines[lineIndx][indx1 + 1]
        else: 
            middle = "."

        if indx2 >= 0 and indx2 < len(lines[lineIndx]): 
            right = lines[lineIndx][indx2]
        else: 
            right = "."

        if (left == "^" and middle == "^" and right == ".") or (left == "." and middle == "^" and right == "^") or (left == "^" and middle == "." and right == ".") or (left == "." and middle == "." and right == "^"): 
            newline += "^"
        else:
            newline += '.'
            safeTiles += 1 
        
        indx1 += 1 
        indx2 += 1
    
    lines.append(newline)
    lineIndx += 1
    rows -= 1 

print(safeTiles)

#Part 2 Solution (Takes a few minutes)
f1 = open("day18.txt")

safeTiles = 0
lineIndx = 0
rows = 400000 - 1
lines = []

for line in f1:
    lines.append(line.strip())

for i in lines[0]: 
    if i == ".":
        safeTiles += 1 

while rows: 
    newline = ''
    indx1 = -1
    indx2 = 1

    while indx1 < len(lines[lineIndx]) - 1:
        if indx1 >= 0: 
            left = lines[lineIndx][indx1]
        else: 
            left = "."
        
        if indx1 + 1 >= 0 and indx1 + 1 < len(lines[lineIndx]): 
            middle = lines[lineIndx][indx1 + 1]
        else: 
            middle = "."

        if indx2 >= 0 and indx2 < len(lines[lineIndx]): 
            right = lines[lineIndx][indx2]
        else: 
            right = "."

        if (left == "^" and middle == "^" and right == ".") or (left == "." and middle == "^" and right == "^") or (left == "^" and middle == "." and right == ".") or (left == "." and middle == "." and right == "^"): 
            newline += "^"
        else:
            newline += '.'
            safeTiles += 1 
        
        indx1 += 1 
        indx2 += 1
    
    lines.append(newline)
    lineIndx += 1
    rows -= 1 

print(safeTiles)