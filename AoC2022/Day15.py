# Part 1 Solution
f1 = open("day15.txt")

sensorsManhattanDistance = dict()
notBeacons = set()
lineCount = 0

for line in f1:
    line = line.strip().split(" ")

    sensorX = line[2].strip(",").split('=')
    sensorX = int(sensorX[1])
    sensorY = line[3].strip(":").split('=')
    sensorY = int(sensorY[1])
    
    beaconX = line[8].strip(",").split('=')
    beaconX = int(beaconX[1])
    beaconY = line[9].split('=')
    beaconY = int(beaconY[1])

    sensorsManhattanDistance[(sensorX, sensorY)] = abs(sensorX - beaconX) + abs(sensorY - beaconY)

for sensor in sensorsManhattanDistance: 
    for j in range(sensorsManhattanDistance[sensor]): 
        print(sensorsManhattanDistance[sensor], j, sensor)
        notBeacons.add((sensor[0] + j, sensor[1] - sensorsManhattanDistance[sensor] + j))
        notBeacons.add((sensor[0] - j, sensor[1] + sensorsManhattanDistance[sensor] - j))
        notBeacons.add((sensor[0] - sensorsManhattanDistance[sensor] + j, sensor[1] - j))
        notBeacons.add((sensor[0] + sensorsManhattanDistance[sensor] - j, sensor[1] + j))
        print(notBeacons)
for i in notBeacons: 
    if i[1] == 10: 
        lineCount += 1

print(lineCount)
