#!/usr/bin/python  
#-*-coding:utf-8-*- 
# import sys
import chardet
import requests 
import bs4 

rootUrl = 'https://www.baidu.com/index.html' # http://blog.lanyus.com/archives/133.html 这个可以
# explore = rootUrl + '/explore'

def crawlPage(url):
	req = requests.get(url)
	txt = open(req.text) # reload # .decode('gbk')
	return chardet.detect(req.text)
	# root = bs4.BeautifulSoup(req.text)
	# return txt

print crawlPage(rootUrl)