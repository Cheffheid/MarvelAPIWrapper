import requests
import hashlib
import time

class MarvelParent(object):

	def getHash(self, ts, priv_key, pub_key):
		return hashlib.md5(ts+priv_key+pub_key).hexdigest()

	def getRequestURL(self, id=None, subType=None, args={}):
		request_url = self.API_URL

		if id:
			request_url += '/%s' % id

		if subType:
			request_url += '/%s' % subType

		ts = str(time.time())
		reqHash = self.getHash(ts, self.PRIV_KEY, self.API_KEY)

		request_url += '?apikey=%s&ts=%s&hash=%s' % (self.API_KEY, ts, reqHash)

		for arg in args:
			request_url += "&%s=%s" % (arg, args[arg])		

		print request_url
		return request_url

	def getList(self, args):
		request_url = self.getRequestURL(args=args)

		return requests.get(request_url)

	def getOne(self, id):
		request_url = self.getRequestURL(id)

		return requests.get(request_url)

	def getCharacters(self, id, args):
		request_url = self.getRequestURL(id=id, subType='characters', args=args)

		return requests.get(request_url)

	def getComics(self, id, args):
		request_url = self.getRequestURL(id=id, subType='comics', args=args)

		return requests.get(request_url)

	def getCreators(self, id, args):
		request_url = self.getRequestURL(id=id, subType='creators', args=args)

		return requests.get(request_url)

	def getEvents(self, id, args):
		request_url = self.getRequestURL(id=id, subType='events', args=args)

		return requests.get(request_url)

	def getSeries(self, id, args):
		request_url = self.getRequestURL(id=id, subType='series', args=args)

		return requests.get(request_url)

	def getStories(self, id, args):
		request_url = self.getRequestURL(id=id, subType='stories', args=args)

		return requests.get(request_url)