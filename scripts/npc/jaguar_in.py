# Black Jack - Resistance Headquarters : Secret Plaza
if (sm.getChr().getJob() % 3300 > 12):
    sm.sendSayOkay("Grrrr....(You can't enter. Only Wild Hunters may enter.)")
    sm.dispose()
response = sm.sendAskYesNo("Do you want to enter the jaguar habitat?")

if response:
    sm.warp(931000500, 0)