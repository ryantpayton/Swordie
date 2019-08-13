if sm.getChr().getJob() == 3211:
    sm.warpInstanceIn(931000300, 0, False) # BATTLE MAGE
elif sm.getChr().getJob() == 3311:
    sm.warpInstanceIn(931000301, 0, False) # WILD HUNTER
elif sm.getChr().getJob() == 3511:
    sm.warpInstanceIn(931000302, 0, False) # MECHANIC
elif sm.getChr().getJob() == 3711:
    sm.warpInstanceIn(931000303, 0, False) # BLASTER

sm.setInstanceTime(15*60)