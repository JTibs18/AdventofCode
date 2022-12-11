import math

# Part 1 Solution
f1 = open("day11.txt")

monkies = []
monkeyProfile = dict()

for line in f1:
    note = line.strip().split(' ') 
    if note[0] == "Monkey": 
        monkeyProfile["monkey"] = int(note[1].strip(':'))
    elif note[0] == "Starting": 
        items = []
        for i in range(2, len(note)):
            items.append(int(note[i].strip(',')))
        monkeyProfile["items"] =  items
    elif note[0] == "Operation:":
        monkeyProfile["operator"] = note[4]
        monkeyProfile["amount"] = note[5]
    elif note[0] == "Test:":
        monkeyProfile["test"] = int(note[3]) 
        testInstruction = True 
    elif len(note) > 1 and note[1] == "true:": 
        monkeyProfile["true"] = int(note[5])
    elif len(note) > 1 and note[1] == "false:": 
        monkeyProfile["false"] = int(note[5])
    else: 
        monkies.append(monkeyProfile)
        monkeyProfile = dict()

monkies.append(monkeyProfile)
monkeyInspectionCount = [0] * len(monkies)

for r in range (0, 20): 
    for m in monkies: 
        for i in m['items']:
            monkeyInspectionCount[m['monkey']] += 1

            if m['amount'] == 'old':
                amount = i 
            else: 
                amount = int(m['amount'])

            if m['operator'] == '*':
                worryLevel = i * amount
            elif m['operator'] == '+':
                worryLevel = i + amount

            worryLevel = math.floor(worryLevel / 3)

            if worryLevel % m['test'] == 0: 
                monkies[m['true']]['items'].append(worryLevel)
            else: 
                monkies[m['false']]['items'].append(worryLevel)
        m['items'] = []

monkeyCountOrder = sorted(monkeyInspectionCount, reverse=True)
print(monkeyCountOrder[0] * monkeyCountOrder[1])

# Part 2 Solution
# Thanks reddit clue: devise a greatest common divisor by multiplying the "divisible by" numbers together and then modulo each new worry level by that number.
f1 = open("day11.txt")

monkies = []
monkeyProfile = dict()

for line in f1:
    note = line.strip().split(' ') 
    if note[0] == "Monkey": 
        monkeyProfile["monkey"] = int(note[1].strip(':'))
    elif note[0] == "Starting": 
        items = []
        for i in range(2, len(note)):
            items.append(int(note[i].strip(',')))
        monkeyProfile["items"] =  items
    elif note[0] == "Operation:":
        monkeyProfile["operator"] = note[4]
        monkeyProfile["amount"] = note[5]
    elif note[0] == "Test:":
        monkeyProfile["test"] = int(note[3]) 
        testInstruction = True 
    elif len(note) > 1 and note[1] == "true:": 
        monkeyProfile["true"] = int(note[5])
    elif len(note) > 1 and note[1] == "false:": 
        monkeyProfile["false"] = int(note[5])
    else: 
        monkies.append(monkeyProfile)
        monkeyProfile = dict()

monkies.append(monkeyProfile)
monkeyInspectionCount = [0] * len(monkies)
specialNumber = 1

for m in monkies: 
    specialNumber = specialNumber * m['test'] 

for r in range (0, 10000): 
    for m in monkies: 
        for i in m['items']:
            monkeyInspectionCount[m['monkey']] += 1

            if m['amount'] == 'old':
                amount = i 
            else: 
                amount = int(m['amount'])

            if m['operator'] == '*':
                worryLevel = i * amount
            elif m['operator'] == '+':
                worryLevel = i + amount

            worryLevel = worryLevel % specialNumber
            
            if worryLevel % m['test'] == 0: 
                monkies[m['true']]['items'].append(worryLevel)
            else: 
                monkies[m['false']]['items'].append(worryLevel)
        m['items'] = []

monkeyCountOrder = sorted(monkeyInspectionCount, reverse=True)
print(monkeyCountOrder[0] * monkeyCountOrder[1])
