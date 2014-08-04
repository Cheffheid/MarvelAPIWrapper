from parent import MarvelParent

class MarvelCharacters(MarvelParent):

	def __init__(self, apikey, privkey, base_url):
		self.API_URL = base_url + '/characters'
		self.API_KEY = apikey
		self.PRIV_KEY = privkey

	def getCharacters(self, id, args):
		return "Not a valid method for Characters, use getOne or getList instead"

	def getCreators(self, id, args):
		return "Not a valid method for Characters"