import requests 
import bs4 

rootUrl = 'https://www.zhihu.com'
explore = rootUrl + '/explore'

def crawlPage(url):
	req = requests.get(url)
	# return req
	root = bs4.BeautifulSoup(req.text)
	return [a.attrs.get('href') for a in soup.select('div.feed-item')]
	# return [a.attrs.get(href) for a in root.select('div.feed-item')]

print crawlPage(explore)