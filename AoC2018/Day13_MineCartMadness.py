#Part 1 Solution  
f1 = open("day13.txt")

grid = dict()
cartsStart = []
cartsTurnPtr = []
cartsCurDir = []
turnDirections = ["L", "S", "R"]

for y, line in enumerate(f1):
    for x, val in enumerate(line): 
        if val != " " and val != "\n": 
            grid[(x, y)] = val 
            
            if val == ">" or val == "<" or val == "^" or val == "v": 
                cartsStart.append((x, y))
                cartsTurnPtr.append(0)
                
                if val == ">":
                    cartsCurDir.append("R")
                elif val == "<":
                    cartsCurDir.append("L")
                elif val == "^":
                    cartsCurDir.append("U")
                else:
                    cartsCurDir.append("D")

while len(set(cartsStart)) == len(cartsStart):
    sortedCarts = sorted(cartsStart, key=lambda x:(x[1], x[0]))
    
    for cart in sortedCarts:
        i = cartsStart.index(cart)
        if cartsCurDir[i] == "R":
            nextLocation = (cartsStart[i][0] + 1, cartsStart[i][1])
            
            if grid[nextLocation] == "\\":
                cartsCurDir[i] = "D"
            elif grid[nextLocation] == "/":
                cartsCurDir[i] = "U"
            elif grid[nextLocation] == "+":
                if turnDirections[cartsTurnPtr[i]] == "L": 
                    cartsCurDir[i] = "U"
                elif turnDirections[cartsTurnPtr[i]] == "R":
                    cartsCurDir[i] = "D"

                cartsTurnPtr[i] += 1 
                if cartsTurnPtr[i] == len(turnDirections):
                    cartsTurnPtr[i] = 0 

            cartsStart[i] = nextLocation

        elif cartsCurDir[i] == "L":
            nextLocation = (cartsStart[i][0] - 1, cartsStart[i][1])
            
            if grid[nextLocation] == "/":
                cartsCurDir[i] = "D"
            elif grid[nextLocation] == "\\":
                cartsCurDir[i] = "U"
            elif grid[nextLocation] == "+":
                if turnDirections[cartsTurnPtr[i]] == "L": 
                    cartsCurDir[i] = "D"
                elif turnDirections[cartsTurnPtr[i]] == "R":
                    cartsCurDir[i] = "U"

                cartsTurnPtr[i] += 1 
                if cartsTurnPtr[i] == len(turnDirections):
                    cartsTurnPtr[i] = 0 

            cartsStart[i] = nextLocation

        elif cartsCurDir[i] == "U":
            nextLocation = (cartsStart[i][0], cartsStart[i][1] - 1)

            if grid[nextLocation] == "/":
                cartsCurDir[i] = "R"
            elif grid[nextLocation] == "\\":
                cartsCurDir[i] = "L"
            elif grid[nextLocation] == "+":
                if turnDirections[cartsTurnPtr[i]] == "L":
                    cartsCurDir[i] = "L"
                elif turnDirections[cartsTurnPtr[i]] == "R":
                    cartsCurDir[i] = "R"
                
                cartsTurnPtr[i] += 1
                if cartsTurnPtr[i] == len(turnDirections):
                    cartsTurnPtr[i] = 0
            
            cartsStart[i] = nextLocation
        
        else:
            nextLocation = (cartsStart[i][0], cartsStart[i][1] + 1)

            if grid[nextLocation] == "/":
                cartsCurDir[i] = "L"
            elif grid[nextLocation] == "\\":
                cartsCurDir[i] = "R"
            elif grid[nextLocation] == "+":
                if turnDirections[cartsTurnPtr[i]] == "L":
                    cartsCurDir[i] = "R"
                elif turnDirections[cartsTurnPtr[i]] == "R":
                    cartsCurDir[i] = "L"
                
                cartsTurnPtr[i] += 1
                if cartsTurnPtr[i] == len(turnDirections):
                    cartsTurnPtr[i] = 0

            cartsStart[i] = nextLocation

        if len(set(cartsStart)) != len(cartsStart):
            break 

collision = set([i for i in cartsStart if cartsStart.count(i) > 1])

print(collision)

#Part 2 Solution  
f1 = open("day13.txt")

grid = dict()
cartsStart = []
cartsTurnPtr = []
cartsCurDir = []
turnDirections = ["L", "S", "R"]

for y, line in enumerate(f1):
    for x, val in enumerate(line): 
        if val != " " and val != "\n": 
            grid[(x, y)] = val 
            
            if val == ">" or val == "<" or val == "^" or val == "v": 
                cartsStart.append((x, y))
                cartsTurnPtr.append(0)
                
                if val == ">":
                    cartsCurDir.append("R")
                elif val == "<":
                    cartsCurDir.append("L")
                elif val == "^":
                    cartsCurDir.append("U")
                else:
                    cartsCurDir.append("D")

while len(cartsStart) > 1:
    sortedCarts = sorted(cartsStart, key=lambda x:(x[1], x[0]))
    
    for cart in sortedCarts:
        if cart in cartsStart: 
            i = cartsStart.index(cart)
            if cartsCurDir[i] == "R":
                nextLocation = (cartsStart[i][0] + 1, cartsStart[i][1])
                
                if grid[nextLocation] == "\\":
                    cartsCurDir[i] = "D"
                elif grid[nextLocation] == "/":
                    cartsCurDir[i] = "U"
                elif grid[nextLocation] == "+":
                    if turnDirections[cartsTurnPtr[i]] == "L": 
                        cartsCurDir[i] = "U"
                    elif turnDirections[cartsTurnPtr[i]] == "R":
                        cartsCurDir[i] = "D"

                    cartsTurnPtr[i] += 1 
                    if cartsTurnPtr[i] == len(turnDirections):
                        cartsTurnPtr[i] = 0 

                cartsStart[i] = nextLocation

            elif cartsCurDir[i] == "L":
                nextLocation = (cartsStart[i][0] - 1, cartsStart[i][1])
                
                if grid[nextLocation] == "/":
                    cartsCurDir[i] = "D"
                elif grid[nextLocation] == "\\":
                    cartsCurDir[i] = "U"
                elif grid[nextLocation] == "+":
                    if turnDirections[cartsTurnPtr[i]] == "L": 
                        cartsCurDir[i] = "D"
                    elif turnDirections[cartsTurnPtr[i]] == "R":
                        cartsCurDir[i] = "U"

                    cartsTurnPtr[i] += 1 
                    if cartsTurnPtr[i] == len(turnDirections):
                        cartsTurnPtr[i] = 0 

                cartsStart[i] = nextLocation

            elif cartsCurDir[i] == "U":
                nextLocation = (cartsStart[i][0], cartsStart[i][1] - 1)

                if grid[nextLocation] == "/":
                    cartsCurDir[i] = "R"
                elif grid[nextLocation] == "\\":
                    cartsCurDir[i] = "L"
                elif grid[nextLocation] == "+":
                    if turnDirections[cartsTurnPtr[i]] == "L":
                        cartsCurDir[i] = "L"
                    elif turnDirections[cartsTurnPtr[i]] == "R":
                        cartsCurDir[i] = "R"
                    
                    cartsTurnPtr[i] += 1
                    if cartsTurnPtr[i] == len(turnDirections):
                        cartsTurnPtr[i] = 0
                
                cartsStart[i] = nextLocation
            
            else:
                nextLocation = (cartsStart[i][0], cartsStart[i][1] + 1)

                if grid[nextLocation] == "/":
                    cartsCurDir[i] = "L"
                elif grid[nextLocation] == "\\":
                    cartsCurDir[i] = "R"
                elif grid[nextLocation] == "+":
                    if turnDirections[cartsTurnPtr[i]] == "L":
                        cartsCurDir[i] = "R"
                    elif turnDirections[cartsTurnPtr[i]] == "R":
                        cartsCurDir[i] = "L"
                    
                    cartsTurnPtr[i] += 1
                    if cartsTurnPtr[i] == len(turnDirections):
                        cartsTurnPtr[i] = 0

                cartsStart[i] = nextLocation

            if len(set(cartsStart)) != len(cartsStart):
                toRemove = set([i for i in cartsStart if cartsStart.count(i) > 1]).pop()
                indx1 = cartsStart.index(toRemove)
                cartsStart.pop(indx1)
                indx2 = cartsStart.index(toRemove)
                cartsStart.pop(indx2)

                cartsCurDir.pop(indx1)
                cartsCurDir.pop(indx2)

                cartsTurnPtr.pop(indx1)
                cartsTurnPtr.pop(indx2)

print(cartsStart[0])
