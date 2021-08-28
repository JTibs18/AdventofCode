#Part 1 Solution
f1 = open("day5.txt") 
nice = 0 

for line in f1: 
    vowelC = 0
    double = False 
    line = line.rstrip() 
    for i in line: 
        if i == "a" or i == "e" or i == "o" or i == "u" or i == "i": 
            vowelC = vowelC + 1 
    if vowelC >= 3: 
        for count, j in enumerate(line): 
            if (count + 1) < len(line) and j == line[count + 1]: 
                double = True 
    if (double == True) and ("ab" not in line) and ("cd" not in line) and ("pq" not in line) and ("xy" not in line):
        nice = nice + 1 
print (nice)

#Part 2 Solution
f1 = open("day5.txt") 
nice = 0 

for line in f1: 
    double = False 
    line = line.rstrip() 
    for count, i in enumerate(line): 
        if (count + 2) < len(line): 
            compare = i + line[1 + count]
            c = line[count + 2: len(line)]
            if compare in c: 
                double = True
    for count, l in enumerate(line): 
        if (count + 2) < len(line) and double == True and l == line[count + 2]: 
            nice = nice + 1
            break
print (nice)