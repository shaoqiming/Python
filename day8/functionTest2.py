# coding:UTF-8

#函数参数 还可以添加默认值
def powers( x,n=6):
    s=1
    while n>0:
        n-=1
        s=s*x
    return s

print powers(2,10)
def add_end(L=[]):
        L.append('End')
        return L

print add_end()
# 会输出两个End 因为默认参数也是个变量 当第一次调用的时候 L便被初始化了然后便指向了[]
print add_end()


# 这样就不会出现上面的情况了
def add_end1(L=None):
    if L is None:
        L=[]
    L.append("End")
    return L


#可变参数
def calc(*numbers):
    sum=0
    for n in numbers:
        sum+=n
    return sum

s=[1,2,3]
# 数组传参简便方法
print calc(*s)


#关键字参数 在最后的关键字可以输入任何的参数
def person(name,age,**kw):
    print('name:',name,'age:',age,'other',kw)

person('Adam', 45, gender='M', job='Engineer')

# 命名关键字参数   如果要限制关键字
# def person1(name,age,*,name,city):
#     print(name,age,city)

#递归函数 汗诺塔
steps=[]

def move(n,A,B,C): 
    if n==1:
        step=A+'-->'+C
        steps.append(step)
    else:
        move(n-1,A,C,B)
        step=A+'-->'+C
        steps.append(step)
        move(n-1,B,A,C)

move(3,"A","B","C")

for step in steps:  
    print (step)


