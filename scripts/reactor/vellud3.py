import time, random

golluxPenny = 4310098 #Gollux Penny
golluxCoin = 4310097 #Gollux Coin
crackedBelt = 1132243 #Cracked Engraved Gollux Belt
crackedPendant = 1122264 #Cracked Engraved Gollux Pendant
solidBelt = 1132244 #Solid Engraved Gollux Belt
solidPendant = 1122265 #Solid Engraved Gollux Pendant
reinforcedBelt = 1132245 #Reinforced Engraved Gollux Belt
reinforcedPendant = 1122266 #Reinforced Engraved Gollux Pendant
superiorBelt = 1132246 #Superior Engraved Gollux Belt
superiorPendant = 1122267 #Superior Engraved Gollux Pendant
powerElixir = 2000005 #Power Elixir

items = []

#3 Power Elixer drops with random quantities between 1-4
items.append(int(str(powerElixir)+str(random.randint(1,4))))
items.append(int(str(powerElixir)+str(random.randint(1,4))))
items.append(int(str(powerElixir)+str(random.randint(1,4))))

#5 Power Elixir drops with random quantities between 1-5
items.append(int(str(golluxPenny) + str(random.randint(1,5))))
items.append(int(str(golluxPenny) + str(random.randint(1,5))))
items.append(int(str(golluxPenny) + str(random.randint(1,5))))
items.append(int(str(golluxPenny) + str(random.randint(1,5))))
items.append(int(str(golluxPenny) + str(random.randint(1,5))))


#1 singular Gollux Coin drop and 1 with a random quantity between 19-39
items.append(int(str(golluxCoin) + str(1)))
items.append(int(str(golluxCoin) + str(random.randint(19,39))))




if random.randint(0,100) < 10:
    items.append(int(str(crackedBelt) + str(1)))
if random.randint(0,100) < 5:
    items.append(int(str(crackedBelt) + str(1)))

if random.randint(0,100) < 10:
    items.append(int(str(crackedPendant) + str(1)))
if random.randint(0,100) < 5:
    items.append(int(str(crackedPendant) + str(1)))


if random.randint(0,100) < 10:
    items.append(int(str(solidBelt) + str(1)))
if random.randint(0,100) < 5:
    items.append(int(str(solidBelt) + str(1)))

if random.randint(0,100) < 10:
    items.append(int(str(solidPendant) + str(1)))
if random.randint(0,100) < 5:
    items.append(int(str(solidPendant) + str(1)))


if random.randint(0,100) < 15:
    items.append(int(str(reinforcedBelt) + str(1)))
if random.randint(0,100) < 5:
    items.append(int(str(reinforcedBelt) + str(1)))

if random.randint(0,100) < 15:
    items.append(int(str(reinforcedPendant) + str(1)))
if random.randint(0,100) < 5:
    items.append(int(str(reinforcedPendant) + str(1)))


if random.randint(0,100) < 20:
    items.append(int(str(superiorBelt) + str(1)))
if random.randint(0,100) < 5:
    items.append(int(str(superiorBelt) + str(1)))

if random.randint(0,100) < 25:
    items.append(int(str(superiorPendant) + str(1)))
if random.randint(0,100) < 5:
    items.append(int(str(superiorPendant) + str(1)))


random.shuffle(items)


if reactor.getHitCount() == 0:
    reactor.incHitCount()
    
    sm.removeReactor()
    time.sleep(.75)
    sm.spawnReactorInState(8630004, 95, 67, 1)
    chr.getField().dropItemsAlongLine(items, 115, 95, 75, 125)
    sm.dispose()