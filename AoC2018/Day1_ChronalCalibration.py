#Part 1 Solution
f1 = open("day1.txt")

frequency = 0

for line in f1:
    line = line.strip("\n")
    if line[0] == "-":
        frequency -= int(line[1:])
    else:
        frequency += int(line[1:])
print(frequency)

#Part 2 Solution
f1 = open("day1.txt")

frequency = 0
count = 0
freq = set()
nums = []

for line in f1:
    line = line.strip("\n")
    nums.append(line)

while True:
    if nums[count][0] == "-":
        frequency -= int(nums[count][1:])
    else:
        frequency += int(nums[count][1:])

    if frequency in freq:
        print(frequency)
        break
    else:
        freq.add(frequency)

    count += 1
    if count == len(nums):
        count = 0
