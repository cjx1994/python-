#coding=utf-8
import re
import urllib
import urllib.request

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read().decode("GBK")
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x =0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1
    
   
html = getHtml("http://www.jiayu.net/thread-357684-1-1.html")
print(html)
