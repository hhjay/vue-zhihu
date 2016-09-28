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
req = urllib2.Request('https://www.zhihu.com/explore')
res = urllib2.urlopen(req)
print res.read()


## 明天尝试使用urlopen