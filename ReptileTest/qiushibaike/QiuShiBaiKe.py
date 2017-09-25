# coding:utf-8
import urllib
import urllib2
import re

page =1
url='http://www.qiushibaike.com/hot/page/' + str(page)


try:
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    headers = {'User-Agent': user_agent}
    request=urllib2.Request(url,headers=headers)
    response=urllib2.urlopen(request)

    html=response.read()
    pattern=re.compile('<div.*?clearfix">.*?<h2>(.*?)</h2>.*?<div.*?span>(.*?)</span>.*?number">(.*?)</i>',re.S)
    items = re.findall(pattern, html)

    for item in items:
        print "-----------"
        print item[0],item[1],item[2]

except urllib2.URLError,e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason

