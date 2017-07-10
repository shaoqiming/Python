# coding:UTF-8
import math
#函数也是个变量 变量可以指向函数 并且可以用变量指向 函数名也是个变量 指向函数的变量
print abs

#什么叫高阶函数？ 一个函数可以接收另一个函数作为参数  这个函数就被称为高阶函数

#内建的函数 map和reduce


#map 返回一个新的集合 也是高阶函数
def fx(x):
    return x * x


print map(fx, range(10))

#还可以这样 将数据转换成字符串
print list(map(str, range(10)))


#reduce函数是做累积计算
def add(x, y):
    return x + y


print reduce(add, range(11))


#上面这个列子太简单了下面换个简单点的 将Str的数字转换为int
def fn(x, y):
    return x * 10 + y


def char2num(x):
    return {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
    }[x]


print reduce(fn, map(char2num, '13542'))


#练习
def normalize(name):
    return name[0:1].upper() + name[1:].lower()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


#filter 过滤列表 这个网站上有个比较难得例子 下次补上
def is_odd(n):
    return n % 2 == 1

print list(filter(is_odd, range(10)))

#sorted()

print sorted([36, 5, -12, 9, -21])

#第三个参数是否倒序
print sorted([36, 5, -12, 9, -21], key=abs,reverse=True)

#将函数作为返回值

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 3, 5, 7, 9)
#在调用的时候 才会真正的去计算f的值
print f()

#匿名函数  lambda表达式
list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

#当然可以返回匿名函数
def build(x,y):
    return lambda:x*x+y*y

#装饰器 函数都有个名字
def now():
    print("aaa")

print now.__name__
#如果想增强函数功能，在函数调用的时候 执行一些自定义的操作 但又不想改变函数原有的逻辑

def log(func):
    def warpper(*arge,**Kw):
        print('call %s()' %func.__name__)
        return func(*arge,**Kw)
    return warpper
@log
def now1():
    print("aaa")

now1()
import functools
#如果要在装饰器中添加参数需要在加一层

def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def warpper(*args,**kw):
            print ("%s,%s():"%(text,func.__name__))
            return func(*args,**kw)
        return warpper
    return decorator

@log2("execute")
def now2():
    print("aaa")

now2()

print now2.__name__

#相当为 now2 = log2('execute')(now)


#偏函数 
def int2(x,base=2):
    return int(x,base)

print int2("1010101")

#这个是和上面一样的  调用函数的时候 给指定的参数默认值
sint2 = functools.partial(int, base=2)