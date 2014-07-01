

import time
import random
from Action import *
from IPPool import *


def OneKick(index):
	''' vote once'''
	print('=========Play round %d==========' % index)
	ipPoolInstance.refresh()
	idStr = str(279)
	actionQueue = [Show(idStr), FakeShare(idStr), RefreshVerfyCode(), Vote(), RefreshVerfyCode(), Vote()]
	#actionQueue = [RefreshVerfyCode()]
	for action in actionQueue:
		action.process()
		time.sleep(random.randint(1, 2))
		#if status != 200:
		#	return

def Start():
	for i in range(0, 1000):
		# wait a few seconds here

		OneKick(i);
		time.sleep(random.randint(10, 20))

#
# Start voting
#
Start()
print('1000 voting Done!')