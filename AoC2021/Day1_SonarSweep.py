#Part 1 Solution
f1 = open("day1.txt")

first = True
count = 0

for line in f1:
    line = line.strip("\n")
    if first == True:
        first = False
    else:
        if prev < int(line):
            count += 1
    prev = int(line)
print(count)

#Part 2 Solution
f1 = open("day1.txt")

nums = []
count = 0

for line in f1:
    line = line.strip("\n")
    nums.append(int(line))

front = 0
back = 3
first = True

while back <= len(nums):
    if first == True:
        first = False
    else:
        if prev < sum(nums[front:back]):
            count +=1
    prev = sum(nums[front:back])
    front += 1
    back += 1
print(count)
