# Part 1 Solution
f1 = open("day1.txt")

maxCalories = 0
elfCalories = 0

for calories in f1:
    if calories == "\n":
        if elfCalories > maxCalories:
            maxCalories = elfCalories
        elfCalories = 0
    else:
        elfCalories += int(calories)

print(maxCalories)

# Part 2 Solution
f1 = open("day1.txt")

maxCalories = []
elfCalories = 0

for calories in f1:
    if calories == "\n":
        maxCalories.append(elfCalories)
        elfCalories = 0
    else:
        elfCalories += int(calories)

maxCalories.sort(reverse=True)
print(sum(maxCalories[0:3]))
