#引入模块

import urllib
import http.cookiejar
import re
import os
import sys


#基础链接
url = "https://www.bing.com"


herders = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
}


#获取图片方法
def getBingImage(weburl):

#获取网页内容，等同于浏览器打开www.bing.com 后右键保存文件
response = urllib.request.urlopen(weburl,timeout=10)

html = response.read()

s = str(html)



#搜索图片链接地址，g_img={url 这部分就是上面记事本搜索得到的，可以根据实际情况调整，jpg是图片
#格式，也可根据实际情况调整，后面同理
restr = re.compile('g_img={url.+?jpg')

res = restr.search(s).group()

print(res)

urlPattern = re.compile('/w+.+jpg')

fileNamePattern = re.compile('[a-zA-Z0-9_-]+.jpg')

finalUrl = urlPattern.search(res).group()

print(finalUrl)


#搜索得到图片文件名称
fileName = fileNamePattern.search(finalUrl).group()

print(fileName)

fileNamePattern = re.compile('[a-zA-Z0-9]+')

fileName = fileNamePattern.search(fileName).group()

fileName = fileName + '.jpg'

print(fileName)

jpgUrl = url + finalUrl

jpgRes = urllib.request.urlopen(jpgUrl,timeout=10)

print(jpgUrl)


#图片数据获取和保存
jpgData = jpgRes.read()

path = os.getcwd()

filepath = path + '\'+fileName

fp = open(filepath,'wb')

fp.write(jpgData)

fp.flush()

fp.close()

cnUrl = 'https://www.bing.com'

enUrl = 'https://www.bing.com/?ensearch=1'

getBingImage(cnUrl)

getBingImage(enUrl)