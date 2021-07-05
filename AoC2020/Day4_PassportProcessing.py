#Part 1 Solution
f1 = open("day4Input.txt") 
passPort = []
curLine = ""
valid = 0

for line in f1: 
        line = line.rstrip()
        print(line)
        if not line.strip():
            passPort.append(curLine)
            print (curLine)
            curLine = "" 
        else: 
            curLine = curLine + " " + line 
passPort.append(curLine)           

for p in passPort: 
    print(p)
    if ((p.find("iyr") != -1 ) and (p.find("byr") != -1) and (p.find("eyr") != -1) and (p.find("ecl") != -1 ) and (p.find("hgt") != -1) and (p.find("hcl") != -1) and (p.find("pid") != -1)):
        valid = valid + 1 

print(valid)

#Part 2 Solution
f1 = open("day4Input.txt") 
passPort = []
curLine = ""
valid = 0

for line in f1: 
        line = line.rstrip()
        print(line)
        if not line.strip():
            passPort.append(curLine)
            print (curLine)
            curLine = "" 
        else: 
            curLine = curLine + " " + line 
passPort.append(curLine)           

for p in passPort: 
    print(p)
    passPoints = 0
    if ((p.find("iyr") != -1 ) and (p.find("byr") != -1) and (p.find("eyr") != -1) and (p.find("ecl") != -1 ) and (p.find("hgt") != -1) and (p.find("hcl") != -1) and (p.find("pid") != -1)):
        fields = p.split()
        for i in fields: 
            if (i.find("iyr") != -1): 
                data = i.split(":")
                if (len(data[1]) == 4 and (int(data[1]) >= 2010 and int(data[1]) <= 2020)):
                    passPoints = passPoints + 1
          
            if (i.find("byr") != -1): 
                data = i.split(":")
                if (len(data[1]) == 4 and (int(data[1]) >= 1920 and int(data[1]) <= 2002)):
                    passPoints = passPoints + 1
          
            if (i.find("eyr") != -1): 
                data = i.split(":")
                if (len(data[1]) == 4 and (int(data[1]) >= 2020 and int(data[1]) <= 2030)):
                    passPoints = passPoints + 1

            if (i.find("hgt") != -1): 
                data = i.split(":")
                if (data[1].find("cm") != -1):
                    num = data[1].split("cm")
                    if ((int(num[0]) >= 150) and (int(num[0]) <= 193)):
                        passPoints = passPoints + 1
                elif(data[1].find("in") != -1):
                    num = data[1].split("in")
                    print(num[0])
                    if ((int(num[0]) >= 59) and (int(num[0]) <= 76)):
                        passPoints = passPoints + 1

            if (i.find("hcl") != -1): 
                data = i.split(":")
                if ((data[1].find("#")) != -1 and (len(data[1]) ==7)):
                    passPoints = passPoints + 1
                    
            if (i.find("ecl") != -1): 
                data = i.split(":")
                if ((data[1].find("amb") != -1) or (data[1].find("blu") != -1) or (data[1].find("brn") != -1) or (data[1].find("gry") != -1) or (data[1].find("grn") != -1) or (data[1].find("hzl") != -1)  or (data[1].find("oth") != -1) )   :
                    passPoints = passPoints + 1
            
            if (i.find("pid") != -1): 
                data = i.split(":")
                if (len(data[1]) == 9):
                    passPoints = passPoints + 1
                    
    if passPoints == 7: 
        valid = valid + 1

print(valid)
      
