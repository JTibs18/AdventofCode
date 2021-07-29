#Part 1 Solution
f1 = open("day4.txt")

for indx, line in enumerate(f1):
    line = line.strip("/n").split("-")

start = int(line[0])
end = int(line[1])
valid = 0

for num in range(start, end):
    n = str(num)
    if (n[0] == n[1] or n[1] == n[2] or n[2] == n[3] or n[3] == n[4] or n[4] == n[5]) and n[0] <= n[1] and n[1] <= n[2] and n[2] <= n[3] and n[3] <= n[4] and n[4] <= n[5]:
          valid += 1

print(valid)

#Part 2 Solution
f1 = open("day4.txt")

for indx, line in enumerate(f1):
    line = line.strip("/n").split("-")

start = int(line[0])
end = int(line[1])
valid = 0

for num in range(start, end):
    n = str(num)
    if ((n[0] == n[1] and n[1] != n[2]) or (n[1] == n[2] and n[1] != n[0] and n[2] != n[3]) or (n[2] == n[3] and n[2] != n[1] and n[3] != n[4]) or (n[3] == n[4] and n[3] != n[2] and n[4] != n[5]) or (n[4] == n[5]) and n[4] != n[3]) and n[0] <= n[1] and n[1] <= n[2] and n[2] <= n[3] and n[3] <= n[4] and n[4] <= n[5]:
          valid += 1

print(valid)
