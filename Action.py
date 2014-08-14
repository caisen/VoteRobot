#
# Actions
#

import time
from HttpClient import *
from Utils import *
from IPPool import *

#
# Action classes
#
# Action base class
class Action:
	def __init__(self):
		self._status = 200 
		self._result = 0 # 0, normal; 3, succeed; otherwise, failed
		self._message = 'Succeed'
		self.url = 'http://top.chengdu.cn/acts/2014_huoguo50/base.php'
		self.method = 'POST'
		self.http = getHtppClient()
		# ; CNZZDATA5915424=cnzz_eid%3D279823847-1403541396-http%253A%252F%252Fvotes.cnr.cn%252F%26ntime%3D1403541396
	def getHeaders(self):
		return {'Host' : 'top.chengdu.cn', \
				'Origin' : 'http://top.chengdu.cn', \
				'Referer' : 'http://top.chengdu.cn/acts/2014_huoguo50/', \
				'Content-Type' : 'pplication/x-www-form-urlencoded; charset=UTF-8', \
				'Cookie' : 'pgv_pvi=1586438144; pgv_si=s6836620288; PHPSESSID=3ba5518e67c5a2259fcf6d4b05b02e6b;', \
				'X-Forwarded-For' : '175.152.210.79', \
				'X-Requested-With' : 'XMLHttpRequest', \
				'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'}

	def getFormData(self):
		return {}

	def process(self):
		'''implement by subclasses'''
		print(self.url)
		print(self.method)
		print(self.getHeaders())
		print(self.getFormData())
		self.response, self.content = self.http.request(self.url, self.method, self.getHeaders(), self.getFormData())
		#if self.response['status'] 
		self._status = self.response['status']

	def status(self):
		'''200, succeed; otherwise, failed'''
		return self._status

	def result(self):
		return self._result

	def message(self):
		'''message such as succeed or failed'''
		return self._message

# Action: Show, get the time for refreshing verify code
class Show(Action):
	def __init__(self, idStr):
		Action.__init__(self)
		self.url = 'http://votes.cnr.cn/show.php?id=' + idStr
		self.method = 'GET'
#ipPoolInstance.getCurrentIP(), \
	def getHeaders(self):
		return {'Host' : 'votes.cnr.cn', \
				'Origin' : 'http://votes.cnr.cn', \
				'Cookie' : 'pgv_pvi=1586438144; pgv_si=s6836620288; PHPSESSID=0327aaafc057073a20abcf03d13d13f6;', \
				'X-Forwarded-For' : '175.152.210.79', \
				'X-Requested-With' : 'XMLHttpRequest', \
				'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'}

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
		return {'action' : 'vote', 'id' : 33390609}

	def process(self):
		Action.process(self)
		print(self.response)
		print(self.content.decode())
		#self._result = int(self.content.decode())
		



