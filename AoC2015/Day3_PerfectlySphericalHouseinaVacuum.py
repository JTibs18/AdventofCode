# #Part 1 Solution
f1 = open("day3.txt") 

x = 0 
y = 0 
locations = set()
locations.add((x, y))

for line in f1:
    for i in range (len(line)):
        print(line[i-0])
        if line[i-0] == "^":
            y = y + 1
            locations.add((x, y))
            print("Go North", x, y)
        elif line[i-0] == ">":
            x = x + 1 
            locations.add((x, y))
            print("Go East", x, y)            
        elif line[i-0] == "v":
            y = y - 1 
            locations.add((x, y))
            print("Go South", x, y)
        elif line[i-0] == "<":
            x = x - 1 
            locations.add((x, y))
            print("Go West", x , y)
           
print (len(locations))

#Part 2 Solution
f1 = open("day3.txt") 

x = 0 
y = 0 
Rx = 0 
Ry = 0 
locations = set()
locations.add((x, y))
rS = 0 

for line in f1:
    for i in range (len(line)):
        if rS == 0: 
            rS = 1 
            print(line[i-0])
            if line[i-0] == "^":
                y = y + 1
                locations.add((x, y))
                print("Go North", x, y)
            elif line[i-0] == ">":
                x = x + 1 
                locations.add((x, y))
                print("Go East", x, y)            
            elif line[i-0] == "v":
                y = y - 1 
                locations.add((x, y))
                print("Go South", x, y)
            elif line[i-0] == "<":
                x = x - 1 
                locations.add((x, y))
                print("Go West", x , y)
        elif rS == 1: 
            rS = 0 
            print(line[i-0])
            if line[i-0] == "^":
                Ry = Ry + 1
                locations.add((Rx, Ry))
                print("ROBO Go North", Rx, Ry)
            elif line[i-0] == ">":
                Rx = Rx + 1 
                locations.add((Rx, Ry))
                print("ROBO Go East", Rx, Ry)            
            elif line[i-0] == "v":
                Ry = Ry - 1 
                locations.add((Rx, Ry))
                print("ROBO Go South", Rx, Ry)
            elif line[i-0] == "<":
                Rx = Rx - 1 
                locations.add((Rx, Ry))
                print("ROBO Go West", Rx , Ry)
           
print (len(locations))