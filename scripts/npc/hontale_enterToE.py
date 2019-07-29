# Encrypted Slate of the Squad(2083000) | Cave of Life, Cave Entrance
if sm.isPartyLeader() and sm.sendAskYesNo("The letters on the slate glitter and the backdoor opens. Do you want to go to the secret path?"):
    sm.warpInstanceIn(240050400, True)
else:
    sm.sendSayOkay("Please proceed through the Party leader.")