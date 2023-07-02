#Part 1 Solution
f1 = open("day13.txt")

firewallRecord = dict() 
curSecurityScanner = dict() 
scannerDirection = dict() 
severity = 0 
currentLayer = 0 

for line in f1: 
    parsed = line.strip().split(": ")
    firewallRecord[int(parsed[0])] = int(parsed[1])
    curSecurityScanner[int(parsed[0])] = 0 
    scannerDirection[int(parsed[0])] = "plus"

layers = max(firewallRecord.keys()) + 1 

while currentLayer <= layers: 
    if currentLayer in curSecurityScanner and curSecurityScanner[currentLayer] == 0: 
        severity += currentLayer * firewallRecord[currentLayer]
    
    for key, value in firewallRecord.items(): 
        if scannerDirection[key] == "plus": 
            if curSecurityScanner[key] + 1 == value: 
                curSecurityScanner[key] -= 1 
                scannerDirection[key] = "minus"
            else: 
                curSecurityScanner[key] += 1 
        else: 
            if curSecurityScanner[key] - 1 == -1: 
                curSecurityScanner[key] += 1 
                scannerDirection[key] = "plus"
            else: 
                curSecurityScanner[key] -= 1 

    currentLayer += 1 

print(severity)

#Part 2 Solution (takes about five minutes to run)
import copy 
f1 = open("day13.txt")

firewallRecord = dict() 
curSecurityScanner = dict() 
scannerDirection = dict() 
currentLayer = 0 
delay = 0 
delayCount = 0 
securityScannerAtTime = dict() 

for line in f1: 
    parsed = line.strip().split(": ")
    firewallRecord[int(parsed[0])] = int(parsed[1])
    curSecurityScanner[int(parsed[0])] = 0 
    scannerDirection[int(parsed[0])] = "plus"

layers = max(firewallRecord.keys()) + 1 

def simulateScanner(time): 
    for key, value in firewallRecord.items(): 
        if scannerDirection[key] == "plus": 
            if curSecurityScanner[key] + 1 == value: 
                curSecurityScanner[key] -= 1 
                scannerDirection[key] = "minus"
            else: 
                curSecurityScanner[key] += 1 
        else: 
            if curSecurityScanner[key] - 1 == -1: 
                curSecurityScanner[key] += 1 
                scannerDirection[key] = "plus"
            else: 
                curSecurityScanner[key] -= 1 
    
    securityScannerAtTime[time] = copy.deepcopy(curSecurityScanner)

while currentLayer <= layers: 
    if delay + currentLayer not in securityScannerAtTime: 
        simulateScanner(delay + currentLayer)

    if currentLayer in curSecurityScanner and securityScannerAtTime[delay + currentLayer][currentLayer] == 0: 
        delay += 1 
        currentLayer = 0 
    else: 
        currentLayer += 1 
   
print(delay + 1)