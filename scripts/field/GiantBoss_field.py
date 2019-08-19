sm.addCurrentGolluxMap()
if not sm.hasMobsInField():
    sm.openGolluxPortal()
else:
    while sm.hasMobsInField():
        sm.waitForMobDeath()
    sm.addClearedGolluxMap()
    sm.openGolluxPortal()