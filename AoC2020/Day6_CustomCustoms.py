#Part 1 Solution
f1 = open("day6Input.txt") 
yesLetts = []
count = 0 
curLett = ""

for line in f1:   
    line = line.rstrip()  
    if not line.strip():
            for i in curLett:
                if i not in yesLetts: 
                    yesLetts.append(i)
            curLett = ""
            count = count + (len(yesLetts))
            yesLetts = [] 
    else: 
            curLett = curLett + "" + line  
print (count)

#Part 2 Solution
f1 = open("day6Input.txt") 
yesLetts = []
letterList = []
noLetters = []
group = []
count = 0 

for line in f1:   
    line = line.rstrip()  

    if not line.strip():
        for c, i in enumerate(group):
            if c == 0 and len(group) > 1:
                for j in i:
                    letterList.append(j)
                    print(j)
            elif c == 0:
                for j in i:
                    yesLetts.append(j)
            else: 
                for j in letterList:
                    if j in i and j not in yesLetts and j not in noLetters: 
                        yesLetts.append(j)
                    elif j not in i and j in yesLetts: 
                        yesLetts.remove(j)
                        noLetters.append(j)
                    elif j not in i: 
                        noLetters.append(j)
            for i in noLetters: 
                if i in yesLetts: 
                    yesLetts.remove(i)

            print(yesLetts)

        count = count + (len(yesLetts))
        print(count)
        yesLetts = [] 
        noLetters = []
        letterList = [] 
        group = []
    else: 
        group.append(line)  

print (count)