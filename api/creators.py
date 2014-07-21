from parent import MarvelParent

class MarvelCreators(MarvelParent):

	def __init__(self, apikey, base_url):
		self.API_URL = base_url + '/creators'
		self.API_KEY = apikey

	def getCharacters(self, id, args):
		return "Not a valid method for Creators"

	def getCreators(self, id, args):
		return "Not a valid method for Creators, use getOne or getLIst instead"