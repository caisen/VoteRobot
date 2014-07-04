#
# Http client
#

import urllib.parse
import httplib2

class HttpClient:
	'''Http client'''
	def __init__(self):
		self.http = httplib2.Http()

	def request(self, url, metohd, headers, formData):
		return self.http.request(url, metohd, headers=headers, body=urllib.parse.urlencode(formData))


# create httpclient instance
httpClient = HttpClient()
def getHtppClient():
	return httpClient

def refreshHttpClient():
	httpClient = HttpClient()