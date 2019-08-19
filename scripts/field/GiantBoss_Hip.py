abdomenID=9390612;
if not sm.golluxMapAlreadyVisited():
    sm.spawnMob(abdomenID)
if not sm.hasMobsInField():
    sm.openGolluxPortal()
sm.addCurrentGolluxMap()
sm.waitForMobDeath(abdomenID)
sm.addClearedGolluxMap()
sm.openGolluxPortal()