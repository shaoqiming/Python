# coding:UTF-8
'''
collections是python里面的内建模块 集合类
'''
from collections import namedtuple
#规定了tuple的数量 并且可以用属性而不是索引来应用tuple的某个元素
Point=namedtuple('Point',['x','y'])

p=Point(1,2)
print p.x

# deque list存储数据访问很快，删除和插入元素就很慢
from collections import deque
# 实现了高效的插入和删除的操作，而且是双向列表
q=deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print q

# defaultdict 默认字典
from collections import defaultdict
#给没有key的字典附上一个默认值
dd=defaultdict(lambda:'N/A 没有值')

print dd['wwww']

# OrderedDict 普通的dict是无序的
from collections import OrderedDict
d=dict([('a', 1), ('b', 2), ('c', 3)])
print d
#会按照key的顺序插入 不是值得顺序
od=OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print od

class MyConunter(dict):
    def __init__(self,**kws):
        super(MyConunter,self).__init__(**kws)

    def __setitem__(self, key, value):
        super(MyConunter,self).__setitem__(key,value)
    


#Counter 计数器
from collections import Counter
c=Counter()
c["dd"]=""
for ch in "programming":
    c[ch]=c[ch]+1
print c