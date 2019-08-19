rightShoulderID=9390610;
if not sm.golluxMapAlreadyVisited():
    sm.spawnMob(rightShoulderID)
if not sm.hasMobsInField():
    sm.openGolluxPortal()
sm.addCurrentGolluxMap()
sm.waitForMobDeath(rightShoulderID)
sm.addClearedGolluxMap()
sm.openGolluxPortal()