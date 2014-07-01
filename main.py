

import time
import random
from Action import *
from IPPool import *

backoffTime = 0 # back off when voting return error code 6
backoffMulti = 0 # multiple

amount = 0
failedAmount = 0

def OneKick(index):
	''' vote once'''
	print('=========Play round %d==========' % index)
	ipPoolInstance.refresh()
	idStr = str(279)
	actionQueue = [Show(idStr), FakeShare(idStr), RefreshVerfyCode(), Vote(), RefreshVerfyCode(), Vote()]
	#actionQueue = [RefreshVerfyCode()]
	i = 0
	for action in actionQueue:
		i += 1
		randomtime = 2
		if i == 5:
			randomtime += 10
		action.process()
		time.sleep(randomtime)

		result = action.result()
		print('result: %d' % result)
		global backoffMulti
		global backoffTime
		global amount
		global failedAmount
		if result == 6:
			backoffMulti += 1
			backoffTime += 30 * backoffMulti
			failedAmount += 1
			return
		elif result == 3:
			backoffMulti = 0
			backoffTime = 0
			amount += 1

def Start():
	for i in range(0, 1000):
		# wait a few seconds here
		global backoffTime
		OneKick(i);
		time.sleep(random.randint(10, 20) + backoffTime)

#
# Start voting
#
Start()
print('1000 voting Done, succeed:%d, failed:%d' % (amount, failedAmount))