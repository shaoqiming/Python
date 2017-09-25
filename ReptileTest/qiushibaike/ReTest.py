# coding:utf-8
import re

html='''
<div class="author clearfix">
<a href="/users/20524321/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/2052/20524321/thumb/2016112023330562.JPEG?imageView2/1/w/90/h/90" alt="放我出去我没病..">
</a>
<a href="/users/20524321/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
放我出去我没病..…
</h2>
</a>
<div class="articleGender manIcon">29</div>
</div>

<a href="/article/119577393" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


朋友家一小男孩，今天不小心撞到桌角了，猛哭。<br/><br/>这时他爸出现了，对着孩子一顿骂，说桌子比你更疼，你还好意思哭？<br/><br/>小男孩不哭了，然后就对桌子说对不起。。。。

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">4121</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
'''


##pattern=re.compile('<div.*?author">.*?<div.*?content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S);
pattern=re.compile('<div.*?clearfix">.*?<h2>(.*?)</h2>.*?<div.*?span>(.*?)</span>.*?number">(.*?)</i>',re.S)
items=re.findall(pattern,html)
print items
print str(items[0][0]).strip()
print str(items[0][1]).strip()
print str(items[0][2]).strip()

print "-------------------------"
for item in items:
    print item[0]



