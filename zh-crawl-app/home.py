# -*- coding: utf-8 -*-
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

def timeOut():
	import urllib2
	overRes = []
	overStr = urllib2.urlopen(overUrl)
	overRes.append(overWallS)
	return overRes
	linkRes = []
	overRes = []
	testUrl = ['http://www.163.com/', 'http://www.qq.com/']
	for i in testUrl:
		try:
			s = urllib2.urlopen(i)
			linkRes.append(s)
		except:
			linkRes.append(None)
		if not any(linkRes):
			return 00 # 联网失败
		else:
			overUrl = 'https://www.google.com.hk'
			overStr = urllib2.urlopen(overUrl)
			overRes.append(overWallS)
			if not any(overRes):
				return 10 # 翻墙失败
			else:
				return 01 # 翻墙失败 但联网成功

print timeOut()
print crawlPage(rootUrl)