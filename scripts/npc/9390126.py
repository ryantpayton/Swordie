# 863010000 - Gollux

sm.setSpeakerID(9390124) #Heart Tree Guardian
response = sm.sendNext("<#e#rRoad to Gollux#n>\r\n#kThis is where #rGollux#k, the Heart Tree corrupted by rage, is located.\r\n#r(Your entry record will reset 22 hours after your previous entry.)\r\n#L0##bEnter to fight Gollux now (Lv. 140 Required)\r\n#L1##bChallenge later.")


if response == 0:
    if sm.getParty() is None:
        sm.sendSayOkay("You must be in a party before attempting to challenge the boss!")
    elif not sm.isPartyLeader():
        sm.sendSayOkay("Please have your party leader enter if you wish to face Gollux.")
    elif sm.checkParty():
        sm.warpInstanceIn(863010100, 5, True)
else:
    sm.sendSayOkay("#fs16#We are in grave need of your help!\r\n#fs12#Gollux has almost entirely been corrupted, please find the time to join the cause!")
sm.dispose()
