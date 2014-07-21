from parent import MarvelParent

class MarvelSeries(MarvelParent):

	def __init__(self, apikey, base_url):
		self.API_URL = base_url + '/series'
		self.API_KEY = apikey

	def getSeries(self, id, args):
		return "Not a valid method for Series, use getOne or getList instead"