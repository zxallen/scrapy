# coding=utf-8

import requests
"""
目标：
爬取百度贴吧页面:
1、构造url
2、构造请求头
3、发送请求
4、保存数据
"""

class Baidu(object):
    def __init__(self, name, pn):
        #保存传入的贴吧名称
        self.name = name
        # kw={}不能写死   kw={}  》》》 format()
        # 1、构造url
        self.url = 'https://tieba.baidu.com/f?kw={}&ie=utf-8&pn='.format(name)
        # 2、构造请求头
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"
        }

        # 构造url列表，拼接的页数
        self.url_list = [self.url + str(pn*50) for pn in range(pn)]
        print(self.url_list)


    # 发送请求获取数据,需要修改传入的url
    def get_data(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content

    # 保存数据
    def save_data(self, data, num):
        # 构造保存数据的文件名称
        file_name = self.name + '_' + str(num) + '.html'
        with open(file_name, 'wb') as f:
            f.write(data)

    # 执行方法
    def run(self):
        # 遍历前面构造的url列表
        for url in self.url_list:
            # print (url)
            # 调用发送请求的方法，获取数据
            data = self.get_data(url)
            # 获取self.url_list索引值
            num = self.url_list.index(url)
            # 调用保存数据的方法
            self.save_data(data, num)


import sys

if __name__ == '__main__':
    # 传入参数，贴吧名称，页数
    name = sys.argv[1]
    pn = int(sys.argv[2])
    # print(type(name))
    # print(type(pn))
    # print(name,pn)
    baidu = Baidu(name, pn)
    baidu.run()