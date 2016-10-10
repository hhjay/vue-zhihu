# -*- coding: utf-8 -*-
import urllib2
rootUrl = 'https://www.zhihu.com'
explore = rootUrl + '/explore'

def crawlPage(url):
	haveNet = crawlOut()
	if haveNet == 000:
		fp = open("./home.html", "w")
		txt = fp.readlines() # 读取所以内容
		return txt
	elif haveNet == 200:
		res = urllib2.urlopen(url)
		txt = res.read()
		res.close # 关闭文档流并写入文件
		fp = open("./home.html", "wb")
		fp.writelines(txt) # 写入多行在性能上比使用write写入更高
		return txt

# 判断网络连接问题 直接判断本地忘络 无须判断是否能翻墙
def crawlOut():
	import urllib2
	overRes = []
	testUrl = ['http://www.163.com/', 'http://www.qq.com/']
	for i in testUrl:
		try:
			s = urllib2.urlopen(i)
			overRes.append(s)
		except:
			overRes.append(None)
	if not any(overRes):
		return 000 # 联网失败
	else:
		return 200 # 翻墙失败 但联网成功

# 解析html格式
def parseHtml():
	import urllib2
	from sgmllib import SGMLParser
	class ListName(SGMLParser):
		def __init__(self):
			SGMLParser.__init__(self)
			self.name = []

		def handle_data(self, text):
			if self.is_h4 == 1:
				self.name.append(text)

	main = crawlPage(rootUrl)
	ListName = ListName()
	ListName.feed(main)
	print ListName.links

parseHtml()