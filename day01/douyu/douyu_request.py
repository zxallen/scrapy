# coding:utf-8

# 先导出requests模块
# 写出headers和start_url
# 通过requests模块获得开始页面的html文本
# 通过正则匹配html文本文件，获得我们要爬去的文件内容
# 转换得到的文件，进行保存

import requests, re, time


headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
}

start_url = "https://www.douyu.com/directory/game/yz"

response = requests.get(start_url, headers)
# 访问response响应对象有三种方法：text 一般是文本
#                            content 以字节的方式访问响应对象，遇到图片的时候，我们可以使用
#                            json 它是requests内置的json解码器，将json字符串解码成字典


# 通过text得到文本
response = response.text
print(response)

# 正则很重要，所以大家忘了的或者不熟悉的，记得去复习
reg = r'data-original="(.+?\.jpg)"'

# re中的compile函数不熟悉的看这个网址   https://www.cnblogs.com/nomorewzx/p/4203829.html
imgpic = re.compile(reg)

# imppic对象不能和search和match一起使用，可以和findall一起使用

pic_url_list = re.findall(imgpic, response)

# 通过遍历图片地址列表，获取每个图片的地址
for pic_url in pic_url_list:
    pic = requests.get(pic_url, headers)
    pic = pic.content
    # 为了保证所有的图片名字不冲突，我们使用time.time()生成的浮点型时间戳来代替名字
    pic_name = '%f.jpg' % time.time()
    with open("yanzhi/" + pic_name, "wb") as f:
        print(pic_name)
        f.write(pic)

print("下载完成，请查看～～～")


