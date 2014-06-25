
import Action

def OneKick():
	''' vote once'''
	actionQueue = [FakeShare(), RefreshVerfyCode(), Vote(), RefreshVerfyCode(), Vote()]
		for action in actionQueue:
			action.process()
			if action.status() != 0:
				return

def Start():
	for true:

		# wait a few seconds here

		OneKick();
		
#
# Start voting
#
Start()