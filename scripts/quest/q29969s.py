# The Mind of the Raven

medal = 1142377

if sm.canHold(medal):
    sm.chat("You have earned a new medal.")
    sm.giveItem(medal)
    sm.startQuestNoCheck(parentID)
    sm.completeQuestNoRewards(parentID)
sm.dispose()
