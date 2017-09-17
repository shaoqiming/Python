# coding:utf-8
import hashlib
import urllib
import urllib2
import time
import json

m = hashlib.md5()
d = 'i love you'
url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=null'
u = 'fanyideskweb'
f = str(int(time.time() * 1000))
c = "rY0D^0'nM0}g5Mm1z%1G4"

m.update((u + d + f + c).encode('utf-8'))

data = {
    'i': d,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': u,
    'salt': f,
    'sign': m.hexdigest(),
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_ENTER',
    'typoResult': 'true'
}

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    'Origin': 'http://fanyi.youdao.com/',
    'Referer': 'http://fanyi.youdao.com/',
}


data=urllib.urlencode(data)

Req=urllib2.Request(url,data,headers)

response=urllib2.urlopen(Req);

html=response.read()

print(html)

target=json.loads(html)

print(target['translateResult'][0][0]['tgt'])
# print('data', data)
# Req = urllib2.Request(url, data=data ,headers=headers)
#
# request = urllib2.urlopen(Req)
#
# html = request.read()
#
# print ('dd')
# request(html)
