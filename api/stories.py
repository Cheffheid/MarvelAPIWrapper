from abstract import MarvelAbstract

class MarvelStories(MarvelAbstract):

	def __init__(self, apikey, base_url):
		self.API_URL = base_url + '/stories'
		self.API_KEY = apikey

	def getStories(self, id, args):
		return "Not a valid method for Stories, use getOne or getList instead"