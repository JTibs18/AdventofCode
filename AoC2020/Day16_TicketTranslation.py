# Part 1 Solution
f1 = open("day16.txt")

rules = []
parsedRules = []
data = []
parseRules = True
parseData = False
errorRate = 0

# parse input
for line in f1:
    if line.strip() == "nearby tickets:":
        parseData = True
    elif line.strip() == "your ticket:":
        parseRules = False
    elif parseRules == True and line != '\n':
        curRule = line.strip().split()
        rules.append(curRule[len(curRule) - 3])
        rules.append(curRule[len(curRule) - 1])
    elif parseData == True:
        curData = line.strip().split(",")
        data.extend(curData)

# combining rule ranges for efficiency
for i in rules:
    ranges = i.split("-")
    ranges = [int(x) for x in ranges]
    parsedRules.append(ranges)

efficientRules = []
parsedRules = sorted(parsedRules)
efficientRules.append(parsedRules[0])

for i in parsedRules[1:]:
    if efficientRules[-1][0] <= i[0] and i[0] <= efficientRules[-1][1]:
        efficientRules[-1][1] = max(efficientRules[-1][1], i[1])
    else:
        efficientRules.append(i)

# iterating through data, testing against rules, counting error rate 
for i in data:
    valid = False
    for j in efficientRules:
        if j[0] <= int(i) and int(i) <= j[1]:
            valid = True
            break
    if valid == False:
        errorRate += int(i)

print(errorRate)

# Part 2 Solution
from copy import deepcopy

f1 = open("day16.txt")

rules = []
ticketRules = []
data = []
validTickets = []
categories = []
parseRules = True
parseData = False
valid = False 
myTicket = []

# parse input
for line in f1:
    if line.strip() == "nearby tickets:":
        parseData = True
    elif line.strip() == "your ticket:":
        parseRules = False
    elif parseRules == True and line != '\n':
        curRule = line.strip().split(":")
        categories.append(curRule[0])
        ranges = curRule[1].strip().split(' or ')
        rules.append(ranges[0])
        rules.append(ranges[1])
    elif parseData == True:
        curData = line.strip().split(",")
        data.append(curData)
    elif parseRules == False and parseData == False and line != '\n': 
        myTicket = line.strip().split(",")

# combining rule ranges for efficiency and maintaining initial rule ranges
for i in rules:
    ranges = i.split("-")
    ranges = [int(x) for x in ranges]
    ticketRules.append(ranges)

parsedRules = sorted(deepcopy(ticketRules))
efficientRules.append(parsedRules[0])

for i in parsedRules[1:]:
    if efficientRules[-1][0] <= i[0] and i[0] <= efficientRules[-1][1]:
        efficientRules[-1][1] = max(efficientRules[-1][1], i[1])
    else:
        efficientRules.append(i)

# iterating through data, testing against rules, finding valid tickets 
for ticket in data:
    for i in ticket: 
        valid = False 
        for j in efficientRules:
            if j[0] <= int(i) and int(i) <= j[1]:
                valid = True 
                break
        if valid == False:
            break 
    if valid == True: 
        validTickets.append(ticket)

fields = [deepcopy(categories) for i in range(len(categories))]

# eliminating possible categories 
rulesIndx = 0
categoryIndx = 0
validTickets.append(myTicket)

for ticket in validTickets: 
    for indx, val in enumerate(ticket): 
        while rulesIndx < len(ticketRules) - 1: 
            if (int(val) < ticketRules[rulesIndx][0] or int(val) > ticketRules[rulesIndx][1]) and (int(val) < ticketRules[rulesIndx + 1][0] or int(val) > ticketRules[rulesIndx + 1][1]):
                if categories[categoryIndx] in fields[indx]: 
                    fields[indx].remove(categories[categoryIndx])
            rulesIndx += 2
            categoryIndx += 1 
        rulesIndx = 0
        categoryIndx = 0 

# finding single categories that are solved 
unsolved = 0 
toRemove = []

for i in fields: 
    if len(i) == 1: 
        toRemove.append(i[0])
    else: 
        unsolved += 1

# resolving all unsolved categories 
while unsolved: 
    for i in fields: 
        if len(i) > 1: 
            for f in i: 
                if f in toRemove: 
                    i.remove(f)
            if len(i) == 1: 
                unsolved -= 1 
                toRemove.append(i[0])

# mapping fields to my ticket and calculating final value
value = 1

for indx, val in enumerate(fields): 
    if "departure" in val[0]: 
        value *= int(myTicket[indx])

print(value)