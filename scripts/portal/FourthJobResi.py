# Portal to the 4th Job Advancement for Main Resistance

validJobIDs = [3211, 3311, 3511, 3711]

charJobID = sm.getChr().getJob()
if charJobID not in validJobIDs:
    sm.dispose()

if charJobID == 3211:
    sm.warpInstanceIn(931000300, 0, False) # BATTLE MAGE
elif charJobID == 3311:
    sm.warpInstanceIn(931000301, 0, False) # WILD HUNTER
elif charJobID == 3511:
    sm.warpInstanceIn(931000302, 0, False) # MECHANIC
elif charJobID == 3711:
    sm.warpInstanceIn(931000303, 0, False) # BLASTER

sm.setInstanceTime(15*60)