#Part 1 Solution
import itertools
f1 = open("day21.txt")

lowestCost = 1000
bossStats = dict()
weapons = [
    {
        "name": "Dagger", 
        "cost": 8, 
        "damage": 4, 
        "armor": 0
    }, 
    {
        "name": "Shortsword", 
        "cost": 10, 
        "damage": 5, 
        "armor": 0
    }, 
    {
        "name": "Warhammer", 
        "cost": 25, 
        "damage": 6, 
        "armor": 0
    }, 
    {
        "name": "Longsword", 
        "cost": 40, 
        "damage": 7, 
        "armor": 0
    }, 
    {
        "name": "Greataxe", 
        "cost": 74, 
        "damage": 8, 
        "armor": 0
    }, 
]

armor = [
    {
        "name": "Leather", 
        "cost": 13, 
        "damage": 0, 
        "armor": 1
    }, 
    {
        "name": "Chainmail", 
        "cost": 31, 
        "damage": 0, 
        "armor": 2
    }, 
    {
        "name": "Splintmail", 
        "cost": 53, 
        "damage": 0, 
        "armor": 3
    }, 
    {
        "name": "Bandedmail", 
        "cost": 75, 
        "damage": 0, 
        "armor": 4
    }, 
    {
        "name": "Platemail", 
        "cost": 102, 
        "damage": 0, 
        "armor": 5
    }, 
]

rings = [
    {
        "name": "Damage +1", 
        "cost": 25, 
        "damage": 1, 
        "armor": 0
    }, 
    {
        "name": "Damage +2", 
        "cost": 50, 
        "damage": 2, 
        "armor": 0
    }, 
    {
        "name": "Damage +3", 
        "cost": 100, 
        "damage": 3, 
        "armor": 0
    }, 
    {
        "name": "Defense +1", 
        "cost": 20, 
        "damage": 0, 
        "armor": 1
    }, 
    {
        "name": "Defense +2", 
        "cost": 40, 
        "damage": 0, 
        "armor": 2
    }, 
    {
        "name": "Defense +3", 
        "cost": 80, 
        "damage": 0, 
        "armor": 3
    }, 
]

for line in f1: 
    data = line.strip().split(": ")
    bossStats[data[0]] = int(data[1])

noRingsProduct = list(itertools.product(*[weapons, armor]))
oneRingProduct = list(itertools.product(*[weapons, armor, rings]))
twoRingsPermutations = list(itertools.permutations(rings, 2)) 
twoRingsProduct = list(itertools.product(*[weapons, armor, twoRingsPermutations]))

for weapon, armor in noRingsProduct: 
    damagePlayer = weapon['damage'] + armor['damage'] - bossStats['Armor']
    damageBoss = bossStats['Damage'] - weapon['armor'] - armor['armor']
    
    if damagePlayer < 1: 
        damagePlayer = 1 

    if damageBoss < 1: 
        damageBoss = 1 

    if damagePlayer >= damageBoss: 
        cost = weapon['cost'] + armor['cost']
        if cost < lowestCost: 
            lowestCost = cost 

for weapon, armor, ring in oneRingProduct: 
    damagePlayer = weapon['damage'] + armor['damage'] + ring['damage'] - bossStats['Armor']
    damageBoss = bossStats['Damage'] - weapon['armor'] - armor['armor'] - ring['armor']
    
    if damagePlayer < 1: 
        damagePlayer = 1 

    if damageBoss < 1: 
        damageBoss = 1 
    
    if damagePlayer >= damageBoss: 
        cost = weapon['cost'] + armor['cost'] + ring['cost']
        if cost < lowestCost: 
            lowestCost = cost 

for weapon, armor, ring in twoRingsProduct: 
    damagePlayer = weapon['damage'] + armor['damage'] + ring[0]['damage'] + ring[1]['damage'] - bossStats['Armor']
    damageBoss = bossStats['Damage'] - weapon['armor'] - armor['armor'] - ring[0]['armor'] - ring[1]['armor']
    
    if damagePlayer < 1: 
        damagePlayer = 1 

    if damageBoss < 1: 
        damageBoss = 1 
    
    if damagePlayer >= damageBoss: 
        cost = weapon['cost'] + armor['cost'] + ring[0]['cost'] + ring[1]['cost'] 
        if cost < lowestCost: 
            lowestCost = cost 
            
print(lowestCost)

#Part 2 Solution
import itertools
f1 = open("day21.txt")

highestCost = 0
bossStats = dict()
weapons = [
    {
        "name": "Dagger", 
        "cost": 8, 
        "damage": 4, 
        "armor": 0
    }, 
    {
        "name": "Shortsword", 
        "cost": 10, 
        "damage": 5, 
        "armor": 0
    }, 
    {
        "name": "Warhammer", 
        "cost": 25, 
        "damage": 6, 
        "armor": 0
    }, 
    {
        "name": "Longsword", 
        "cost": 40, 
        "damage": 7, 
        "armor": 0
    }, 
    {
        "name": "Greataxe", 
        "cost": 74, 
        "damage": 8, 
        "armor": 0
    }, 
]

armor = [
    {
        "name": "Leather", 
        "cost": 13, 
        "damage": 0, 
        "armor": 1
    }, 
    {
        "name": "Chainmail", 
        "cost": 31, 
        "damage": 0, 
        "armor": 2
    }, 
    {
        "name": "Splintmail", 
        "cost": 53, 
        "damage": 0, 
        "armor": 3
    }, 
    {
        "name": "Bandedmail", 
        "cost": 75, 
        "damage": 0, 
        "armor": 4
    }, 
    {
        "name": "Platemail", 
        "cost": 102, 
        "damage": 0, 
        "armor": 5
    }, 
]

rings = [
    {
        "name": "Damage +1", 
        "cost": 25, 
        "damage": 1, 
        "armor": 0
    }, 
    {
        "name": "Damage +2", 
        "cost": 50, 
        "damage": 2, 
        "armor": 0
    }, 
    {
        "name": "Damage +3", 
        "cost": 100, 
        "damage": 3, 
        "armor": 0
    }, 
    {
        "name": "Defense +1", 
        "cost": 20, 
        "damage": 0, 
        "armor": 1
    }, 
    {
        "name": "Defense +2", 
        "cost": 40, 
        "damage": 0, 
        "armor": 2
    }, 
    {
        "name": "Defense +3", 
        "cost": 80, 
        "damage": 0, 
        "armor": 3
    }, 
]

for line in f1: 
    data = line.strip().split(": ")
    bossStats[data[0]] = int(data[1])

noRingsProduct = list(itertools.product(*[weapons, armor]))
oneRingProduct = list(itertools.product(*[weapons, armor, rings]))
oneRingNoArmorProduct = list(itertools.product(*[weapons, rings]))
twoRingsPermutations = list(itertools.permutations(rings, 2)) 
twoRingsProduct = list(itertools.product(*[weapons, armor, twoRingsPermutations]))
twoRingsNoArmorProduct = list(itertools.product(*[weapons, twoRingsPermutations]))

for weapon, armor in noRingsProduct: 
    damagePlayer = weapon['damage'] + armor['damage'] - bossStats['Armor']
    damageBoss = bossStats['Damage'] - weapon['armor'] - armor['armor']
    
    if damagePlayer < 1: 
        damagePlayer = 1 

    if damageBoss < 1: 
        damageBoss = 1 

    if damagePlayer < damageBoss: 
        cost = weapon['cost'] + armor['cost']
        if cost > highestCost: 
            highestCost = cost 

for weapon, armor, ring in oneRingProduct: 
    damagePlayer = weapon['damage'] + armor['damage'] + ring['damage'] - bossStats['Armor']
    damageBoss = bossStats['Damage'] - weapon['armor'] - armor['armor'] - ring['armor']
    
    if damagePlayer < 1: 
        damagePlayer = 1 

    if damageBoss < 1: 
        damageBoss = 1 
    
    if damagePlayer < damageBoss: 
        cost = weapon['cost'] + armor['cost'] + ring['cost']
        if cost > highestCost: 
            highestCost = cost 

for weapon, ring in oneRingNoArmorProduct: 
    damagePlayer = weapon['damage'] + ring['damage'] - bossStats['Armor']
    damageBoss = bossStats['Damage'] - weapon['armor'] - ring['armor'] 
    
    if damagePlayer < 1: 
        damagePlayer = 1 

    if damageBoss < 1: 
        damageBoss = 1 
    
    if damagePlayer < damageBoss: 
        cost = weapon['cost'] + ring['cost'] 
        if cost > highestCost: 
            highestCost = cost  

for weapon, armor, ring in twoRingsProduct: 
    damagePlayer = weapon['damage'] + armor['damage'] + ring[0]['damage'] + ring[1]['damage'] - bossStats['Armor']
    damageBoss = bossStats['Damage'] - weapon['armor'] - armor['armor'] - ring[0]['armor'] - ring[1]['armor']
    
    if damagePlayer < 1: 
        damagePlayer = 1 

    if damageBoss < 1: 
        damageBoss = 1 
    
    if damagePlayer < damageBoss: 
        cost = weapon['cost'] + armor['cost'] + ring[0]['cost'] + ring[1]['cost'] 
        if cost > highestCost: 
            highestCost = cost  

for weapon, ring in twoRingsNoArmorProduct: 
    damagePlayer = weapon['damage'] + ring[0]['damage'] + ring[1]['damage'] - bossStats['Armor']
    damageBoss = bossStats['Damage'] - weapon['armor'] - ring[0]['armor'] - ring[1]['armor']
    
    if damagePlayer < 1: 
        damagePlayer = 1 

    if damageBoss < 1: 
        damageBoss = 1 
    
    if damagePlayer < damageBoss: 
        cost = weapon['cost'] + ring[0]['cost'] + ring[1]['cost'] 
        if cost > highestCost: 
            highestCost = cost  

print(highestCost)