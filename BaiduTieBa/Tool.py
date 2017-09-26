# coding:utf-8

import re

class Tool:
    removImage=re.compile('<img.*?>| {7}|')
    removAddr=re.compile('<a.*?>|</a>')
    replace=re.compile('<tr>|<div>|</div>|</p>')
    replaceTD=re.compile('<td>')
    replacePAra=re.compile('<p.*?>')
    replaceBR = re.compile('<br><br>|<br>')
    removExtrarTag=re.compile('<.*?>')
    def repalce(self,x):
        x = re.sub(self.removImage,"",x)
        x = re.sub(self.removAddr,"",x)
        x = re.sub(self.replace,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replacePAra,"\n    ",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removExtrarTag,"",x)
        #strip()将前后多余内容删除
        return x.strip()