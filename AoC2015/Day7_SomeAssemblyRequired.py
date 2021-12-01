#Part 1 Solution
f1 = open("day7.txt")
signals = {}
knownVal = {}
toSolve = {}

def getSig(nSig):
    if isinstance(nSig, int) == True:
        print(nSig)
        return nSig
    elif "AND" in nSig:
        print("AND")
    elif "OR" in nSig:
        print("OR")
        op = nSig.split(" OR ")
        first = signals.get(op[0])
        second = signals.get(op[1])
        print(first, second)
        return getSig(first) | getSig(second)
    elif "LSHIFT" in nSig:
        print("LSHIFT")
    elif "RSHIFT" in nSig:
        print("RSHIFT")
    elif "NOT" in nSig:
        print("NOT")
    else:
        print(nSig)
        n = signals.get(nSig)
        getSig(n)

for line in f1:
    line = line.rstrip()
    splat = line.split(" -> ")
    signals[splat[1]] = splat[0]
    # print(splat[1], splat[0])

for key, val in signals.items():
    if val.isdigit() == True:
        knownVal[key] = val
    else:
        val = val.split()
        toSolve[key] = val



#to remove key from dict = toSolve.pop(key)


#while "a" not in knownVal:

# print(knownVal)
# newSig = signals.get("a")
# getSig(newSig)
