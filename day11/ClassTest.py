# coding:UTF-8

# 表示是从object继承 
class Student(object):
    pass

bart=Student()

# 后面是内存地址
print bart

# 可以在类上面绑定属性
bart.name='shaoqi'
print bart.name


class Student1(object):
# 在类中定义的方法的第一个参数是self 表示实例的本身。
    def __init__(self,name,score):
        self.name=name
        self.score=score
    
    def print_score(self):
        print ("%s:%s"%(self.name,self.score))

demo1=Student1("shaoqi1",12)
demo1.print_score()

print demo1.name,demo1.score

#访问限制 

# 通过给属性添加__来限定属性的访问限制
class Student2(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    
    def print_score(self):
         print ("%s:%s"%(self.__name,self.__score))


demo2=Student2("shaoqi",55)
print ("======")
demo2.print_score()
#其实还是可以通过 类的名字加属性的名称进行访问的
#版本不同 改成的名字也不一样
print  demo2._Student2__name

#继承和多态
class Animal(object):
    def run(self):
        print ('Animal is runing....')

class Dog(Animal):
    pass
#子类的方法和父类的方法相同时 子类的方法会覆盖父类的方法
class Cat(Animal):
    def run(self):
        print('cat is runing....')

cat=Cat()
cat.run()

# 动态的语言就是 “鸭子类型”  python就是动态语言 net为静态语言

# 获取对象信 type 返回的Class的类型
print type(123)
print type(abs)#方法

# isinstance() 可以判断继承关系  后面可以写两个
isinstance([1,2,3],(list,tuple))

# dir的可以获得所有的属性和方法
print dir('ABC')# str里面的所有方法和属性


#举个例子 __len__ 方法 在len()的内部其实调用了对象本身的__len__()的方法
class MyDog(object):
    #重写 或者是 创建了一个__len__方法。len()调用
    def __len__(self):
        return 100

dog=MyDog()
print len(dog)# 输出100





