# Part 1 Solution
from copy import deepcopy

f1 = open("day11.txt")

# layout = []
# changed = 1
# seatsOccupiedCount = 0

# for line in f1:
#     layout.append(list(line.strip()))

# newLayout = deepcopy(layout)

# while changed != 0: 
#     changed = 0 
#     layout = deepcopy(newLayout)
#     for y, row in enumerate(layout): 
#         for x, seat in enumerate(row): 
#             if seat == ".": 
#                 continue 
#             if seat == "L": 
#                 if (x - 1 >= 0 and layout[y][x-1] != "#") and (x - 1 >= 0 and y - 1 >= 0 and layout[y-1][x-1] != "#") and (y - 1 >= 0 and layout[y-1][x] != "#") and (x + 1 < len(row) and y - 1 >= 0 and layout[y - 1][x + 1] != "#") and (x + 1 < len(row) and layout[y][x + 1] != "#") and (x + 1 < len(row) and y + 1 < len(layout) and layout[y + 1][x + 1] != "#") and (y + 1 < len(layout) and layout[y + 1][x] != "#") and (x - 1 >= 0 and y + 1 < len(layout) and layout[y + 1][x] != "#"): 
#                     newLayout[y][x] = "#"
#                     changed += 1
#             elif seat == "#": 
#                 occupiedCount = 0 
#                 if x - 1 >= 0 and layout[y][x-1] == "#": 
#                     occupiedCount += 1
#                 if x - 1 >= 0 and y - 1 >= 0 and layout[y-1][x-1] == "#": 
#                     occupiedCount += 1
#                 if y - 1 >= 0 and layout[y-1][x] == "#":
#                     occupiedCount += 1
#                 if x + 1 < len(row) and y - 1 >= 0 and layout[y - 1][x + 1] == "#":
#                     occupiedCount += 1 
#                 if x + 1 < len(row) and layout[y][x + 1] == "#":
#                     occupiedCount += 1
#                 if x + 1 < len(row) and y + 1 < len(layout) and layout[y + 1][x + 1] == "#": 
#                     occupiedCount += 1
#                 if y + 1 < len(layout) and layout[y + 1][x] == "#":
#                     occupiedCount += 1
#                 if x - 1 >= 0 and y + 1 < len(layout) and layout[y + 1][x] == "#":
#                     occupiedCount += 1

#                 if occupiedCount >= 4: 
#                     newLayout[y][x] = "L"
#                     changed += 1 
                
#     print(newLayout)
#     break

# for i in layout: 
#     if i == "#":
#         seatsOccupiedCount += 1 

# print(seatsOccupiedCount)

# This makes the incorrect assumption that "BESIDE IT" meant index directly next to current index. Actually means seat directly desire the next seat 
