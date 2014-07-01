#
# IP pool
#
import random

class IPPool:
	'''IP pool'''
	def __init__(self):
		pass

	def getCurrentIP(self):
		return self.ip

	def _genIP(self):
		self.ip = ''
		# #1 field
		while True:
			first = random.randint(10, 223)
			if first != 127:
				self.ip += str(first)
				break

		# #2-#4 field
		for i in range(0, 3):
			num = random.randint(1, 254)
			self.ip += '.' + str(num)

	def refresh(self):
		self._genIP()

ipPoolInstance = IPPool()