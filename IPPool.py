#
# IP pool
#

ip_pool = ['175.152.209.25', '175.152.209.26', '175.152.209.27', '175.152.209.28', '175.152.209.29']

class IPPool:
	'''IP pool'''
	def __init__(self):
		pass

	def getIPCount(self):
		return 5

	def getIP(self, index):
		return ip_pool[index]

	def refresh():
		'''refresh succeed, return true; otherwise, return false'''
		return true

ipPoolInstance = IPPool()