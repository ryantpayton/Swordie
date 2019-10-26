# Chaos horntail gem

from net.swordie.ms.constants import BossConstants
import random

HORNTAIL = 8810130 # HT invis body, when this is killed it spawns all the HT parts

SPAWN_PX = 95
SPAWN_PY = 260

reactor.incHitCount()
reactor.increaseState()
if reactor.getHitCount() >= 4:
	sm.spawnMob(HORNTAIL, SPAWN_PX, SPAWN_PY, False)
	sm.killMob(HORNTAIL, False)
	sm.removeReactor()