# coding:UTF-8
import hashlib
md5=hashlib.md5()
md5.update("shaoqi".encode('utf-8'))
# 输出了一个MD5的值
print (md5.hexdigest())

# 也可以分两次计算

def calc_md5(password):
    md5.update(password.encode('utf-8'))
    print md5.hexdigest


### itertools 提供操作迭代对象的方法
import itertools
ns=itertools.repeat('ABC',3)
for n in ns:
    print(n)

## 可以从一个无线的序列里面截取出符合条件的序列
natuals=itertools.count(1)

ns=itertools.takewhile(lambda x:x<=10,natuals)

print list(ns)

for c in itertools.chain('ABC',"XYC"):
    print(c)

for key,group in itertools.groupby('AABBBCCAAA'):
    print(key,list(group))

## contextLib
from contextlib import contextmanager

class Query(object):
    def __init__(self,name):
        self.name=name
    def query(self):
        print('query info about %s ..'% self.name)

@contextmanager
def create_query(name):
    print ('Binge')
    q=Query(name)
    yield q
    print ('End')

with create_query('Bod') as q:
    q.query()


#还可以设置某段代码执行前和执行后执行相同的代码
@contextmanager
def tag(name):
    print('<%s>'% name)
    yield
    print('<%s>'% name)

with tag('h1'):
    print('Hello')
    print('world')

## HTMLParser

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print('data+',data)

    def handle_comment(self, data):
        print('<!-- -->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('<html><head></head><body><p>Some <a href=\"#\">html</a> tutorial...<br>END</p></body></html>')