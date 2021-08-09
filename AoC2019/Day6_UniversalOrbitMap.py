#Part 1 Solution
f1 = open("day6.txt")

orbits = []
for line in f1:
    line = line.rstrip()
    orbits.append(line)

oDict = dict()
q = []
oCount = 0

for i in orbits:
    planets = i.split(")")
    if planets[1] not in oDict:
        oDict[planets[1]] = [planets[0]]
    else:
        oDict[planets[1]].extend(planets[0])

for key, val in oDict.items():
    q.extend(val)
    while q:
        s = q.pop(0)
        if s in oDict:
            oDict[key].extend(x for x in oDict[s] if x not in oDict[key])
            q.extend(x for x in oDict[s] if x not in q)

for key, val in oDict.items():
    oCount += len(val)

print(oCount)

#Part 2 Solution
f1 = open("day6.txt")

orbits = []
for line in f1:
    line = line.rstrip()
    orbits.append(line)

oDict = dict()
q = []
oCount = 0

for i in orbits:
    planets = i.split(")")
    if planets[1] not in oDict:
        oDict[planets[1]] = [planets[0]]
    else:
        oDict[planets[1]].append(planets[0])

    if planets[0] not in oDict:
        oDict[planets[0]] = [planets[1]]
    elif planets[1] not in oDict[planets[0]]:
        oDict[planets[0]].append(planets[1])

main = oDict["YOU"]
contacts = []
count = 0

while main:
    for x in oDict[main[0]]:
        if x not in contacts:
            contacts.append(x)

    if main[0] in oDict["SAN"] or "SAN" in oDict[main[0]]:
        print(count)
        break

    main.pop(0)
    if len(main) == 0:
        main.extend(contacts)
        contacts = []
        count += 1
