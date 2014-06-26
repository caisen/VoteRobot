
from Action import *

def OneKick():
	''' vote once'''
	# 
	actionQueue = [FakeShare(), RefreshVerfyCode(), Vote(), RefreshVerfyCode(), Vote()]
	for action in actionQueue:
		action.process()
		status = action.status()
		print(status)
		#if status != 200:
		#	return

#def Start():
	#for 1:

		# wait a few seconds here

		#OneKick();

#
# Start voting
#
OneKick()