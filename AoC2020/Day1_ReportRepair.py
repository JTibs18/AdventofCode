#Part 1 Solution
f1 = open("day1Input.txt") 
nums = [] 
num1 = 0
num2 = 0

for line in f1: 

        line = line.rstrip() 
        nums.append(line)

for n in nums: 
        for n2 in nums: 
                if ((int(n) + int(n2)) == int(2020)): 
                        num1 = int(n) 
                        num2 = int(n2)
                        break

print(num1 * num2)



#Part 2 Solution 
f1 = open("day1Input.txt") 
nums = [] 
num1 = 0
num2 = 0
num3 = 0

for line in f1: 

        line = line.rstrip() 
        nums.append(line)

for n in nums: 
        for n2 in nums: 
                for n3 in nums: 
                        if ((int(n) + int(n2) + int(n3)) == int(2020)): 
                                num1 = n
                                num2 = n2 
                                num3 = n3
                                break 

print(int(num1) * int(num2)* int(num3))