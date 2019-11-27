import time
#from net.swordie.ms.constants import WzConstants
firstPhaseHeadID = 9390600
secondPhaseHeadID = 9390601
thirdPhaseHeadID = 9390602
golluxMobID = 9390622
#This Mob in particular needs to be turned around, I am not sure of the means to do so.
secondGolluxMobID = 9390623
sm.blockGolluxAttacks()
if sm.golluxMapAlreadyVisited() is not True:
    sm.spawnGollux(0)
    sm.addCurrentGolluxMap()
    sm.spawnMobRespawnable(golluxMobID, -850, 0, True, 1, 10)
    sm.spawnMobRespawnable(secondGolluxMobID, 850, 0, True, 1, 10)
elif sm.hasMobById(secondPhaseHeadID):
    sm.changeFootHold("phase2-1", True)
    sm.changeFootHold("phase2-2", True)
elif sm.hasMobById(thirdPhaseHeadID):
    sm.changeFootHold("phase2-1", True)
    sm.changeFootHold("phase2-2", True)
    sm.changeFootHold("phase3", True)
if sm.hasMobById(firstPhaseHeadID):
    sm.waitForMobDeath(firstPhaseHeadID)
    sm.changeFootHold("phase2-1", True)
    sm.changeFootHold("phase2-2", True)
    sm.spawnGollux(1)
if sm.hasMobById(secondPhaseHeadID):
    sm.waitForMobDeath(secondPhaseHeadID)
    sm.changeFootHold("phase3", True)
    sm.spawnGollux(2)
    #Timer Gauge defaults to Von-Bon, thus always displaying his message instead of Gollux's
    sm.createTimerGauge(100)
    #This triggers regardless of if they are in the room, we need a more effective timing system
    #sm.invokeAfterDelay(100000, "warpInstanceOut", 863010000)
if sm.hasMobById(thirdPhaseHeadID):
    sm.waitForMobDeath(thirdPhaseHeadID)
    sm.showFieldEffect("Map/EffectTW.img/arisan/clear")
    time.sleep(2.5)
    sm.sendGolluxRewardMap(sm.getGolluxDifficulty().getVal())
    sm.clearGolluxClearedMaps()
