import hashlib
import operator

#Part 1 Solution
f1 = open("day5.txt")

password = ""
count = 0

for line in f1:
    code = line.strip("\n")

while len(password) < 8:
    toHash = code + str(count)
    hashed = hashlib.md5(toHash.encode('utf-8')).hexdigest()
    if hashed[0] == "0" and hashed[1] == "0" and hashed[2] == "0" and hashed[3] == "0" and hashed[4] == "0":
        password += hashed[5]
    count += 1
print(password)

#Part 2 Solution
f1 = open("day5.txt")

password = []
passedIndex = []
count = 0

for line in f1:
    code = line.strip("\n")

while len(password) < 8:
    toHash = code + str(count)
    hashed = hashlib.md5(toHash.encode('utf-8')).hexdigest()
    if hashed[0] == "0" and hashed[1] == "0" and hashed[2] == "0" and hashed[3] == "0" and hashed[4] == "0":
        index = hashed[5]
        if index.isdigit() == True and int(index) < 8 and index not in passedIndex:
            password.append([int(index), hashed[6]])
            passedIndex.append(index)
    count += 1
print((sorted(password, key=operator.itemgetter(0))))
