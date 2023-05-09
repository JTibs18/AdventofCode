# Part 1 Solution 
f1 = open("day21.txt")

allergenIngredients = dict() 
knownAllergens = set()
allIngredients = [] 
notAllergenCount = 0 

for line in f1:
    # parsing input
    inputLine = line.strip().split("(contains ")
    ingredients = inputLine[0].strip().split(" ")
    allergens = inputLine[1].strip(")").split(", ")

    # finding ingredients associated to allergens 
    for i in allergens: 
        if i not in allergenIngredients: 
            allergenIngredients[i] = ingredients
        else: 
            allergenIngredients[i] = list(set(allergenIngredients[i]) & set(ingredients))
    
    allIngredients.extend(ingredients)

# using process of elimination to find which ingredient translates to each allergen 
while len(knownAllergens) < len(allergenIngredients): 
    for key, value in allergenIngredients.items(): 
        if len(value) == 1: 
            knownAllergens.add(value[0])
        else: 
            for i in value: 
                if i in knownAllergens: 
                    allergenIngredients[key].remove(i)

# counting the number of ingredients that are not allergens 
for i in allIngredients: 
    if i not in knownAllergens: 
        notAllergenCount += 1

print(notAllergenCount)

# Part 2 Solution 
f1 = open("day21.txt")

allergenIngredients = dict() 
knownAllergens = set()
allIngredients = [] 
canonicalList = []
output = []

for line in f1:
    # parsing input
    inputLine = line.strip().split("(contains ")
    ingredients = inputLine[0].strip().split(" ")
    allergens = inputLine[1].strip(")").split(", ")

    # finding ingredients associated to allergens 
    for i in allergens: 
        if i not in allergenIngredients: 
            allergenIngredients[i] = ingredients
        else: 
            allergenIngredients[i] = list(set(allergenIngredients[i]) & set(ingredients))
    
    allIngredients.extend(ingredients)
    canonicalList.extend(allergens)

# using process of elimination to find which ingredient translates to each allergen 
while len(knownAllergens) < len(allergenIngredients): 
    for key, value in allergenIngredients.items(): 
        if len(value) == 1: 
            knownAllergens.add(value[0])
        else: 
            for i in value: 
                if i in knownAllergens: 
                    allergenIngredients[key].remove(i)

# finding canonical dangerous ingredient list 
canonicalList = sorted(set(canonicalList))

for i in canonicalList:
    output.append(allergenIngredients[i][0])

print(",".join(output))