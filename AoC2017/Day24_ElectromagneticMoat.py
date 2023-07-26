# Part 1 Solution (takes about 10 seconds to run)
f1 = open("day24.txt")

portToComponent = dict() 
strongestBridge = 0 

for line in f1: 
    ports = line.strip().split("/")
    port1 = int(ports[0])
    port2 = int(ports[1])

    if port1 not in portToComponent: 
        portToComponent[port1] = [port2]
    else: 
        portToComponent[port1].append(port2)

    if port2 not in portToComponent: 
        portToComponent[port2] = [port1]
    else: 
        portToComponent[port2].append(port1)

# recursive function to find the next port and find the strongest bridge score 
def findStrongestBridgeScore(currentPort, bridge, strongestBridge): 
    bridgeScores = []

    for port in portToComponent[currentPort]: 
        if (port, currentPort) not in bridge and (currentPort, port) not in bridge: 
            newStrength = strongestBridge + port + currentPort
            bridgeScores.append(newStrength)
            strongestBridgeScore = findStrongestBridgeScore(port, bridge + [(port, currentPort)], newStrength)
            bridgeScores.append(strongestBridgeScore)
    
    if len(bridgeScores) == 0: 
        return 0
    return max(bridgeScores)

print(findStrongestBridgeScore(0, [], 0))

# Part 2 Solution (takes about 10 seconds to run)
f1 = open("day24.txt")

portToComponent = dict() 
strongestBridge = 0 

for line in f1: 
    ports = line.strip().split("/")
    port1 = int(ports[0])
    port2 = int(ports[1])

    if port1 not in portToComponent: 
        portToComponent[port1] = [port2]
    else: 
        portToComponent[port1].append(port2)

    if port2 not in portToComponent: 
        portToComponent[port2] = [port1]
    else: 
        portToComponent[port2].append(port1)

# recursive function to find the next port and find the strongest bridge score for the longest bridge
def findLongestBridgeScore(currentPort, bridge, strongestBridge, bridgeLength): 
    bridgeScores = dict()
    maxBridgeScore = 0

    for port in portToComponent[currentPort]: 
        if (port, currentPort) not in bridge and (currentPort, port) not in bridge: 
            newStrength = strongestBridge + port + currentPort

            if bridgeLength not in bridgeScores: 
                bridgeScores[bridgeLength] = [newStrength]
            else: 
                bridgeScores[bridgeLength].append(newStrength)

            strongestBridgeScore, newBridgeLength = findLongestBridgeScore(port, bridge + [(port, currentPort)], newStrength, len(bridge) + 1)
            
            if newBridgeLength not in bridgeScores: 
                bridgeScores[newBridgeLength] = [strongestBridgeScore]
            else: 
                bridgeScores[newBridgeLength].append(strongestBridgeScore)

    if len(bridgeScores) == 0:
        return maxBridgeScore, 0
    
    for i in bridgeScores[max(bridgeScores.keys())]: 
        if i > maxBridgeScore: 
            maxBridgeScore = i

    return maxBridgeScore, max(bridgeScores.keys())

print(findLongestBridgeScore(0, [], 0, 0)[0])