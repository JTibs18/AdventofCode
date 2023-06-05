#Part 1 Solution
f1 = open("day7.txt")

programs = {}

for line in f1:
    line = line.strip().split("(")
    child = line[1].strip().split("> ")
    if "-" in line[1]:
        children = child[1].split(", ")
        parent = line[0].strip()
        if parent not in programs:
            programs[parent] = 0
        for i in children:
            programs[i] = 1

for key, value in programs.items():
    if value == 0:
        print(key)

#Part 2 Solution
f1 = open("day7.txt")

programWeight = {}
parChild = {}

for line in f1:
    line = line.strip().split("(")
    child = line[1].strip().split("> ")

    c = child[0].strip(") -")
    parent = line[0].strip()

    programWeight[parent] = int(c)
    # print(programWeight)

    if "-" in line[1]:
        children = child[1].split(", ")
        # print(children)
        parChild[parent] = children
# print(parChild)

for i in parChild:
    val = set()
    for j in parChild.get(i):
        # print(j)
        if j in parChild:
            # print("TRUE")
            sum = 0
            for x in parChild.get(j):
                # print(programWeight.get(x))
                sum += programWeight.get(x)
            sum += programWeight.get(j)
            val.add(sum)

            # parChild[i].extend(parChild.get(j))
        else:
            val.add(programWeight.get(j))
    if len(val) > 1:
        # print("THIS", val)
        v = list(val)
        diff = abs(v[0] - v[1])
        print("DIFF", diff, val)
        #PROBLEM : THIS SHOULD ONLY HAPPEN ONCE BUT HAPPENS MANY TIMES IN THE GIVEN INPUT
        #ONLY DEPTH OF 2 IS CONSIDERED, HIGHER DEPTHS OF TOWERS ARE NOT CONSIDERED :/ 



# print(parChild)

# for i in parChild:
#     val = set()
#     for j in parChild.get(i):
#         val.add(programWeight.get(j))
#     print("V", val)
#     print(i)
#     print(parChild.get(i))
