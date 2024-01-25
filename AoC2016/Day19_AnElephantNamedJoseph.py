# Part 1 Solution
f1 = open("day19.txt")

for line in f1:
    numberOfElves = int(line.strip())

elvesWithGifts = []
winGift = True 

for i in range(numberOfElves): 
    elfNum = i + 1
    if elfNum % 2 != 0:
        elvesWithGifts.append(elfNum)

if numberOfElves % 2 != 0: 
    winGift = False 

while len(elvesWithGifts) > 1: 
    newRoundElvesWithGifts = []

    for val in elvesWithGifts: 
        if winGift == True: 
            newRoundElvesWithGifts.append(val)
        
        winGift = not winGift
    
    elvesWithGifts = newRoundElvesWithGifts[:]

print(elvesWithGifts[0])

# Part 2 Solution
f1 = open("day19.txt")

for line in f1:
    numberOfElves = int(line.strip())

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

dummy = ListNode()
curNode = dummy 

for i in range(1, numberOfElves + 1):
    nextNode = ListNode(i)
    curNode.next = nextNode
    curNode = nextNode 

startNode = (numberOfElves // 2) + 1
prevNode = dummy 
curNode = dummy 

while curNode.val != startNode:
    prevNode = curNode
    curNode = curNode.next

while numberOfElves != 1:
    if curNode.next:
        prevNode.next = curNode.next 
        curNode = curNode.next
    else:
        prevNode.next = None 
        prevNode = dummy 
        curNode = dummy.next  
    
    numberOfElves -= 1

    if numberOfElves % 2 == 0:
        prevNode = curNode 
        curNode = curNode.next 

    if not curNode: 
        prevNode = dummy
        curNode = dummy.next

print(dummy.next.val) 