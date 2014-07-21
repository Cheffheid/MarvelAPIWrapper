class MarvelParent(object):

	def getList(self, args):
		request_url = self.API_URL + '?apikey=%s' % self.API_KEY

		for arg in args:
			request_url += "&%s=%s" % (arg, args[arg])

		return request_url

	def getOne(self, id):
		request_url = self.API_URL + '/%s?apikey=%s' % (id, self.API_KEY)
		
		return request_url

	def getCharacters(self, id, args):
		request_url = self.API_URL + '/%s/characters?apikey=%s' % (id, self.API_KEY)

		for arg in args:
			request_url += "&%s=%s" % (arg, args[arg])

		return request_url

	def getComics(self, id, args):
		request_url = self.API_URL + '/%s/comics?apikey=%s' % (id, self.API_KEY)

		for arg in args:
			request_url += "&%s=%s" % (arg, args[arg])

		return request_url

	def getCreators(self, id, args):
		request_url = self.API_URL + '/%s/creators?apikey=%s' % (id, self.API_KEY)

		for arg in args:
			request_url += "&%s=%s" % (arg, args[arg])

		return request_url

	def getEvents(self, id, args):
		request_url = self.API_URL + '/%s/events?apikey=%s' % (id, self.API_KEY)

		for arg in args:
			request_url += "&%s=%s" % (arg, args[arg])

		return request_url

	def getSeries(self, id, args):
		request_url = self.API_URL + '/%s/series?apikey=%s' % (id, self.API_KEY)

		for arg in args:
			request_url += "&%s=%s" % (arg, args[arg])

		return request_url

	def getStories(self, id, args):
		request_url = self.API_URL + '/%s/stories?apikey=%s' % (id, self.API_KEY)

		for arg in args:
			request_url += "&%s=%s" % (arg, args[arg])

		return request_url