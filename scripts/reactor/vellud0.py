import time, random

golP = 4310098 #Gollux Penny
golC = 4310097 #Gollux Coin
crackB = 1132243 #Cracked Engraved Gollux Belt
crackP = 1122264 #Cracked Engraved Gollux Pendant
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
items.append(t2)
items.append(t2)

gp1 = int(str(golP) + str(random.randint(1,3)))
items.append(gp1)
gp2 = int(str(golP) + str(random.randint(1,3)))
items.append(gp2)




gc1 = int(str(golC) + str(random.randint(1,4)))
items.append(gc1)
gc2 = int(str(golC) + str(1))
items.append(gc2)



if random.randint(1,100) <= 35:
    t5 = int(str(crackB) + str(1))
    items.append(t5)
if random.randint(1,100) <= 5:
    t6 = int(str(crackB) + str(1))
    items.append(t6)

if random.randint(1,100) <= 45:
    t7 = int(str(crackP) + str(1))
    items.append(t7)
if random.randint(1,100) <= 5:
    t8 = int(str(crackP) + str(1))
    items.append(t8)


random.shuffle(items)


if reactor.getHitCount() == 0:
    reactor.incHitCount()
    
    sm.removeReactor()
    time.sleep(.75)
    sm.spawnReactorInState(8630004, 95, 67, 1)
    sm.dropItemsAlongLine(items, 115, 95, 75, 125, True)
    sm.dispose()