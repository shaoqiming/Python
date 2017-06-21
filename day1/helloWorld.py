#-*- coding: UTF-8 -*-   
import math
import string

print ("Hello world+烧起")

print(pow(2,3))

print(math.floor(32.9))

Head_format="print of eggs:% .*s";

print Head_format % (3,"shjaoqisdihfiahd")

width=35
price_width=10;
item_width=25

Head_format1='%-*s%*s'
format1='%-*s%*.2f'

print '='*width

print Head_format1 % (item_width,'item',price_width,'prince')
print '-'*width

#常用的字符串
print string.digits

items=[('name','Gumby'),('age',42)] 

print dict(items)

#dict
# d={'x':1,'y':2}
# a=d.pop('x');
# print 'a=%s' % a
# print(d)


d={'x':1,'y':2,'z':3,'r':6}
a=d.popitem();
print(a)
print(d)


def hello(name):
    'dddsdsadfjakdsjf'
    return 'hello '+name+'!'

print hello("shaoqi")
print hello.__doc__
print help(hello)

params=(5,2)*3
print(params)  

class C:
    print "dddd"

class MemberCounter:
    member=0
    def init(self):
        MemberCounter.member+=1

m1=MemberCounter();
m1.init();
print m1.member
m2=MemberCounter();
m2.init();
print m2.member
print m1.member

m1.member="two"
print m2.member
print m1.member



