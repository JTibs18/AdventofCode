#Part 1 Solution
f1 = open("day1.txt") 
floor = 0

for line in f1: 
    line = line.rstrip() 

for level in line: 
    if level == "(": 
        floor = floor + 1
    else: 
        floor = floor - 1

print(floor)

#Part 2 Solution
f1 = open("day1.txt") 
floor = 0
position = 1

for line in f1: 
    line = line.rstrip() 

for level in line: 
    if level == "(": 
        floor = floor + 1
    else: 
        floor = floor - 1
    
    if floor == -1:
        print("Basement is", position)
        break 
    
    position = position + 1

print(floor)