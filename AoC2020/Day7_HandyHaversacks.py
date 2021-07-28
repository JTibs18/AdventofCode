#Part 1 Solution
import re

f1 = open("day7.txt")
bagContains = dict()
holdBag = set()
lineOfBags = []

for line in f1:
    line = line.rstrip()
    lineOfBags.append(line)

for b in lineOfBags:
    bags = []

    manyBags = b.split("contain")
    fb = re.sub(r'[.]', '', manyBags[0])
    fs = re.sub(r'[.]', '', manyBags[1])
    fs = re.sub(r'[0-9]', '', fs)
    fb = re.sub(r'[0-9]', '', fb)
    fb = fb.replace("bags", "")
    fs = fs.replace("bags", "")
    fs = fs.replace("bag", "")
    fs = fs.split(",")
    fb = fb.strip()

    for i in fs:
        i = i.strip()
        bags.append(i)

    bagContains[fb] = bags

q = ["shiny gold"]

while q:
    for key, val in bagContains.items():
        if q[0] in val:
            holdBag.add(key)
            q.append(key)
    q.pop(0)

print(len(holdBag))

#Part 2 Solution
f1 = open("day7.txt")
bagContains = dict()
holdBag = set()
lineOfBags = []

for line in f1:
    line = line.rstrip()
    lineOfBags.append(line)

for b in lineOfBags:
    bags = []

    manyBags = b.split("contain")
    fb = re.sub(r'[.]', '', manyBags[0])
    fs = re.sub(r'[.]', '', manyBags[1])
    fb = fb.replace("bags", "")
    fs = fs.replace("bags", "")
    fs = fs.replace("bag", "")
    fs = fs.split(",")
    fb = fb.strip()

    for i in fs:
        i = i.strip()
        bags.append(i)

    bagContains[fb] = bags

s = []
bgs = []
q = []
bagCount = dict()

q.extend(bagContains["shiny gold"])

while q:
    if q[0] != "no other":
        s.append(q[0][2:])
        q.extend(bagContains[q[0][2:]])
    q.pop(0)

while s:
    cur = s.pop()
    b = bagContains[cur]
    sum = 0

    for i in b:
        if "no other" in i:
            sum += 0
        else:
            sum += int(i[0])
            if cur not in bgs:
                bgs.append(cur)
    bagCount[cur] = sum
bgs.append("shiny gold")

for b in bgs:
    inside = bagContains[b]
    sum = 0
    for bg in inside:
        multi = int(bg[0])
        sum = sum + (int(bagCount[bg[2:]]) * multi) + multi
    bagCount[b] = sum

print(bagCount["shiny gold"])
