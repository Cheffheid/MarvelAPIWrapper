from api.characters import MarvelCharacters
from api.comics import MarvelComics
from api.series import MarvelSeries
from api.events import MarvelEvents
from api.creators import MarvelCreators
from api.stories import MarvelStories

class MarvelAPIObject(object):
	BASE_URL = "http://gateway.marvel.com/v1/public"
	
	def __init__(self, apikey=None, privkey=None):
		self.API_KEY = apikey
		self.PRIV_KEY = privkey

		self.characters = MarvelCharacters(self.API_KEY, self.PRIV_KEY, self.BASE_URL)
		self.comics = MarvelComics(self.API_KEY, self.BASE_URL)
		self.series = MarvelSeries(self.API_KEY, self.BASE_URL)
		self.events = MarvelEvents(self.API_KEY, self.BASE_URL)
		self.creators = MarvelCreators(self.API_KEY, self.BASE_URL)
		self.stories = MarvelStories(self.API_KEY, self.BASE_URL)