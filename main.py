
from Action import *

def OneKick():
	''' vote once'''
	# Show(id), FakeShare(id), RefreshVerfyCode()
	idS = str(279)
	actionQueue = [FakeShare(idS)]
	for action in actionQueue:
		action.process()
		#print(action.status())
		print(action.response)
		print(action.content)
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