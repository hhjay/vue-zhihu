import urllib2
rootUrl = 'https://www.zhihu.com'
explore = rootUrl + '/explore'

def crawlPage(url):
	res = urllib2.urlopen(url)
	txt = res.read()
	res.close
	file = open("./buffer.html", "wb")
	file.writelines(txt) # 写入多行在性能上比使用write写入更高
	return txt

print crawlPage(rootUrl)