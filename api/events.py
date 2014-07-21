from parent import MarvelParent

class MarvelEvents(MarvelParent):

	def __init__(self, apikey, base_url):
		self.API_URL = base_url + '/events'
		self.API_KEY = apikey

	def getEvents(self, id, args):
		return "Not a valid method for Events, use GetOne or GetList instead"