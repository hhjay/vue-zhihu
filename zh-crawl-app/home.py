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
    def handle_startendtag(self, comment):
    	print self + "<br/>" + comment

m = myHtmlParser()
h = crawlPage(rootUrl)
m.feed(h)  
m.close() 

'''
HTMLParser的成员函数: 
 
    handle_startendtag  处理开始标签和结束标签 
    handle_starttag     处理开始标签，比如<xx> 
    handle_endtag       处理结束标签，比如</xx> 
    handle_charref      处理特殊字符串，就是以&#开头的，一般是内码表示的字符 
    handle_entityref    处理一些特殊字符，以&开头的，比如   
    handle_data         处理数据，就是<xx>data</xx>中间的那些数据 
    handle_comment      处理注释 
    handle_decl         处理<!开头的，比如<!DOCTYPE html PUBLIC “-//W3C//DTD HTML 4.01 Transitional//EN” 
    handle_pi           处理形如<?instruction>的东西 
 
'''