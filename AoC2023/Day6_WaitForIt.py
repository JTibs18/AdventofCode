# Part 1 Solution  
f1 = open("day6.txt")

marginError = 1

for line in f1: 
    if "Time" in line: 
        time = line.strip("Time:     ").split()
    else: 
        distance = line.strip("Distance: ").split()

for i in range(len(time)):
    racePossibleCount = 0

    for t in range(int(time[i])):
        m = (int(time[i]) - t) * t 

        if m > int(distance[i]):
            racePossibleCount += 1 
    
    marginError *= racePossibleCount

print(marginError)

# Part 2 Solution  
f1 = open("day6.txt")

for line in f1: 
    if "Time" in line: 
        time = line.strip("Time:     ").split()
    else: 
        distance = line.strip("Distance: ").split()

time = "".join(time)
time = int(time)
distance = "".join(distance)
distance = int(distance)    
racePossibleCount = 0

for t in range(time):
    m = (time - t) * t 

    if m > distance:
        racePossibleCount += 1 

print(racePossibleCount)
