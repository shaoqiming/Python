# coding:UTF-8
'''
文件和流
'''
f=open('./shaoqi.txt','w')
f.write("ddddd")
f.write("ssss")
f.close()

f=open('./shaoqi.txt','r')
print f.read(10) 