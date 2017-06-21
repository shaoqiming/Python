# coding:UTF-8
'''
时间可以通过元组去表示，（2008,1,21,12,3,56,0,12,0）
'''
import time
import random

import shelve

print time.asctime()

print "休眠好了"

print time.strptime(time.asctime())

print random.random()
#二进制的位数 随机出数字
print random.getrandbits(9)

s=shelve.open('shaoqi.txt')
s['X']=['a','b','c']

print s['X']


