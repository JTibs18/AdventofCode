#Part 1 Solution
f1 = open("day4.txt")

records = [] 
guardNum = 0

for line in f1:
    dateSplit = line.strip().split("-")
    month = int(dateSplit[1])
    daySplit = dateSplit[2].split()
    day = int(daySplit[0])
    timeSplit = daySplit[1].split(':')
    hour = int(timeSplit[0])
    minute = int(timeSplit[1][0 : 2])
    message = daySplit[2]
    print(message)
    if message == 'Guard':
        guardNum = daySplit[3]
        print(guardNum)

# To Do
# sort dates in chronological order (list of enteries)
# iterate through list and add sleep to guard
# create dict for each guard and tally each minute that they are asleep
# dictorary (key=guard number, value=minutes asleep pairs)
# find guard with most minutes slept
# find minute that is most asleep
# multiply two prev numbers




#Part 2 Solution
