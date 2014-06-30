#
# Actions
#

import time
from HttpClient import *
from Utils import *

#
# Action classes
#

# Action base class
class Action:
	def __init__(self):
		self._status = 200
		self._message = 'Succeed'
		self.url = 'http://votes.cnr.cn/ajax.php'
		self.method = 'POST'
		self.http = getHtppClient()

	def getHeaders(self):
		return {'Host' : 'votes.cnr.cn', \
				'Origin' : 'http://votes.cnr.cn', \
				'Referer' : 'http://votes.cnr.cn/show.php?id=279', \
				'Content-Type' : 'application/x-www-form-urlencoded', \
				'X-Forwarded-For' : '175.152.209.24', \
				'Cookie' : 'PHPSESSID=afsbgsm4uokronqbdmdt130533; CNZZDATA5915424=cnzz_eid%3D279823847-1403541396-http%253A%252F%252Fvotes.cnr.cn%252F%26ntime%3D1403886826', \
				'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36' }

	def getFormData(self):
		return {}

	def process(self):
		'''implement by subclasses'''
		self.response, self.content = self.http.request(self.url, self.method, self.getHeaders(), self.getFormData())
		self._status = self.response['status']

	def status(self):
		'''200, succeed; otherwise, failed'''
		return self._status

	def message(self):
		'''message such as succeed or failed'''
		return self._message

# Action: Show, get the time for refreshing verify code
class Show(Action):
	def __init__(self, idStr):
		Action.__init__(self)
		self.url = 'http://votes.cnr.cn/show.php?id=' + idStr
		self.method = 'GET'

	def getHeaders(self):
		return {'Host' : 'votes.cnr.cn'}

	def process(self):
		Action.process(self)

		# find the timestamp
		keyWord = 'yanzm&time=\'+'
		decodedContent = self.content.decode()
		pos = decodedContent.find(keyWord)
		if pos != -1:
			# found
			keyWordLen = len(keyWord)
			timeBeginPos = pos + keyWordLen
			timeEndPos = decodedContent.find(';', timeBeginPos)
			if timeEndPos != -1:
				timeLen = timeEndPos - timeBeginPos
				maxTimeLen = 20 # timestamp is a 19 or 20 character string
				if timeLen <= maxTimeLen:
					# bingo
					self._status = 0
					timeS = decodedContent[timeBeginPos : timeEndPos]
					utilsInstance.setTimestamp(timeS)
				else:
					self._status = -1
					self._message = 'Finding timestamp failed(end).'
			else:
				self._status = -1
				self._message = 'Finding timestamp failed(begin).'

# Action: refresh verify code
class RefreshVerfyCode(Action):
	def __init__(self):
		Action.__init__(self)

	def getFormData(self):
		return {'act' : 'yanzm', 'time' : utilsInstance.getTimestamp()}

	def process(self):
		Action.process(self)
		originCode = self.content.decode()
		self._dealWithCode(originCode)

	def _dealWithCode(self, originCode):
		# filtering <span style='display:none'></span> and &nbsp
		needContinue = True
		while needContinue:
			# delete span
			beginSpanPos = originCode.find('<span')
			if beginSpanPos == -1:
				needContinue = False
				break
			else:
				endSpanPos = originCode.find('</span>')
				if endSpanPos == -1:
					needContinue = False
					break

			if beginSpanPos < endSpanPos:
				originCode = originCode[:beginSpanPos] + originCode[endSpanPos + 7:]
			else:
				needContinue = False
				break
				
		# delete &nbsp
		finalCode = originCode.replace('&nbsp', '')

		utilsInstance.setCode(finalCode[1:3])

# Action: fake share
class FakeShare(Action):
	def __init__(self, idStr):
		Action.__init__(self)
		self.idStr = idStr

	def getFormData(self):
		return {'act' : 'fenxiang', 'id' : self.idStr}

# Action: Vote
class Vote(Action):
	def __init__(self):
		Action.__init__(self)

	def getFormData(self):
		return {'act' : 'vote', 'id' : '279', 'yzm' : utilsInstance.getCode()}

	def process(self):
		Action.process(self)
		print(self.response)
		print(self.content)



