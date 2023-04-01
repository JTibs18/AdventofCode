# Part 1 Solution (takes about 30 seconds to run)
f1 = open("day15.txt")

ingredientList = []
bestScore = 0

for line in f1:
    ingredients = line.strip().split(": ")
    properties = ingredients[1].split(", ")
    newIngredient = dict()

    for i in properties: 
        if "calories" not in i: 
            property = i.split(" ")
            newIngredient[property[0]] = int(property[1])
        
    ingredientList.append(newIngredient)

for i in range (1, 100):
    for j in range(1, 100):
        for k in range(1, 100):
            for l in range(1, 100): 
                if i + j + k + l != 100:
                    continue 
                    
                multiplyerArray = [i, j, k, l]
                propertyScore = {
                    "capacity": 0,
                    "durability": 0, 
                    "flavor": 0,
                    "texture": 0, 
                }
                curScore = 1
                
                for indx, val in enumerate(multiplyerArray): 
                    for key, value in ingredientList[indx].items(): 
                        propertyScore[key] += value * val 

                for value in propertyScore.values():
                    if value <= 0: 
                        curScore = 0 
                        continue 
                    curScore *= value
                
                if curScore > bestScore: 
                    bestScore = curScore

print(bestScore)

# Part 2 Solution (takes about 30 seconds to run)
f1 = open("day15.txt")

ingredientList = []
bestScore = 0

for line in f1:
    ingredients = line.strip().split(": ")
    properties = ingredients[1].split(", ")
    newIngredient = dict()

    for i in properties: 
        property = i.split(" ")
        newIngredient[property[0]] = int(property[1])
        
    ingredientList.append(newIngredient)

for i in range (1, 100):
    for j in range(1, 100):
        for k in range(1, 100): 
            for l in range(1, 100): 
                if i + j + k + l != 100:
                    continue 
                    
                multiplyerArray = [i, j, k, l]
                propertyScore = {
                    "capacity": 0,
                    "durability": 0, 
                    "flavor": 0,
                    "texture": 0, 
                    "calories": 0, 
                }
                curScore = 1
                
                for indx, val in enumerate(multiplyerArray): 
                    for key, value in ingredientList[indx].items(): 
                        propertyScore[key] += value * val 

                for key, value in propertyScore.items():
                    if value <= 0 or propertyScore["calories"] != 500: 
                        curScore = 0 
                        continue 

                    if key != "calories":
                        curScore *= value
                
                if curScore > bestScore: 
                    bestScore = curScore

print(bestScore)