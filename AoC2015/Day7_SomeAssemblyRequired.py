#Part 1 Solution
f1 = open("day7.txt")

circuit = dict() 

# parsing input 
for line in f1: 
    line = line.rstrip()
    splitLine = line.split(" -> ")

    if splitLine[0].isnumeric():
        circuit[splitLine[1]] = int(splitLine[0])
    else: 
        signal = splitLine[0].split(" ")
        instruction = []
        for i in signal: 
            if i.isnumeric(): 
                instruction.append(int(i))
            else: 
                instruction.append(i)
        circuit[splitLine[1]] = instruction

# recursive part that solves logical operators 
def calculateSignal(signal): 
    if len(signal) == 1: 
        return getWireSignal(signal[0])

    if "AND" == signal[1]:
        if isinstance(signal[0], int) == False and isinstance(signal[2], int) == False: 
            return getWireSignal(signal[0]) & getWireSignal(signal[2])
        elif isinstance(signal[0], int) == False and isinstance(signal[2], int): 
            return getWireSignal(signal[0]) & signal[2] 
        elif isinstance(signal[0], int) and isinstance(signal[2], int) == False: 
            return signal[0] & getWireSignal(signal[2])  
        else: 
            return signal[0] & signal[2]
    elif "OR" == signal[1]:
        if isinstance(signal[0], int) == False and isinstance(signal[2], int) == False: 
            return getWireSignal(signal[0]) | getWireSignal(signal[2])
        elif isinstance(signal[0], int) == False and isinstance(signal[2], int): 
            return getWireSignal(signal[0]) | signal[2] 
        elif isinstance(signal[0], int) and isinstance(signal[2], int) == False: 
            return signal[0] | getWireSignal(signal[2])  
        else: 
            return signal[0] | signal[2]
    elif "LSHIFT" == signal[1]:
        if isinstance(signal[0], int) == False and isinstance(signal[2], int) == False: 
            return getWireSignal(signal[0]) << getWireSignal(signal[2])
        elif isinstance(signal[0], int) == False and isinstance(signal[2], int): 
            return getWireSignal(signal[0]) << signal[2] 
        elif isinstance(signal[0], int) and isinstance(signal[2], int) == False: 
            return signal[0] << getWireSignal(signal[2])  
        else: 
            return signal[0] << signal[2]
    elif "RSHIFT" == signal[1]:
        if isinstance(signal[0], int) == False and isinstance(signal[2], int) == False: 
            return getWireSignal(signal[0]) >> getWireSignal(signal[2])
        elif isinstance(signal[0], int) == False and isinstance(signal[2], int): 
            return getWireSignal(signal[0]) >> signal[2] 
        elif isinstance(signal[0], int) and isinstance(signal[2], int) == False: 
            return signal[0] >> getWireSignal(signal[2])  
        else: 
            return signal[0] >> signal[2]
    else:
        if isinstance(signal[1], int) == False: 
            return ~getWireSignal(signal[1]) & 65535
        else: 
            return ~signal[1] & 65535

# recursive controller with base case and recursive case       
def getWireSignal(wire):
    if isinstance(circuit[wire], int):
        return circuit[wire]
    else: 
        circuit[wire] = calculateSignal(circuit[wire])
        return circuit[wire]
    
print(getWireSignal("a"))

#Part 2 Solution
import copy
f1 = open("day7.txt")

circuit = dict() 

# parsing input 
for line in f1: 
    line = line.rstrip()
    splitLine = line.split(" -> ")

    if splitLine[0].isnumeric():
        circuit[splitLine[1]] = int(splitLine[0])
    else: 
        signal = splitLine[0].split(" ")
        instruction = []
        for i in signal: 
            if i.isnumeric(): 
                instruction.append(int(i))
            else: 
                instruction.append(i)
        circuit[splitLine[1]] = instruction

originalCircuit = copy.deepcopy(circuit)

# recursive part that solves logical operators 
def calculateSignal(signal): 
    if len(signal) == 1: 
        return getWireSignal(signal[0])

    if "AND" == signal[1]:
        if isinstance(signal[0], int) == False and isinstance(signal[2], int) == False: 
            return getWireSignal(signal[0]) & getWireSignal(signal[2])
        elif isinstance(signal[0], int) == False and isinstance(signal[2], int): 
            return getWireSignal(signal[0]) & signal[2] 
        elif isinstance(signal[0], int) and isinstance(signal[2], int) == False: 
            return signal[0] & getWireSignal(signal[2])  
        else: 
            return signal[0] & signal[2]
    elif "OR" == signal[1]:
        if isinstance(signal[0], int) == False and isinstance(signal[2], int) == False: 
            return getWireSignal(signal[0]) | getWireSignal(signal[2])
        elif isinstance(signal[0], int) == False and isinstance(signal[2], int): 
            return getWireSignal(signal[0]) | signal[2] 
        elif isinstance(signal[0], int) and isinstance(signal[2], int) == False: 
            return signal[0] | getWireSignal(signal[2])  
        else: 
            return signal[0] | signal[2]
    elif "LSHIFT" == signal[1]:
        if isinstance(signal[0], int) == False and isinstance(signal[2], int) == False: 
            return getWireSignal(signal[0]) << getWireSignal(signal[2])
        elif isinstance(signal[0], int) == False and isinstance(signal[2], int): 
            return getWireSignal(signal[0]) << signal[2] 
        elif isinstance(signal[0], int) and isinstance(signal[2], int) == False: 
            return signal[0] << getWireSignal(signal[2])  
        else: 
            return signal[0] << signal[2]
    elif "RSHIFT" == signal[1]:
        if isinstance(signal[0], int) == False and isinstance(signal[2], int) == False: 
            return getWireSignal(signal[0]) >> getWireSignal(signal[2])
        elif isinstance(signal[0], int) == False and isinstance(signal[2], int): 
            return getWireSignal(signal[0]) >> signal[2] 
        elif isinstance(signal[0], int) and isinstance(signal[2], int) == False: 
            return signal[0] >> getWireSignal(signal[2])  
        else: 
            return signal[0] >> signal[2]
    else:
        if isinstance(signal[1], int) == False: 
            return ~getWireSignal(signal[1]) & 65535
        else: 
            return ~signal[1] & 65535

# recursive controller with base case and recursive case               
def getWireSignal(wire):
    if isinstance(circuit[wire], int):
        return circuit[wire]
    else: 
        circuit[wire] = calculateSignal(circuit[wire])
        return circuit[wire]

# override wire b to the value of wire a 
wireB = getWireSignal("a")

# resetting all wires but b 
circuit = copy.deepcopy(originalCircuit)
circuit["b"] = wireB

# finding new signal in a 
print(getWireSignal("a"))