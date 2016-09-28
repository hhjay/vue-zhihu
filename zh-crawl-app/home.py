# #!../../../../../Program Files/python/python  
# #-*-coding:utf-8-*- 
# # import sys
# import chardet
# import requests 
# import bs4 
# rootUrl = 'https://www.zhihu.com' # http://blog.lanyus.com/archives/133.html 这个可以
# explore = rootUrl + '/explore'
# def crawlPage(url):
# 	req = requests.get(url)
# 	root = bs4.BeautifulSoup(req.text, "html.parser")
# 	print root
# crawlPage(explore) 使用request和bs4还需要引入模板才可以哦


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