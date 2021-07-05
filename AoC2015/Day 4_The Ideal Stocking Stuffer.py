# #Part 1 Solution
import hashlib 
n = []
key = "bgvyzdsv"
for i in range(500000): 
    k = key + str(i) 
    x = (hashlib.md5(k.encode()))
    x = x.hexdigest()
    if x[0] == "0" and x[1] == "0" and x[2] == "0" and x[3] == "0" and x[4] == "0":    
        n = i
        break
print(n) 

#Part 2 Solution
import hashlib 
n = []
key = "bgvyzdsv"
for i in range(2000000): 
    k = key + str(i) 
    x = (hashlib.md5(k.encode()))
    x = x.hexdigest()
    if x[0] == "0" and x[1] == "0" and x[2] == "0" and x[3] == "0" and x[4] == "0" and x[5] == "0":    
        n = i
        break
print(n) 