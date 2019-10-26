# Head Researcher Wynn
# Pink Zakum : Pink Zakum Exit

if sm.getFieldID() == 689010000: # waiting map
	#if sm.isPinkZakumOpen():
	#	sm.sendSayOkay("The event will start soon!")
	#else:
		sm.sendSayOkay("Have you heard of the terrifying Zakum? This one's pink! He's not so scary anymore.")
else: # reward map
	sm.sendNext("Good job defeating the Pink Zakum!")
	# TODO give reward points
	sm.warp(sm.getPreviousFieldID(), 0, False)