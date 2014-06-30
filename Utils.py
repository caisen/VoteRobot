#
# Utils
#

class Utils:
	def __init__(self):
		self.timestamp = ''

	def getTimestamp(self):
		return self.timestamp

	def setTimestamp(self, time):
		self.timestamp = time

	def setCode(self, code):
		self.code = code

	def getCode(self):
		return self.code

utilsInstance = Utils()