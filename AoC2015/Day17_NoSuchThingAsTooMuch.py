#Part 1 Solution
f1 = open("day17.txt")

containers = []
ptr1 = 0 
waysToFit = 0 

for line in f1:
    containers.append(int(line.strip()))

containers = sorted(containers, reverse=True)
print(containers)

while ptr1 < len(containers): 
    litres = containers[ptr1]

    for i in range(ptr1 + 1, len(containers)):
        if litres + containers[i] < 150:
            litres += containers[i]
        elif litres + containers[i] == 150:
            waysToFit += 1
            litres = containers[ptr1]
    
    ptr1 += 1 

print(waysToFit)