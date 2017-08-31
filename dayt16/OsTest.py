# coding:utf-8

import os
import os.path

print 'dddd'

filename='./temp/test.txt'

if os.path.isfile(filename):
    #追加模式会将不存的文件创建出来？
    f1=open(filename,'a+')
else:
    filnameTruple= os.path.split(filename)
    if filnameTruple[0]=='' or filnameTruple[0]=='./':
        f1=open(filename,'w')
    else:
        os.mkdir(filnameTruple[0])
        f1=open(filename,'w')
    
while True:
    line=raw_input('输入一些信息：')
    if line=='q' or line=='quite':
        break
    
    f1.write(line+'\n')

f1.close()
