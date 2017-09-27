# coding:utf-8
import urllib2
import re
import os

class TaoMM:

    def __init__(self):
        self.url='https://mm.taobao.com/json/request_top_list.htm'
        self.page=1
        self.user_agnt = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        # 初始化headers
        self.headers = {'User-Agent': self.user_agnt}

    def getPage(self):
        url=self.url+"?page="+str(self.page)
        print url
        request=urllib2.Request(url,headers=self.headers)
        respone=urllib2.urlopen(request)
        return respone.read().decode('gbk')

    def getContent(self,pageContent):
        pattern = re.compile(
            '<div class="list-item.*?s60.*?<a href="(.*?)".*?<img src="(.*?)".*?</a>.*?_blank">(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',
            re.S)
        items=re.findall(pattern,pageContent)
        for item in items:
            print item[0],'++++++',item[1],item[2],item[3],item[4]

    def SaveImage(self,content,name):
        fileName=name+"/"+name+"txt"
        f=open(fileName,"w+")
        print u"正在保存她的个人信息,文件路径为",fileName
        f.write(content)

    #只创建目录
    def mkdir(self,path):
        path=path.strip()
        #判断文件是否存在
        isExists=os.path.exists(path)
        if not isExists:
            #不存在
            os.makedirs(path)
            return True
        else:
            #目录存在
            return  False


mm=TaoMM()
content=mm.getPage()
mm.getContent(content)



