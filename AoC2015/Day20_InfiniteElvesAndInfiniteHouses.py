# Part 1 Solution THIS SOLUTION IS SLOW AF!!! 
f1 = open("day20.txt")

presentCount = 0 
houseNumber = 776000 # used lots of guess and check to reach this number as a starting point

for line in f1:
    goalPresents = int(line.strip())

while presentCount < goalPresents: 
    houseNumber += 10
    presentCount = 0 

    for i in range(1, houseNumber + 1): 
        if houseNumber % i == 0: 
            presentCount += i * 10 
    
print(houseNumber)
