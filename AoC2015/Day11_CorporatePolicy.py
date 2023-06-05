#Part 1 Solution
def newLetter(letter):
    print(letter)
    print(ord(letter))
    newASCIILetter = ord(letter) + 1

    if newASCIILetter == 105 or newASCIILetter == 108 or newASCIILetter == 111:
        newASCIILetter += 1

    if newASCIILetter > 122:
        return('a')
    else:
        return chr(newASCIILetter)

f1 = open("day11.txt")

for line in f1:
    data = line.strip()

indexLetterOfInterest = 7
newPassword = []
newPassword.extend(data)
print(len(newPassword), newPassword)

while indexLetterOfInterest >= 0:

    letterOfInterest = str(newPassword[indexLetterOfInterest])
    print("TES", newPassword[indexLetterOfInterest])

    newLett = newLetter(letterOfInterest)

    if newLetter == 'a':
        newPassword[indexLetterOfInterest] = 'a'
        indexLetterOfInterest -= 1
    else:
        newPassword[indexLetterOfInterest] = newLetter
        print(newPassword)

# def threeIncreasingLetters():
#
# def twoPairLetters():
