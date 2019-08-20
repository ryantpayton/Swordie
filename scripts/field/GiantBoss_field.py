sm.addCurrentGolluxMap()
if not sm.hasMobsInField():
    sm.openGolluxPortal()
else:
    while sm.hasMobsInField():
        sm.waitForMobDeath()
    sm.addClearedGolluxMap()
    sm.openGolluxPortal("open", 1)
    sm.openGolluxPortal("clear", 1)