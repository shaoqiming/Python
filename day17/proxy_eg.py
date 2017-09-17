# coding:utf-8

import urllib.request
import random

# 代理使用
url = 'http://www.whatismyip.com.tw/'

iplist=['58.250.119.48:80','111.155.116.235:8123','183.153.63.223:808']

proxy_support = urllib.request.ProxyHandler({'http': random.choice(iplist)})

open = urllib.request.build_opener(proxy_support)

open.addheaders = [("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")]

urllib.request.install_opener(open)

request = urllib.request.urlopen(url)

html = request.read().decode('utf-8')

print(html)
