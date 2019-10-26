# Pink Zakum : Pink Zakum Raid

from time import sleep

ZAKUM_BODY = 9400900
ZAKUM_ARM = 9400903 # +1 for each additional arm
pX = -5
pY = 329

sleep(5) # give em time to move outta the way

sm.spawnMob(ZAKUM_BODY, pX, pY, False)
for i in range(8):
	sm.spawnMob(ZAKUM_ARM + i, pX, pY, False)