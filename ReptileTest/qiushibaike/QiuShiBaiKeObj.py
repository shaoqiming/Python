# coding:utf-8
__author__ = 'shaoqi'

import urllib2
import re
import os.path


class QSBK:
    def __init__(self):
        self.pageIndex = 1
        self.user_agnt = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        # 初始化headers
        self.headers = {'User-Agent': self.user_agnt}
        self.stories = []
        self.enadle = False

    def getPage(self, pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(self.pageIndex)
            request = urllib2.Request(url, headers=self.headers)
            response = urllib2.urlopen(request)
            pageCode = response.read().decode('utf-8')
            return pageCode
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"链接糗事百科失败，错误原因：", e.reason
                return None

    def getPageItems(self, pageIndex):
        pagecode = self.getPage(pageIndex)
        if not pagecode:
            print "页面读取失败"
            return None
        pattern = re.compile('<div.*?clearfix">.*?<h2>(.*?)</h2>.*?<div.*?span>(.*?)</span>.*?number">(.*?)</i>', re.S)
        items = re.findall(pattern, pagecode)
        pageStories = []

        for item in items:
            repalceBR = re.compile('<br/>')
            text = re.sub(repalceBR, "\n", item[1])
            pageStories.append([item[0].strip(), text.strip(), item[2].strip()])

        return pageStories

    def LoadPage(self):
        if self.enadle==True:

            if len(self.stories)<1 or len(self.stories[0])<2:
                pageStories=self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex+=1

    def getOneStrory(self,pageStories,page):
        for story in pageStories:
            input=raw_input()
            self.LoadPage()
            if input=="Q":
                self.enadle=False
                return
            # 可以记录到文本文件中
            print "---------------"
            self.SaveFile(u"第%d页\t发布人:%s\t\t赞:%s\n%s" %(page,story[0],story[2],story[1]))
            print "======"
            print u"第%d页\t发布人:%s\t\t赞:%s\n%s" %(page,story[0],story[2],story[1])

    def start(self):
        print u"正在读取糗事百科,按回车查看新段子，Q退出"
        self.enadle=True
        self.LoadPage()
        nowpage=0
        while self.enadle:
            if len(self.stories[0])>0:
                pageStories = self.stories[0]
                nowpage+=1
                del self.stories[0][0]
                self.getOneStrory(pageStories,nowpage)

    #保存文件
    def SaveFile(self,*arg):
        filename = './temp/test.txt'
        if os.path.isfile(filename):
            # 追加模式会将不存的文件创建出来？
            f1 = open(filename, 'a+')
        else:
            filnameTruple = os.path.split(filename)
            if filnameTruple[0] == '' or filnameTruple[0] == './':
                f1 = open(filename, 'w')
            else:
                os.mkdir(filnameTruple[0])
                f1 = open(filename, 'w')
        f1.write(arg[0].encode('utf-8') + '\n')
        f1.write('\n')
        f1.close();


sprider=QSBK()
sprider.start()