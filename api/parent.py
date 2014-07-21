import requests
import hashlib
import time

class MarvelParent(object):

	def getHash(self, ts, priv_key, pub_key):
		return hashlib.md5(ts+priv_key+pub_key).hexdigest()

	def getList(self, args):
		request_url = self.API_URL + '?apikey=%s' % self.API_KEY
		ts = str(time.time())

		request_url += '&ts=%s' % ts
		request_url += '&hash=%s' % self.getHash(ts, self.PRIV_KEY, self.API_KEY)

		for arg in args:
			request_url += "&%s=%s" % (arg, args[arg])

		print request_url
		return requests.get(request_url)

	def getOne(self, id):
		request_url = self.API_URL + '/%s?apikey=%s' % (id, self.API_KEY)
		ts = str(time.time())

		request_url += '&ts=%s' % ts
		request_url += '&hash=%s' % self.getHash(ts, self.PRIV_KEY, self.API_KEY)

		return requests.get(request_url)

	def getCharacters(self, id, args):
		request_url = self.API_URL + '/%s/characters?apikey=%s' % (id, self.API_KEY)
		ts = str(time.time())

		request_url += '&ts=%s' % ts
		request_url += '&hash=%s' % self.getHash(ts, self.PRIV_KEY, self.API_KEY)

		for arg in args:
			request_url += "&%s=%s" % (arg, args[arg])

		return requests.get(request_url)

	def getComics(self, id, args):
		request_url = self.API_URL + '/%s/comics?apikey=%s' % (id, self.API_KEY)
		ts = str(time.time())

		request_url += '&ts=%s' % ts
		request_url += '&hash=%s' % self.getHash(ts, self.PRIV_KEY, self.API_KEY)

		for arg in args:
			request_url += "&%s=%s" % (arg, args[arg])

		return requests.get(request_url)

	def getCreators(self, id, args):
		request_url = self.API_URL + '/%s/creators?apikey=%s' % (id, self.API_KEY)
		ts = str(time.time())

		request_url += '&ts=%s' % ts
		request_url += '&hash=%s' % self.getHash(ts, self.PRIV_KEY, self.API_KEY)

		for arg in args:
			request_url += "&%s=%s" % (arg, args[arg])

		return requests.get(request_url)

	def getEvents(self, id, args):
		request_url = self.API_URL + '/%s/events?apikey=%s' % (id, self.API_KEY)
		ts = str(time.time())

		request_url += '&ts=%s' % ts
		request_url += '&hash=%s' % self.getHash(ts, self.PRIV_KEY, self.API_KEY)

		for arg in args:
			request_url += "&%s=%s" % (arg, args[arg])

		return requests.get(request_url)

	def getSeries(self, id, args):
		request_url = self.API_URL + '/%s/series?apikey=%s' % (id, self.API_KEY)
		ts = str(time.time())

		request_url += '&ts=%s' % ts
		request_url += '&hash=%s' % self.getHash(ts, self.PRIV_KEY, self.API_KEY)

		for arg in args:
			request_url += "&%s=%s" % (arg, args[arg])

		return requests.get(request_url)

	def getStories(self, id, args):
		request_url = self.API_URL + '/%s/stories?apikey=%s' % (id, self.API_KEY)
		ts = str(time.time())

		request_url += '&ts=%s' % ts
		request_url += '&hash=%s' % self.getHash(ts, self.PRIV_KEY, self.API_KEY)

		for arg in args:
			request_url += "&%s=%s" % (arg, args[arg])

		return requests.get(request_url)