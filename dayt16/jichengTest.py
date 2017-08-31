# coding:utf-8

class parent():
    name='parent'
    def setAge(self,age):
        self.age=age
    def saySomething(self):
        print('Im parent!')


class parent1():
    name='parent'
    def setAge(self,age):
        self.age=age
    def saySomething(self):
        print('Im parent1!')


class childer(parent1,parent):
    pass

p1=parent()
p2=parent1()
c1=childer()


p1.saySomething()
p2.saySomething()
c1.saySomething()




