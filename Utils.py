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

utilsInstance = Utils()