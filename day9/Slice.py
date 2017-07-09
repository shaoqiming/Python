# coding:UTF-8
'''
数组和list的一些高级特性 切片还是很灵活的
'''
L = ['11', '222', '333']

print L[0:3]
print L[:3]  #0可以忽略不写
print L[1:3]  #从第二个开始
print L[:-1]  #从右边开始

#创建一个100的列数
M = list(range(100))
print M

#获取前十
print M[:10]
print M[:-10]
print M[10:20]  #11~20

#还可以添加step 就是隔多少个 取值
print M[:10:2]
print M[::5]
print M[:]  #可以复制一个列表 深复制

print "shaoqi" [:2]

#=================迭代循环================

Lis = list(range(10))
for Li in Lis:
    print(Li)

Lis1 = {'a': 1, 'b': 2, 'c': 3}
for Li in Lis1:
    print Li

for value in Lis1.values():
    print value

for k, v in Lis1.items():
    print k, v

#判断变量是否能被迭代
from collections import Iterable
isinstance(Lis1, Iterable)  #true

#list 是沒有下標的，如果想有下標可以用enumerate函數
'''
会报错
for i,v in Lis:
    print(i,v)
'''

for i, v in enumerate(Lis):
    print i, v

print '+================================='
#当然也可以引用了两个变量
for x, y in [(1, 2), (2, 3), (3, 4)]:
    print x, y

#列表生产器:生产一个list

#这种只能生产出数学的list 而且只能是连续的数子
list(range(10))

#[1*1,2*2,.....N*N]这个应该怎么生产呢？
#笨方法 使用了三行代码
L = []
for x in range(1, 11):
    L.append(x * x)

#列表生成器 只用了一行
print [X * X for X in range(1, 11)]

#还可以在后面加上条件
print [X * X for X in range(1, 11) if X % 2 == 0]

#当然可以使用两循环
print [m + n for m in "ABC" for n in "EFG"]

#也可以对字典进行修改
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print [k + "=" + v for k, v in d.items()]

#练习
L2 = ['Hello', 'World', 18, 'Apple', None]
print [s.lower() for s in L2 if isinstance(s,str)]


#生产器 在循环的时候 再去计算元素 不会一下就将所有的元素生产出来 有点像C#中的Ienumber 懒加载
#创建一个生产器  
g=(x*x for x in range(10))
print g

next(g) #使用next就可以获取下一个值
#生成器保存的是算法 调用next便会去计算下一个值
print '================='
#这是个函数 怎么改造成功生产器呢？
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b #(a,b)=(b,a+b)
        n = n + 1
    return 'done'

def fib1(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b #(a,b)=(b,a+b)
        n = n + 1
    #return 'done'

f=fib1(6)
print f

#杨辉三角
def triangles(n):
    L=[1]
    if(n==1):
        print L
    elif n>1:
        s=[]
        s.append(L)
        time=1
        while time<n:
            temp1=s[len(s)-1]
            temp=[]
            for a in range(0,time):#n=2
                if a==0:
                    temp.append(1)
                elif a==time-1:
                    temp.append(1)
                else:
                    temp.append(temp1[a-1]+temp1[a])
            print temp
            s.append(temp)
            time+=1
#当然这个很复杂
triangles(10)

#来个简单的
def triangle11(n):
    L=[1]
    m=0
    while m<=n:
        yield L
        L=[L[x]+L[x+1] for x in range(len(L)-1)]
        L.insert(0,1)#给前后加上1
        L.append(1)
        m=m+1

a=triangle11(0)
for i in a:
    print(i)