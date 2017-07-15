# coding:UTF-8

'a test module'

__author__='shaoqi'

import sys

def test():
    args=sys.argv
    if len(args)==1:
        print("Hello world!!")
    elif  len(args)==2:
        print('Hello %s！' %args[1])
        pass
    else:
        print('Too many argument！！')

# 判断是不是当做第三方的模块进行导入的 如果是的话 就返回false
if __name__=='__mian__':
    test()