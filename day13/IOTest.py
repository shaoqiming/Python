# coding:UTF-8
import os

print os.name  #NT
print os.environ #环境变量

#操作文件和目录
#当前的绝对路径
print os.path.abspath('.')

print os.path.join('e:\python', 'testdir')

#print os.makedirs(os.path.join('e:\python', 'testdir'))

#print os.rmdir(os.path.join('e:\python', 'testdir'))

#序列化
import json
d=dict(name='Bob', age=20, score=88)
print json.dumps(d)

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print json.loads(json_str)

class Students(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    
s=Students('Bod',13,33)


def student2dict(stb):
    return {
        'name':stb.name,
        'age':stb.age,
        'score':stb.score
    }

print (json.dumps(s,default=student2dict))

#无须定义方法
print (json.dumps(s,default=lambda obj:obj.__dict__))
print ('====================')
#反序列话
def dict2student(d):
    return Students(d['name'],d['age'],d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))