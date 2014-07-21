from parent import MarvelParent

class MarvelComics(MarvelParent):

	def __init__(self, apikey, base_url):
		self.API_URL = base_url + '/comics'
		self.API_KEY = apikey

	def getComics(self, id, args):
		return "Not a valid method for Comics, use getOne or getList instead"

	def getSeries(self, id, args):
		return "Not a valid method for Comics"