#
# Actions
#

def ActionFactory():
	''' action factory, generate actions object'''
	pass

#
# Action classes
#

# Action base class
class Action:
	def __init__(self, params):
		pass

	def process():
		'''implement by subclasses'''
		pass

	def status():
		'''0, succeed; otherwise, failed'''
		return 0

# Action: refresh verify code
class RefreshVerfyCode(Action):
	def __init__(self, params):
		Action.__init__(params)
		pass

	def process():
		pass

	def status():
		return 0

# Action: fake share
class FakeShare(Action):
	def __init__(self, params):
		Action.__init__(params)
		pass

	def process():
		pass

	def status():
		return 0

# Action: Vote
class Vote(Action):
	def __init__(self, params):
		Action.__init__(params)
		pass

	def process():
		pass

	def status():
		return 0