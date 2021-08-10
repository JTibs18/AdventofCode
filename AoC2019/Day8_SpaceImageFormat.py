# Part 1 Solution
f1 = open("day8.txt")
for line in f1:
    line = line.strip("/n")

layers = []
width = []
cur = []

for indx, num in enumerate(line):
    if indx % 25 == 0 and indx != 0:
        width.append(cur)
        cur = []
    if num != "\n":
        cur.append(num)

if cur != []:
    width.append(cur)

cur = []

for indx, w in enumerate(width):
    if indx % 6 == 0 and indx != 0:
        layers.append(cur)
        cur = []
    cur.append(w)

if cur != []:
    layers.append(cur)

layCount = []
for l in layers:
    count = 0
    for w in l:
        for pixel in w:
            if int(pixel) == 0:
                count += 1
    layCount.append(count)

oneCount = 0
twoCount = 0

for l in layers[layCount.index(min(layCount))]:
    for pixel in l:
        if int(pixel) == 1:
            oneCount += 1
        elif int(pixel) == 2:
            twoCount += 1

print(oneCount * twoCount)

#Part 2 Solution
f1 = open("day8.txt")
for line in f1:
    line = line.strip("/n")

pixels = [[] * 150 for i in range(150)]
image = []
width = []
cur = []

for indx, num in enumerate(line):
    if num != "\n":
        pixels[indx % 150].append(num)

for p in pixels:
    dp = - 1
    for x in p:
        if int(x) == 0:
            dp = 0
            break
        elif int(x) == 1:
            dp = 1
            break
        elif dp < 0:
            dp = 2
    image.append(dp)

for indx, num in enumerate(image):
    if indx % 25 == 0 and indx != 0:
        width.append(cur)
        cur = []
    cur.append(num)

if cur != []:
    width.append(cur)

for i in width:
    for x in i:
        if int(x) == 1:
            print(x, end = '')
        else:
            print(" ", end = '')
    print("")
