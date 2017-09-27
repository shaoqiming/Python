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
        content=[]
        for item in items:
            content.append(("\n"+self.tool.repalce(item)+"\n"))
        return content

    def getTitle(self,pagecode):
        #pagecode=self.getPage(1)
        pattern=re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>',re.S)
        result=re.search(pattern,pagecode)
        if result:
            print result.group(1).strip()
            return result.group(1).strip().decode("utf-8")
        else:
            print "没有结果"

    def getPageNum(self,pagecode):
        #pagecode=self.getPage(1)
        pattern=re.compile('<ul class="l_posts_num".*?<span class="red">(.*?)</span>',re.S)
        result=re.search(pattern,pagecode)
        if result:
            print result.group(1)
            return  result.group(1)
        else:
            print "没有搜索到页数"


    def setFileTitle(self,title):
        if title is not None:
            self.file=open(title+".txt","w+")
        else:
            self.file=open(self.defaultTitle+".txt","w+")

    def writerData(self,content):
        for i in content:
            self.file.write(i)


    def start(self):
        indexPage=self.getPage(1)
        pageNum=self.getPageNum(indexPage)
        title=self.getTitle(indexPage)
        self.setFileTitle(title)
        if  pageNum==None:
            print "URL已经失效，请重试"
            return
        else:
            try:
                print "该帖子共有"+str(pageNum)+"页"
                for i in range(1,int(pageNum)+1):
                    print "正在写入第"+str(i)+"页"
                    page=self.getPage(i)
                    content=self.getContent(page)
                    self.writerData(content)
            except IOError,e:
                print "写入异常，原因："+e.message
            finally:
                self.file.close()
                print "写入完成"


baseUrl='https://tieba.baidu.com/p/3138733512'

bdtb=BDTB(baseUrl,1)
bdtb.start()
