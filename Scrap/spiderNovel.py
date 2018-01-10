#encoding:utf-8
import urllib, urllib2, os
import re

def getNovelListUrl():
    html = urllib.urlopen('http://www.quanshuwang.com/list/1_1.html').read().decode('gbk').encode('utf-8')
    reg = r'<a target="_blank" title=".*?" href="(.*?)" class="clearfix stitle">.*?</a>作者：<a href=".*?">.*?</a>'
    urlList = re.findall(reg, html)
    return urlList

def getChapterList(url):
    html = urllib.urlopen(url).read().decode('gbk').encode('utf-8')
    reg = r'<a href="(.*?)"  class="l mr11">'
    chapterUrl = re.findall(reg, html)
    # print(chapterUrl)
    html1 = urllib.urlopen(chapterUrl[0]).read().decode('gbk').encode('utf-8')
    reg = r'<li><a href="(.*?)" title=".*?">.*?</a></li>'
    chapterList = re.findall(reg, html1)
    # print(chapterList)
    return chapterList

def getContentList(url):
    html = urllib.urlopen(url).read().decode('gbk').encode('utf-8')
    reg = r'<script type="text/javascript">style5\(\);</script>(.*?)<script type="text/javascript">'
    reg = re.compile(reg, re.S)
    contentList = re.findall(reg, html)[0]
    return contentList

def download(dir, content):
    # if not os.path.isdir(dir):
    #     os.mkdir(dir)
    f = open(dir, 'a')
    f.write(content)

for novel in getNovelListUrl():
    for chapter in getChapterList(novel):
        content = getContentList(chapter)
        dir = 'D:/Imgs/content.txt'
        download(dir, content.replace('&nbsp;', ' ').replace('<br />', ''))
print("写入完成！")