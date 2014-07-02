#
# Utils
#

import random, string

class Utils:
	def __init__(self):
		pass

	# timestamp
	def getTimestamp(self):
		return self.timestamp

	def setTimestamp(self, time):
		self.timestamp = time

	# verify code
	def setCode(self, code):
		self.code = code

	def getCode(self):
		return self.code

	# session
	def refreshSession(self):
		self.session = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz0123456789', 26)).replace("','", '')

	def getSession(self):
		return self.session

utilsInstance = Utils()