#Part 1 Solution
import operator
f1 = open("day4.txt")

idSum = 0

for line in f1:
    numChar = dict()
    checkSum = False
    mostEncrypted = []
    count = 0
    eNum = ""

    line = line.strip("\n")
    for char in line:
        if char == '[':
            checkSum = True
            mostEncrypted = dict(sorted(numChar.items(), key=operator.itemgetter(1), reverse =True)[:5])
            prevCount = max(mostEncrypted.values())
        elif char != "-" and char != "[" and char != "]" and checkSum == False:
            if char.isdigit() == True:
                eNum += char
            elif char in numChar:
                num = numChar.get(char)
                num += 1
                numChar[char] = num
            else:
                numChar[char] = 1
        elif checkSum == True and char != "[" and char != "]":
            if (char in mostEncrypted or numChar.get(char) == min(mostEncrypted.values())) and numChar.get(char) <= prevCount:
                count += 1
                prevCount = numChar.get(char)
        elif char == "]" and count == 5:
            idSum += int(eNum)

print(idSum)

#Part 2 Solution
f1 = open("day4.txt")

for line in f1:
    eNum = ""
    charList = []
    shifted = ""

    line = line.strip("\n")
    for char in line:
        if char != "[" and char != "]":
            if char.isdigit() == True:
                eNum += char
            else:
                charList.append(char)
        elif char == "[":
            shift = int(eNum) % 26
            for c in charList:
                if c == "-":
                    shifted += " "
                elif c == "z" and shift > 0:
                    shifted += chr(97 + shift - 1)
                else:
                    newC = ord(c) + shift
                    if newC > 122:
                        over = newC - 123
                        shifted += chr(97 + over)
                    else:
                        shifted += chr(newC)
            if "northpole object" in shifted:
                print(int(eNum))
