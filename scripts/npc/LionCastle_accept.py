# Mark of the Squad(2083004) | Cave of Life, Entrance to Horntail's Cave
from net.swordie.ms.constants import BossConstants
from net.swordie.ms.constants import GameConstants
if sm.getFieldID() == 211070100 or sm.getFieldID() == 211070102:
    if sm.sendAskYesNo("Would you like to leave the fight?"):
        sm.warpInstanceOut(211070000, 0)
else:
    if sm.isPartyLeader():
        sm.sendNext("#e<Boss:Von Leon>#n \r\n Are you brave enough to face Von Leon?#b\r\n \r\n"
                    "#L0#Apply to enter Von Leon expedition.#l\r\n")
        selection = sm.sendNext("#e<Boss:Von Leon>#n \r\n Select a mode. \r\n \r\n"
                                "#L0#Easy(Level 125+) #l \r\n"
                                "#L1#Normal (Level 125+) #l \r\n")
        if selection == 0:
            sm.warpInstanceIn(211070100, True)
            sm.setInstanceTime(BossConstants.VON_LEON_TIME)
        elif selection == 1:
            sm.warpInstanceIn(211070102, True)
            sm.setInstanceTime(BossConstants.VON_LEON_TIME)
    else:
        sm.sendSayOkay("Please have your party leader speak to me.")