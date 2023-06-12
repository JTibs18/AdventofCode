#Part 1 Solution
f1 = open("day20.txt")

particles = []
closestParticleValue = 1000000000
closestParticle = ""

for line in f1: 
    splitLine = line.strip().split(", ")
    
    position = splitLine[0].strip("p=<>").split(",")
    for indx, val in enumerate(position):
        position[indx] = int(val)
    
    velocity = splitLine[1].strip("v=<>").split(",")
    for indx, val in enumerate(velocity):
        velocity[indx] = int(val)

    acceleration = splitLine[2].strip("a=<>").split(",")
    for indx, val in enumerate(acceleration): 
        acceleration[indx] = int(val)

    particles.append([position, velocity, acceleration])

for i in range(1000):
    for indx, p in enumerate(particles): 
        particles[indx][1][0] += particles[indx][2][0]
        particles[indx][1][1] += particles[indx][2][1]
        particles[indx][1][2] += particles[indx][2][2]
        particles[indx][0][0] += particles[indx][1][0]
        particles[indx][0][1] += particles[indx][1][1]
        particles[indx][0][2] += particles[indx][1][2]
    
for indx, p in enumerate(particles): 
    if abs(particles[indx][0][0]) + abs(particles[indx][0][1]) + abs(particles[indx][0][2]) < closestParticleValue: 
        closestParticleValue = abs(particles[indx][0][0]) + abs(particles[indx][0][1]) + abs(particles[indx][0][2])
        closestParticle = indx 

print(closestParticle)

#Part 2 Solution
import copy 
f1 = open("day20.txt")

particles = []

for line in f1: 
    splitLine = line.strip().split(", ")
    
    position = splitLine[0].strip("p=<>").split(",")
    for indx, val in enumerate(position):
        position[indx] = int(val)
    
    velocity = splitLine[1].strip("v=<>").split(",")
    for indx, val in enumerate(velocity):
        velocity[indx] = int(val)

    acceleration = splitLine[2].strip("a=<>").split(",")
    for indx, val in enumerate(acceleration): 
        acceleration[indx] = int(val)

    particles.append([position, velocity, acceleration])

for i in range(1000):
    removePositions = dict()

    for indx, p in enumerate(particles): 
        particles[indx][1][0] += particles[indx][2][0]
        particles[indx][1][1] += particles[indx][2][1]
        particles[indx][1][2] += particles[indx][2][2]
        particles[indx][0][0] += particles[indx][1][0]
        particles[indx][0][1] += particles[indx][1][1]
        particles[indx][0][2] += particles[indx][1][2]
    
        pos = (particles[indx][0][0], particles[indx][0][1], particles[indx][0][2])

        if pos in removePositions: 
            removePositions[pos] += 1
        else: 
            removePositions[pos] = 1  

    tempParticles = []

    for p in particles: 
        pos = (p[0][0], p[0][1], p[0][2])

        if removePositions[pos] == 1: 
            tempParticles.append(p)

    particles = copy.deepcopy(tempParticles)
    
print(len(particles))
    