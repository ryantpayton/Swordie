leftShoulderID=9390611;
if not sm.golluxMapAlreadyVisited():
    sm.spawnMob(leftShoulderID)
if not sm.hasMobsInField():
    sm.openGolluxPortal()
sm.addCurrentGolluxMap()
sm.waitForMobDeath(leftShoulderID)
sm.addClearedGolluxMap()
sm.openGolluxPortal()