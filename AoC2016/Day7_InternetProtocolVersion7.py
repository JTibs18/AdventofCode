# #Part 1 Solution
f1 = open("day7.txt")

count = 0

for line in f1:
    line = line.strip("\n")

    charSequence = []
    seq = []
    found = False
    ex = False
    con = 0
    exclude = False

    for char in line:
        if char != "[" and char != "]" and (len(charSequence) == 0 or charSequence[-1] != char):
            if len(seq) > 0:
                charSequence.append(seq[0])
            charSequence.append(char)
            con = 0
            seq = []
        elif char == "[":
            exclude = True
            seq = []
            con = 0
            charSequence = []
        elif char == "]":
            exclude = False
            seq = []
            con = 0
            charSequence = []
        elif charSequence[-1] == char:
            charSequence.pop()
            con += 1
            seq.append(char)
            
            if con == 2 and seq[0] != seq[1] and exclude == False:
                found = True
            elif con == 2 and seq[0] != seq[1] and exclude == True:
                ex = True

    if found == True and ex == False:
        count += 1
print(count)

#Part 2 Solution
f1 = open("day7.txt")

count = 0

for line in f1:
    line = line.strip("\n")

    out = []
    inner = []
    exclude = False

    for idx, char in enumerate(line):
        if char != "[" and char != "]" and (idx - 1 >= 0 and idx + 1 <= len(line) - 1):
            if line[idx - 1] != "]" and line[idx - 1] != "[" and line[idx + 1] != "]" and line[idx + 1] != "[":
                if line[idx - 1] == line[idx + 1]:
                    if exclude == False:
                        innerC = char
                        outerC = line[idx - 1]
                        out.append((innerC, outerC))
                    elif exclude == True:
                        bInnerC = char
                        bOuterC = line[idx - 1]
                        inner.append((bOuterC, bInnerC))

        elif char == "[" :
            exclude = True
        elif char == "]":
            exclude = False

    if len(out) > 0 and len(inner) > 0:
        for i in out:
            if i in inner:
                count += 1
                break

print(count)
