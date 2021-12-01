#Part 1 Solution
f1 = open("day4.txt")

count = 0

for lines in f1:
    cur = lines.strip("\n").split(" ")

    phrases = set()
    dup = False

    for i in cur:
        if i not in phrases:
            phrases.add(i)
        else:
            dup = True
            break
    if dup == False:
        count += 1

print(count)

#Part 2 Solution
f1 = open("day4.txt")

count = 0

for lines in f1:
    cur = lines.strip("\n").split(" ")

    phrases = set()
    dup = False

    for i in cur:
        i = ''.join(sorted(i))
        if i not in phrases:
            phrases.add(i)
        else:
            dup = True
            break
    if dup == False:
        count += 1

print(count)
