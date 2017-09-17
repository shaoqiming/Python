# coding:utf-8
import urllib2

resopn=urllib2.urlopen("http://www.baidu.com")
html=resopn.read()

print(html)
