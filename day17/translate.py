# coding:utf-8


import urllib2
from urllib import urlencode


url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom="

data = {}

data['i'] = 'i love you'
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '1505484533491'
data['sign'] = 'ffc965a2633270610982c6ead51ef782'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CLICKBUTTION'
data['typoResult'] = 'true'

data=urlencode(data).encode('utf-8')

request = urllib2.urlopen(url, data)
html=request.read().decode('utf-8')


print(html)