# coding:utf-8

import threading
import time

def test():
    print "shaoqi"

a=threading.Thread(target=test)

a.start()


ts=[]

def test1(p):
    time.sleep(0.01)
    print p

for i in xrange(0,15):
    # args=[] 要为[]
    th=threading.Thread(target=test1,args=[i])
    ts.append(th)

for j in ts:
    j.start()

print 'end!!!!'