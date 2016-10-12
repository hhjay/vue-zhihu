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
from HTMLParser import HTMLParser
class myHtmlParser(HTMLParser):  
    #处理<!开头的内容  
    def handle_decl(self,decl):  
        print 'Encounter some declaration:'+ decl  
    def handle_starttag(self,tag,attrs):  
        print 'Encounter the beginning of a %s tag' % tag  
    def handle_endtag(self,tag):  
        print 'Encounter the end of a %s tag' % tag  
    #处理注释  
    def handle_comment(self,comment):   
        print 'Encounter some comments:' + comment

m = myHtmlParser()
h = crawlPage(rootUrl)
m.feed(h)  
m.close() 

