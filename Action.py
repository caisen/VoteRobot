#
# Actions
#

import time
from HttpClient import *

def ActionFactory():
	''' action factory, generate actions object'''
	pass

#
# Action classes
#

# Action base class
class Action:
	def __init__(self):
		self._status = 200
		self.url = 'http://votes.cnr.cn/ajax.php'
		self.formData = self.getFormData()
		self.headers = HttpClient.getHeaders()
		self.http = getHtppClient()

	def process(self):
		'''implement by subclasses'''
		self.response, self.content = self.http.request(self.url, self.headers, self.formData)
		self._status = self.response['status']

	def status(self):
		'''200, succeed; otherwise, failed'''
		return self._status

# Action: refresh verify code
class RefreshVerfyCode(Action):
	def __init__(self):
		Action.__init__(self)

	def getFormData(self):
		return {'act' : 'yanzm', 'time' : '20868938901403800000'}#time.time() * 1000000}

# Action: fake share
class FakeShare(Action):
	def __init__(self):
		Action.__init__(self)

	def getFormData(self):
		return {'act' : 'fenxiang', 'id' : '279'}

# Action: Vote
class Vote(Action):
	def __init__(self):
		Action.__init__(self)

	def getFormData(self):
		return {'act' : 'vote', 'id' : '279'}