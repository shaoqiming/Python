# -*- coding:UTF-8 -*-

from heapq import *
from random import shuffle
#双端队列
from collections import deque
a=set([1,2,3])
b=set([2,3,4])
#分解
c=set('boyd')
c.add("ddd")
print c
print c.__doc__
print c

data=range(10)
#随机重新排列序列
shuffle(data)

heap=[]
for n in data:
    heappush(heap,n)

print data

q=deque(range(5))
print q

q.append(5)
print q

q.appendleft(6)
print q

print q.rotate.__doc__
#函数没有返回值
q.rotate(3)
print q
