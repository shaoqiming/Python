# coding:UTF-8
import math
#系统内置函数
print abs(-1)

# 会报错，因为参数的数量不
# abs(1,2)

#数据类型转化
print int('123')
#报错：无效的文字
#print int('12.34')
print int(12.34)
print float('12.34')

print str(12.3)
print bool(2)
print bool("")

#当然 可以将函数付给一个对象
a = abs
print a(-1)

#练习 将一个整数转化成十六进制的字符串
print str(hex(2))

# 定义函数
print('-----定义函数--------')


def my_abs(x):
    if x > 0:
        return x
    else:
        #pass #什么都不做 可以当做一个占位符
        return -x


print my_abs(-2)


# 参数检查
def my_abs1(x):
    if not isinstance(x, (int, float)):
        raise TypeError("错误类型")
    if x > 0:
        return x
    else:
        return -x

# my_abs1("ddd")


# 返回多个值
def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny

#其实返回的是一个tuple 元组
print move(100,100,60,math.pi/6)


#练习
def quadratic(a,b,c):
    if not isinstance(a,(int,float)):
       raise TypeError("错误类型")
    if not isinstance(b,(int,float)):
       raise TypeError("错误类型")
    if not isinstance(c,(int,float)):
       raise TypeError("错误类型")
    e=b**2-4*a*c
    if e<0:
        return '无解'
    elif  e==0:
        return -b/2*a
    else:
        x1=(math.sqrt(e)-b)/(2*a)
        x2=(-math.sqrt(e)-b)/(2*a)
        return x1,x2

print quadratic(2,3,1)
print quadratic(1,3,-4)