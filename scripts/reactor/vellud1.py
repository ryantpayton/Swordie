import time, random

golluxPenny = 4310098 #Gollux Penny
golluxCoin = 4310097 #Gollux Coin
crackedBelt = 1132243 #Cracked Engraved Gollux Belt
crackedPendant = 1122264 #Cracked Engraved Gollux Pendant
solidBelt = 1132244 #Solid Engraved Gollux Belt
solidPendant = 1122265 #Solid Engraved Gollux Pendant
powerElixir = 2000005 #Power Elixir

items = []

#3 Power Elixir drops with random quantities between 1-4
items.append(int(str(powerElixir)+str(random.randint(1,4))))
items.append(int(str(powerElixir)+str(random.randint(1,4))))
items.append(int(str(powerElixir)+str(random.randint(1,4))))

#2 singular Gollux Penny drops and 3 with random quantities between 1-5
items.append(int(str(golluxPenny) + str(1)))
items.append(int(str(golluxPenny) + str(1)))
items.append(int(str(golluxPenny) + str(random.randint(1,4))))
items.append(int(str(golluxPenny) + str(random.randint(1,4))))
items.append(int(str(golluxPenny) + str(random.randint(1,4))))


#1 singular Gollux Coin drop and 1 with a random quantity between 5-10
items.append(int(str(golluxCoin) + str(1)))
items.append(int(str(golluxCoin) + str(random.randint(5,10))))



if random.randint(0,100) < 15:
    items.append(int(str(crackedBelt) + str(1)))
if random.randint(0,100) < 5:
    items.append(int(str(crackedBelt) + str(1)))

if random.randint(0,100) < 15:
    items.append(int(str(crackedPendant) + str(1)))
if random.randint(0,100) < 5:
    items.append(int(str(crackedPendant) + str(1)))


if random.randint(0,100) < 20:
    items.append(int(str(solidBelt) + str(1)))
if random.randint(0,100) < 10:
    items.append(int(str(solidBelt) + str(1)))

if random.randint(0,100) < 30:
    items.append(int(str(solidPendant) + str(1)))
if random.randint(0,100) < 10:
    items.append(int(str(solidPendant) + str(1)))



random.shuffle(items)


if reactor.getHitCount() == 0:
    reactor.incHitCount()
    
    sm.removeReactor()
    time.sleep(.75)
    sm.spawnReactorInState(8630004, 95, 67, 1)
    chr.getField().dropItemsAlongLine(items, 115, 95, 75, 125)