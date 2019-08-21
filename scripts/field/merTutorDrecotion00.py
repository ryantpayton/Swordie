#Strange Space : Darkness | 4000000
if sm.sendAskYesNo("Would you like to skip the introduction?"):
    sm.startQuestNoCheck(24005)
    sm.warp(101050010)
    sm.dispose()
sm.giveSkill(20021181, 1)
sm.playVideoByScript("Mercedes.avi")