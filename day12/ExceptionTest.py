# coding:UTF-8
# try:
#     print ("try....")
#     r=10/0
#     print ('result:',r)
# except ZeroDivisionError as identifier:
#     print("except:",identifier)
# else:
#     pass
# finally:
#     print ('finally..')

# 所有的错误类型都是继承BaseException

#如何打印出出错的记录呢？ 可以使用内置的logging的函数
import logging 

def foo(s):
    return 10/int(s)

def bar(s):
    return foo(s)*2

def main():
    try:
        bar("0")
    except Exception as e:
        #会将错误信息打印出来 程序还是会继续的允许 通过配置还可以将错误的记录到日志文件里面
        logging.exception(e)
        #可以将错误再次抛出 让更高级的调用者去处理
        #raise
        #也可以用其他的错误去抛出
        #raise ValueError
    
main()
print("END")

print ('================')

#断言  assert
def foo1(s):
    n=int(s)
    #本身就会抛出 AssertionError
    assert n!=0,'n is zero'
    return 10/n

def main1():
    foo1("0")

main1()

print ("=================================")
#单元测试
#TDD：Test-Driven Development 先编写测试用例 然后放到测试模块的中

class Dict(dict):

    def __init__(self,**kw):
        super(Dict,dict).__init__(**kw)

    def __getattribute__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
    def __setattr__(self,key,value):
        self[key]=value

import unittest 

class TestDict(unittest.TestCase):

    def test_init(self):
        d=Dict(a=1,b='test')
        self.assertEqual(d.a,1)
        self.assertEqual(d.b,'test')
        self.assertTrue(isinstance(d,dict))
    
    def test_key(self):
        d=Dict()
        d['key']='value'
        self.assertEqual(d.key,'value')

    def test_atter(self):
        d=Dict()
        d.key='value'
        self.assertTrue('Key' in d)
        self.assertEqual(d['key'],'value')

    def test_keyerror(self):
        d=Dict()
        with self.assertRaises(keyError):
            value=d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty


#文档测试