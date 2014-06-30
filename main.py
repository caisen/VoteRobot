
from Action import *
from IPPool import *

def OneKick(index):
	''' vote once'''
	print('=========Play round %d==========' % index)
	# Show(id), FakeShare(id), RefreshVerfyCode()
	idStr = str(279)
	actionQueue = [Show(index, idStr), FakeShare(index, idStr), RefreshVerfyCode(index, ), Vote(index), RefreshVerfyCode(index), Vote(index)]
	#actionQueue = [RefreshVerfyCode()]
	for action in actionQueue:
		action.process()
		#print(action.status())
		#print(action.response)
		#print(action.content)
		#if status != 200:
		#	return

def Start():
	i = 0
	while i < ipPoolInstance.getIPCount():
		ip = ipPoolInstance.getIP(i)
		# wait a few seconds here

		OneKick(i);
		i += 1

#
# Start voting
#
Start()