# coding:UTF-8
'''
多线程的使用情况
'''

import time
import threading


#创建新线程的代码：
def loop():
    # 获得当前线程的名字
    print('子线程 %s 真正运行 ...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('子线程 %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('子线程 %s ended.' % threading.current_thread().name)


print("主线程 %s 真正运行。。。" % threading.current_thread().name)
#创建了一个线程
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print("主线程 %s 结束" % threading.current_thread().name)

#在多线程中 变量是所有线程公用的，所以就会用到Lock锁住变量
balance = 0


def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(1000):
        change_it(n)


# t2 = threading.Thread(target=run_thread, args=(5, ))
# t3 = threading.Thread(target=run_thread, args=(8, ))
# t2.start()
# t3.start()
# t2.join()
# t3.join()
# print(balance)

#获取锁
lock = threading.Lock()


# 加锁版
def run_threadLock(n):
    for i in range(1000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            #释放锁   一定要释放锁否者会编程死线程的
            lock.release()
t2 = threading.Thread(target=run_threadLock, args=(5, ))
t3 = threading.Thread(target=run_threadLock, args=(8, ))
t2.start()
t3.start()
t2.join()
t3.join()
print(balance)
# 锁的存在会造成效率的降低  也会造成死锁的现象

# class Student(name):
#     def __init__(self,name):
#         self.name=name

# 在多线程中，使用全局变量 修改的时候 必须加锁，局部变量修改方便可以传递給其他线程相对麻烦
# 解决方法就是在全局创建一个dict 以各个线程的名称为key
# 创建全局的ThreadLoacal
local_school=threading.local()

def process_student():
    #获取当前线程
    std=local_school.Student
    print('Hello %s （in %s）' % (std,threading.current_thread().name))

def process_thread(names):
    local_school.Student=names
    process_student()

t4=threading.Thread(target=process_thread,args=("Alice",),name='Thread_a')
t5=threading.Thread(target=process_thread,args=("Bod",),name="thread_b")

t4.start()
t5.start()
t4.join()
t5.join()




