# Kaiser's Successor

medal = 1142487

if sm.canHold(medal):
    sm.chat("You have earned a new medal.")
    sm.giveItem(medal)
    sm.startQuestNoCheck(parentID)
    sm.completeQuestNoRewards(parentID)
sm.dispose()
