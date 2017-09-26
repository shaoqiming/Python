# coding:utf-8

import urllib2
import re
import Tool


class BDTB:

    def __init__(self,baseUrl,seelz):
        self.baseUrl=baseUrl
        self.seeLZ='?see_lz='+str(seelz)
        self.user_agnt = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        self.headers = {'User-Agent': self.user_agnt}
        self.tool=Tool.Tool()
        self.file=None
        self.defaultTitle=u'百度贴吧'

    def getPage(self,pageNum):
        try:
            url=self.baseUrl+self.seeLZ+'&pn='+str(pageNum)
            request=urllib2.Request(url,headers=self.headers)
            response=urllib2.urlopen(request)
            #print response.read()
            return response.read()
        except urllib2.URLError,e:
            if hasattr(e,'reason'):
                print u"链接百度贴吧失败，错误原因",e.reason
                return  None

    def getContent(self,page):
        pattern=re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
        items=re.findall(pattern,page)
        for item in items:
            print "==========================="
            print self.tool.repalce(item)
            print "==========================="

    def getTitle(self):
        pagecode=self.getPage(1)
        pattern=re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>',re.S)
        result=re.search(pattern,pagecode)
        if result:
            print result.group(1).strip()
        else:
            print "没有结果"

    def getPageNum(self):
        pagecode=self.getPage(1)
        pattern=re.compile('<ul class="l_posts_num".*?<span class="red">(.*?)</span>',re.S)
        result=re.search(pattern,pagecode)
        if result:
            print result.group(1)
        else:
            print "没有搜索到页数"

    def setFileTitle(self,title):
        if title is not None:
            self.file=open(title+".txt","w+")
        else:
            self.file=open(self.defaultTitle+".txt","w+")

    def start(self):
        indexPage=self.getPage(1)






baseUrl='https://tieba.baidu.com/p/3138733512'
bdtb=BDTB(baseUrl,1)
pagecode=bdtb.getPage(1)
bdtb.getContent(pagecode)

