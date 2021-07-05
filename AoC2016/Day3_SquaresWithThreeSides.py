#Part 1 Solution
f1 = open("day3.txt")

valid = 0

for line in f1:
    line = line.strip("\n")
    triangle = []
    nums = line.strip().split("  ")
    for i in nums:
        i = i.strip()
        if i != "":
            triangle.append(int(i))
    s = sum(triangle)
    m = max(triangle)
    if s - m > m:
        valid += 1
print(valid)

#Part 2 Solution
f1 = open("day3.txt")

valid = 0
count = 0
innerC = 0
tri1 = []
tri2 = []
tri3 = []

for line in f1:
    line = line.strip("\n")
    nums = line.strip().split("  ")

    for idx, val in enumerate(nums):
        number = val.strip()

        if number != "":
            if innerC == 0:
                tri1.append(int(val))
                innerC += 1
            elif innerC == 1:
                tri2.append(int(val))
                innerC += 1
            elif innerC == 2:
                tri3.append(int(val))
                innerC = 0
            count += 1

        if count == 9:
            if len(tri1) != 0:
                s = sum(tri1)
                m = max(tri1)
                if s - m > m:
                    valid += 1
            if len(tri2) != 0:
                s = sum(tri2)
                m = max(tri2)
                if s - m > m:
                    valid += 1
            if len(tri3) != 0:
                s = sum(tri3)
                m = max(tri3)
                if s - m > m:
                    valid += 1
            count = 0
            tri1 = []
            tri2 = []
            tri3 = []
print(valid)
