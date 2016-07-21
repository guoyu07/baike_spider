import urllib.request

class HtmlDownloader(object):

	def download(slef,url):
		if url is None:
			return None
		resp = urllib.request.urlopen(url)
		
		if resp.getcode() != 200:
			return None
		return resp.read()		