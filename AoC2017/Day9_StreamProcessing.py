# Part 1 Solution
f1 = open("day9.txt")

groupStack = []
groupCount = 0
garbage = False
ignoreNext = False

for line in f1:
    stream = line.strip()

for i in stream:
    if ignoreNext == True:
        ignoreNext = False
    elif i == '!' and garbage == True:
        ignoreNext = True
    elif i == '{' and garbage != True:
        groupStack.append(i)
    elif i == '}' and garbage != True:
        groupStack.pop()
        groupCount += 1 + len(groupStack)
    elif i == '<':
        garbage = True
    elif i == ">":
        garbage = False

print(groupCount)

# Part 2 Solution
f1 = open("day9.txt")

groupStack = []
garbage = False
ignoreNext = False
characterCount = 0

for line in f1:
    stream = line.strip()

for i in stream:
    if ignoreNext == True:
        ignoreNext = False
    elif i == '!' and garbage == True:
        ignoreNext = True
    elif i == '{' and garbage != True:
        groupStack.append(i)
    elif i == '}' and garbage != True:
        groupStack.pop()
    elif i == '<' and garbage != True:
        garbage = True
    elif i == ">":
        garbage = False
    elif garbage == True:
        characterCount += 1

print(characterCount)
