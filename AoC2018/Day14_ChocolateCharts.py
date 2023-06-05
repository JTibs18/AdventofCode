# Part 1 Solution
f1 = open("day14.txt")

scoreboard = []
process = "3 7"
Elf1 = 0
Elf2 = 1

for line in f1:
    input = line.strip()

input = int(input)
scoreboard = process.strip().split(" ")

for index, x in enumerate(scoreboard):
    scoreboard[index] = int(x)

for i in range(0, input + 10):
    newRecipe = scoreboard[Elf1] + scoreboard[Elf2]
    if newRecipe > 9:
        firstNum = int(newRecipe / 10)
        secondNum = newRecipe % 10
        scoreboard.append(firstNum)
        scoreboard.append(secondNum)
    else:
        scoreboard.append(newRecipe)

    Elf1 = 1 + scoreboard[Elf1] + Elf1
    Elf2 = 1 + scoreboard[Elf2] + Elf2

    if Elf1 >= len(scoreboard):
        Elf1 = Elf1 % len(scoreboard)
    if Elf2 >= len(scoreboard):
        Elf2 = Elf2 % len(scoreboard)

print(scoreboard[input:input + 10])

# Part 2 Solution DOES NOT WORK
f1 = open("day14.txt")

scoreboard = []
process = "3 7"
Elf1 = 0
Elf2 = 1
searching = True

for line in f1:
    input = line.strip()

input = int(input)
scoreboard = process.strip().split(" ")

for index, x in enumerate(scoreboard):
    scoreboard[index] = int(x)

while(searching):
    newRecipe = scoreboard[Elf1] + scoreboard[Elf2]
    if newRecipe > 9:
        firstNum = int(newRecipe / 10)
        secondNum = newRecipe % 10
        scoreboard.append(firstNum)
        scoreboard.append(secondNum)
    else:
        scoreboard.append(newRecipe)

    Elf1 = 1 + scoreboard[Elf1] + Elf1
    Elf2 = 1 + scoreboard[Elf2] + Elf2

    if Elf1 >= len(scoreboard):
        Elf1 = Elf1 % len(scoreboard)
    if Elf2 >= len(scoreboard):
        Elf2 = Elf2 % len(scoreboard)

    if len(scoreboard) > len(str(input)):
        complete = False
        for indx, num in enumerate(scoreboard[-len(str(input)):]):
            if num != int(str(input)[indx]):
                break
            if indx == len(str(input)) - 1:
                complete = True
        if complete == True:
            searching = False
            print(len(scoreboard) - len(str(input)))
