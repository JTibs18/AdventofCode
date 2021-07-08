#Part 1 Solution
f1 = open("day2.txt")

checkSum = 0

for line in f1:
    line = line.strip("\n")
    nums = line.split()
    nums = list(map(int, nums))
    diff = int(max(nums)) - int(min(nums))
    checkSum += diff
print(checkSum)

#Part 2 Solution
f1 = open("day2.txt")

checkSum = 0

for line in f1:
    line = line.strip("\n")
    nums = line.split()
    nums = list(map(int, nums))
    nums = sorted(nums, reverse=True)
    p1 = 0
    p2 = 1
    while p1 < len(nums):
        if p1 < p2 and nums[p1] % nums[p2] == 0:
            checkSum += nums[p1] // nums[p2]
            break
        elif p2 == len(nums) - 1:
            p1 += 1
            p2 = p1 + 1
        else:
            p2 += 1
print(checkSum)
