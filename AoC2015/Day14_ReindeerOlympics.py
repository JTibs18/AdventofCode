# Part 1 Solution
f1 = open("day14.txt")

distances = [] 
givenTime = 2503 

for line in f1: 
    reindeerData = line.strip().split(' ')
    flyTime = int(reindeerData[6])
    restTime = int(reindeerData[13])
    traveledDistance = int(reindeerData[3])

    oneIntervalTime = flyTime + restTime 
    reindeerDistance = ((givenTime // oneIntervalTime) * traveledDistance * flyTime) 

    if givenTime % oneIntervalTime >= flyTime: 
        reindeerDistance += flyTime * traveledDistance
    else: 
        reindeerDistance += (givenTime % oneIntervalTime) * traveledDistance
    
    distances.append(reindeerDistance)

print(max(distances))

# Part 2 Solution
f1 = open("day14.txt")

givenTime = 2503 
allReindeerData = dict() 
reindeerSimulationData = dict()
maxPoints = 0

for line in f1: 
    reindeerData = line.strip().split(' ')
    
    reindeerName = reindeerData[0]
    flyTime = int(reindeerData[6])
    restTime = int(reindeerData[13])
    traveledDistance = int(reindeerData[3])

    allReindeerData[reindeerName] = {"flyTime": flyTime, "restTime": restTime, "traveledDistance": traveledDistance}
    reindeerSimulationData[reindeerName] = {"flying": True, "time": 0, "points": 0, "distance": 0}

while givenTime: 
    for reindeer in allReindeerData.keys():
        if (reindeerSimulationData[reindeer]["flying"] == True and reindeerSimulationData[reindeer]["time"] < allReindeerData[reindeer]["flyTime"]) or (reindeerSimulationData[reindeer]["flying"] == False and reindeerSimulationData[reindeer]["time"] < allReindeerData[reindeer]["restTime"]):
            reindeerSimulationData[reindeer]["time"] += 1 
        else: 
            reindeerSimulationData[reindeer]["time"] = 1 
            reindeerSimulationData[reindeer]["flying"] = not reindeerSimulationData[reindeer]["flying"]
        
        if reindeerSimulationData[reindeer]["flying"] == True: 
            reindeerSimulationData[reindeer]["distance"] += allReindeerData[reindeer]["traveledDistance"] 

    maxDistance = 0
    maxDistanceReindeerNames = []

    for reindeer in reindeerSimulationData.keys(): 
        if reindeerSimulationData[reindeer]["distance"] > maxDistance: 
            maxDistance = reindeerSimulationData[reindeer]["distance"]
            maxDistanceReindeerNames = [reindeer]
        elif reindeerSimulationData[reindeer]["distance"] == maxDistance:
            maxDistanceReindeerNames.append(reindeer)

    for name in maxDistanceReindeerNames:
        reindeerSimulationData[name]["points"] += 1     

    givenTime -= 1 

for i in reindeerSimulationData.keys():
    if reindeerSimulationData[i]["points"] > maxPoints:
        maxPoints = reindeerSimulationData[i]["points"]

print(maxPoints)