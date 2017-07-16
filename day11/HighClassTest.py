# coding:UTF-8
'''
高级函数使用
'''


class Student(object):
    pass


s = Student()
#给实例动态绑定一个name的属性
s.name = "shaoqi"


def set_age(self, age):
    self.age = age

#给类动态添加方法 所有的实例都有该方法  在静态语言钟很难实现 但到动态语言允许我们这样做
Student.set_age=set_age

#__slots__ 可以通过这个函数限制class能添加的属性
class Student1(object):
    __slots__=('name','age')


s1=Student1()
s1.name="shaoqi"
s1.age=12
#会报错 'Student1' object has no attribute 'score'
#s1.score=98

#注意的是__slots__只对当前的实例起作用，对继承的子类是不起作用的

#@property 可以将一个方法编程属性进行调用
class Student2(object):
    def __init__(self,age):
        self._age=age
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError("输入的不是数字，请重新输入！")
        if value<0 or value>100:
            raise ValueError("输入的值超出了范围！")
        self._score=value
    #定义只读属性
    @property
    def age(self):
        return self._age
#@property本事又创建了另一个装饰器 @XXX.setter 可以将方法变成赋值语句
s2=Student2(12)
s2.score=60
print s2.score

#多重继承
class Mammal(object):
    pass

class RunnAble(object):
    pass

#多重继承
class Dog(Mammal,RunnAble):
    pass

#python 内置函数
#__str__
class Student3(object):
    def __init__(self,name):
        self.name=name
    #通过__str__可以指定打印出来的实例
    def __str__(self):
        return "Student object (name :% s)" % self.name
    
#打印出来的是类创建的实例的内存地址 
print (Student3("shaoqi"))

s3=Student3("shaoqi11")
print s3

# 如果想使用for。。in的方法  必须实现 __iter__()的方法
class Fib(object):
    def __init__(self,Max):
        self.a,self.b=0,1
        self._max=Max
    def __iter__(self):
        return self
    #2.7版本的名字为next 3.0版本的为__next__
    def next(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>self._max:
            #退出循环
            raise StopIteration()
        return self.a

    def __getitem__(self,b):
        #索引
        if isinstance(b,int):
            a,b=0,1
            for x in range(n):
                a,b=b,a+b
            return a
        #切片
        if isinstance(b,slice):
            start=b.start
            stop=b.stop
            returndata=[]
            a,b=0,1
            for x in range(stop):
                a,b=b,a+b
                if n>=start:
                    returndata.append(a)
            return returndata
for n in Fib(50):
    print n
    
#__getItem__ 如果想通过索引来获取某个值得话 需要实现和这个方法

print Fib(50)[49]
print Fib(50)[9:15]

class Student4(object):
    def __init__(self,b):
        self.name=b
    #在找不到函数或者属性的情况下会调用__getattribute__
    def __getattribute__(self,atter):
        if atter=='age':
            return 25
    def __call__(self):
        print ('my name is %s'% self.name)

s4=Student4("shaoqi")
print s4.name
print s4.age
print s4()

# 使用枚举值
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name,member in Month.__members__.items():
    print name,'=>',member,',',member.value

#动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的

class Hello(object):
    def hello(self,name='world'):
        print ('Hello ,%s'% name)




