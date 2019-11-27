fieldID = sm.getFieldID()

sm.addCurrentGolluxMap()
if sm.getInstancedMapMobCount(fieldID) == 3:
    if fieldID == 863010310 or fieldID == 863010410:
        sm.openGolluxPortal("open", 1)
        sm.openGolluxPortal("clear", 1)
else:
    while sm.getInstancedMapMobCount(fieldID) >= 3:
        sm.waitForMobDeath()
        sm.chatScript("There are " + str(sm.getInstancedMapMobCount(fieldID) -3) + " doses of evil energy remaining in this area.")
        if sm.getInstancedMapMobCount(fieldID) == 3:
            sm.addClearedGolluxMap()
            #GMS-like field effect
            #sm.showFieldEffect("Map/EffectTW.img/arisan/clear")
            #Much nicer/smaller profile for clearing side/monster maps
            sm.showFieldEffect("Map/Effect.img/monsterPark/clear")
            if fieldID == 863010310 or fieldID == 863010410:
                sm.openGolluxPortal("open", 1)
                sm.openGolluxPortal("clear", 1)
