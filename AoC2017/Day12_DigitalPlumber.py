# Part 1 Solution
f1 = open("day12.txt")

pipe = dict()
idsConnectedToZero = set()

for line in f1:
    ids = line.strip().split(" <-> ")
    pipe[ids[0]] = ids[1].split(',')

queue = []
for i in pipe['0']:
    queue.append(i.lstrip())

while (len(queue) > 0):
    cur = queue[0].lstrip()
    idsConnectedToZero.add(cur)
    for i in pipe[cur]:
        compare = i.lstrip()
        if compare not in idsConnectedToZero and compare not in queue:
            queue.append(compare)
    queue.pop(0)

print(len(idsConnectedToZero))

# Part 2 Solution
f1 = open("day12.txt")

pipe = dict()
groupCount = 0
inGroup = set()

for line in f1:
    ids = line.strip().split(" <-> ")
    pipe[ids[0]] = ids[1].split(',')

for i in pipe:
    idsConnected = set()
    if i not in inGroup:
        groupCount += 1
        inGroup.add(i)
        queue = []
        for j in pipe[i]:
            queue.append(j.lstrip())

        while (len(queue) > 0):
            cur = queue[0].lstrip()
            idsConnected.add(cur)
            inGroup.add(cur)
            for j in pipe[cur]:
                compare = j.lstrip()
                if compare not in idsConnected and compare not in queue:
                    queue.append(compare)
            queue.pop(0)

print(groupCount)
