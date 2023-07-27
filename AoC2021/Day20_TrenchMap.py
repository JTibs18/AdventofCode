# Part 1 Solution 
import copy 

f1 = open("day20.txt")

imageEnhancementAlgorithm = []
image = dict()
yLength = 0 
xLength = 0 
minXLength = 0
minYLength = 0 
litPixels = 0
imageEnhancementIterationCount = 2 
parseIEA = True 
inverted = False 

for line in f1: 
    if parseIEA == True: 
        imageEnhancementAlgorithm = list(line.strip())
        parseIEA = False 
    elif line != "\n":
        for indx, val in enumerate(line.strip()):
            image[(indx, yLength)] = val 
        
        yLength += 1 
        xLength = len(line)

def findBinary(pixel, image, inverted):
    if (pixel not in image and inverted == False):
        return "0"
    elif pixel not in image: 
        return "1"
    elif image[pixel] == "." : 
        return "0"
    return "1"

while imageEnhancementIterationCount: 
    newImage = dict()

    for x in range(minXLength - 2, xLength + 2): 
        for y in range(minYLength - 2, yLength + 2): 
            binaryNumber = ""

            binaryNumber += findBinary((x - 1, y - 1), image, inverted)
            binaryNumber += findBinary((x, y - 1), image, inverted)
            binaryNumber += findBinary((x + 1, y - 1), image, inverted)
            binaryNumber += findBinary((x - 1, y), image, inverted)
            binaryNumber += findBinary((x, y), image, inverted)
            binaryNumber += findBinary((x + 1, y), image, inverted)
            binaryNumber += findBinary((x - 1, y + 1), image, inverted)
            binaryNumber += findBinary((x, y + 1), image, inverted)
            binaryNumber += findBinary((x + 1, y + 1), image, inverted)

            indexToFind = int(binaryNumber, 2)
            newImage[(x, y)] = imageEnhancementAlgorithm[indexToFind]
    
    image = copy.deepcopy(newImage)
    minXLength -= 1
    minYLength -= 1
    xLength += 1
    yLength += 1
    imageEnhancementIterationCount -= 1 
    inverted = not inverted 

for pixels in image.values(): 
    if pixels == "#": 
        litPixels += 1 

print(litPixels)

# Part 2 Solution (takes about 20 seconds to run)
import copy 

f1 = open("day20.txt")

imageEnhancementAlgorithm = []
image = dict()
yLength = 0 
xLength = 0 
minXLength = 0
minYLength = 0 
litPixels = 0
imageEnhancementIterationCount = 50
parseIEA = True 
inverted = False 

for line in f1: 
    if parseIEA == True: 
        imageEnhancementAlgorithm = list(line.strip())
        parseIEA = False 
    elif line != "\n":
        for indx, val in enumerate(line.strip()):
            image[(indx, yLength)] = val 
        
        yLength += 1 
        xLength = len(line)

def findBinary(pixel, image, inverted):
    if (pixel not in image and inverted == False):
        return "0"
    elif pixel not in image: 
        return "1"
    elif image[pixel] == "." : 
        return "0"
    return "1"

while imageEnhancementIterationCount: 
    newImage = dict()

    for x in range(minXLength - 2, xLength + 2): 
        for y in range(minYLength - 2, yLength + 2): 
            binaryNumber = ""

            binaryNumber += findBinary((x - 1, y - 1), image, inverted)
            binaryNumber += findBinary((x, y - 1), image, inverted)
            binaryNumber += findBinary((x + 1, y - 1), image, inverted)
            binaryNumber += findBinary((x - 1, y), image, inverted)
            binaryNumber += findBinary((x, y), image, inverted)
            binaryNumber += findBinary((x + 1, y), image, inverted)
            binaryNumber += findBinary((x - 1, y + 1), image, inverted)
            binaryNumber += findBinary((x, y + 1), image, inverted)
            binaryNumber += findBinary((x + 1, y + 1), image, inverted)

            indexToFind = int(binaryNumber, 2)
            newImage[(x, y)] = imageEnhancementAlgorithm[indexToFind]
    
    image = copy.deepcopy(newImage)
    minXLength -= 1
    minYLength -= 1
    xLength += 1
    yLength += 1
    imageEnhancementIterationCount -= 1 
    inverted = not inverted 

for pixels in image.values(): 
    if pixels == "#": 
        litPixels += 1 

print(litPixels)
