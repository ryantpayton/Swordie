# horntail entrace - The Cave of Trial 1
from net.swordie.ms.constants import GameConstants

mobs = {
	240060000 : 8810212,
	240060002 : 8810024,
	240060001 : 8810128
}

if int(sm.getQRValue(GameConstants.EASY_HORNTAIL_QUEST)) == 1: 
	sm.spawnMob(mobs[sm.getFieldID()], 868, 230, False)
	sm.killMob(mobs[sm.getFieldID()]) # does the spawn animation
	
	sm.setPartyQRValue(GameConstants.EASY_HORNTAIL_QUEST, "2")