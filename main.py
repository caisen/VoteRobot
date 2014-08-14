

import time
import random
from Action import *
from IPPool import *
import Utils
import HttpClient

backoffMulti = 0 # back off multiple when voting return error code 6

amount = 0
failedAmount = 0

def OneKick(index):
	''' vote once'''
	print('=========Play round %d==========' % index)

	ipPoolInstance.refresh()
	utilsInstance.refreshSession()
	refreshHttpClient()

	idStr = str(279)
	actionQueue = [Show(idStr), FakeShare(idStr), RefreshVerfyCode(), Vote(), Show(idStr), RefreshVerfyCode(), Vote()]
	#i = 0
	for action in actionQueue:

		global backoffMulti
		global amount
		global failedAmount

		# before the second vote
		#if i == 4:
		#	if backoffMulti > 0:
		#		return
		
		#i += 1

		# process action
		action.process()

		randomtime = 5
		time.sleep(randomtime)

		result = action.result()
		print('result: %d' % result)
		if result == 6:
			backoffMulti = 1
			failedAmount += 1
			#print('backoffMulti: %d' % backoffMulti)
			return
		elif result == 3:
			#if backoffMulti > 0:
			backoffMulti = 0
			amount += 1

def Start():
	for i in range(0, 1):
		# wait a few seconds here
		#OneKick(i);
		ipPoolInstance.refresh()
		utilsInstance.refreshSession()
		refreshHttpClient()
		v = Vote()
		v.process()

		#global backoffMulti
		#sleepTime = random.randint(10, 20)
		
		#time.sleep(2)

#
# Start voting
#
Start()
#print('Voting Done, succeed:%d, failed:%d' % (amount, failedAmount))









