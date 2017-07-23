# coding:UTF-8
'''
正则表达式的简单使用
'''
# re模块在python中便可以使用正则表达式 使用r 就不需要转义了。
import re
print re.match(r'^\d{3}\-\d{3,8}$','010-12345')

#可以进行分组
m= re.match(r'^(\d{3})-(\d{3,8})$','010-12345')
print m.group(0)
print m.group(1)
print m.group(2)
print m.group()

#避免贪婪模式的的方法 可以在正则表达式后面加？

#可以预编译正则表达式
#上面就是预编译的
re_telephone=re.compile(r'^(\d{3})-(\d{3,8})$')

re_telephone.match('101-22222').group()


