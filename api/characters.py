from parent import MarvelParent

class MarvelCharacters(MarvelParent):

	def __init__(self, apikey, base_url):
		self.API_URL = base_url + '/characters'
		self.API_KEY = apikey

	def getCharacters(self, id, args):
		return "Not a valid method for Characters, use getOne or getList instead"

	def getCreators(self, id, args):
		return "Not a valid method for Characters"