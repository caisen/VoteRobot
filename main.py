

import time
import random
from Action import *
from IPPool import *

backoffMulti = 0 # back off multiple when voting return error code 6

amount = 0
failedAmount = 0

def OneKick(index):
	''' vote once'''
	print('=========Play round %d==========' % index)
	ipPoolInstance.refresh()
	idStr = str(279)
	actionQueue = [Show(idStr), FakeShare(idStr), RefreshVerfyCode(), Vote(), Show(idStr), RefreshVerfyCode(), Vote()]
	#actionQueue = [RefreshVerfyCode()]
	i = 0
	for action in actionQueue:

		global backoffMulti
		global amount
		global failedAmount

		# before the second vote
		if i == 4:
			if backoffMulti > 0:
				return
		
		i += 1

		# process action
		action.process()

		randomtime = 2
		time.sleep(randomtime)

		result = action.result()
		print('result: %d' % result)
		if result == 6:
			backoffMulti += 1
			failedAmount += 1
			print('backoffMulti: %d' % backoffMulti)
			return
		elif result == 3:
			if backoffMulti > 0:
				backoffMulti -= 1
			amount += 1

def Start():
	for i in range(0, 1000):
		# wait a few seconds here
		OneKick(i);

		global backoffMulti
		sleepTime = random.randint(10, 20) + (50 * backoffMulti)
		print(sleepTime)
		time.sleep(sleepTime)

#
# Start voting
#
Start()
print('Voting Done, succeed:%d, failed:%d' % (amount, failedAmount))