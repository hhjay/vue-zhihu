# -*- coding: utf-8 -*-
import urllib2
rootUrl = 'https://www.zhihu.com'
explore = rootUrl + '/explore'

def crawlPage(url):
	haveNet = crawlOut()
	if haveNet == 000:
		return False
	elif haveNet == 200:
		res = urllib2.urlopen(url)
		txt = res.read()
		res.close
		file = open("./buffer.html", "wb")
		file.writelines(txt) # 写入多行在性能上比使用write写入更高
		return txt
	else:
		return False

# 判断网络连接问题
def crawlOut():
	import urllib2
	linkRes = []
	testUrl = ['http://www.163.com/', 'http://www.qq.com/']
	for i in testUrl:
		try:
			s = urllib2.urlopen(i)
			linkRes.append(s)
		except:
			linkRes.append(None)
		if not any(linkRes):
			return 000 # 联网失败
		else:
			overRes = []
			overUrl = 'https://www.google.com.hk'
			try:
				s = urllib2.urlopen(overUrl)
				overRes.append(s)
			except:
				overRes.append(None)
			if not any(overRes):
				return 100 # 翻墙失败
			else:
				return 200 # 翻墙失败 但联网成功

print crawlPage(rootUrl)