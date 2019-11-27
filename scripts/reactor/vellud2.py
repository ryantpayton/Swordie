import time, random

golP = 4310098 #Gollux Penny
golC = 4310097 #Gollux Coin
crackB = 1132243 #Cracked Engraved Gollux Belt
crackP = 1122264 #Cracked Engraved Gollux Pendant
solidB = 1132244 #Solid Engraved Gollux Belt
solidP = 1122265 #Solid Engraved Gollux Pendant
reinB = 1132245 #Reinforced Engraved Gollux Belt
reinP = 1122266 #Reinforced Engraved Gollux Pendant
pE = 2000005 #Power Elixer

items = []


pe1 = int(str(pE)+str(random.randint(1,4)))
items.append(pe1)
pe2 = int(str(pE)+str(random.randint(1,4)))
items.append(pe2)
pe3 = int(str(pE)+str(random.randint(1,4)))
items.append(pe3)


t2 = int(str(golP) + str(1))
items.append(t2)
gp1 = int(str(golP) + str(random.randint(1,5)))
items.append(gp1)
gp2 = int(str(golP) + str(random.randint(1,5)))
items.append(gp2)
gp3 = int(str(golP) + str(random.randint(1,5)))
items.append(gp3)
gp4 = int(str(golP) + str(random.randint(1,5)))
items.append(gp4)



gc1 = int(str(golC) + str(random.randint(10,19)))
items.append(gc1)
gc2 = int(str(golC) + str(1))
items.append(gc2)



if random.randint(1,100) <= 10:
    t5 = int(str(crackB) + str(1))
    items.append(t5)
if random.randint(1,100) <= 5:
    t6 = int(str(crackB) + str(1))
    items.append(t6)

if random.randint(1,100) <= 10:
    t7 = int(str(crackP) + str(1))
    items.append(t7)
if random.randint(1,100) <= 5:
    t8 = int(str(crackP) + str(1))
    items.append(t8)


if random.randint(1,100) <= 15:
    t9 = int(str(solidB) + str(1))
    items.append(t9)
if random.randint(1,100) <= 5:
    t10 = int(str(solidB) + str(1))
    items.append(t10)

if random.randint(1,100) <= 15:
    t11 = int(str(solidP) + str(1))
    items.append(t11)
if random.randint(1,100) <= 5:
    t12 = int(str(solidP) + str(1))
    items.append(t12)


if random.randint(1,100) <= 20:
    t13 = int(str(reinB) + str(1))
    items.append(t13)
if random.randint(1,100) <= 15:
    t14 = int(str(reinB) + str(1))
    items.append(t14)

if random.randint(1,100) <= 30:
    t15 = int(str(reinP) + str(1))
    items.append(t15)
if random.randint(1,100) <= 15:
    t16 = int(str(reinP) + str(1))
    items.append(t16)



random.shuffle(items)


if reactor.getHitCount() == 0:
    reactor.incHitCount()
    
    sm.removeReactor()
    time.sleep(.75)
    sm.spawnReactorInState(8630004, 95, 67, 1)
    sm.dropItemsAlongLine(items, 115, 95, 75, 125, True)
    sm.dispose()