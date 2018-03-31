#coding=utf-8

import requests
import json
"""
需求：访问金山词霸在线翻译，获取翻译结果
1、构造url
2、请求头
3、构造请求体
4、发送请求，输出数据
"""

class king(object):
    def __init__(self, word):
        self.url = 'http://fy.iciba.com/ajax.php?a=fy'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"
        }
        # 构造请求参数
        self.post_data = {
            "f": "auto",
            "t": "auto",
            "w": word
        }
    # 发送请求
    def request_post(self):
        response = requests.post(url=self.url, headers=self.headers, data=self.post_data)
        return response.content.decode()

    # 解析数据
    def parse_data(self, data):
        # 把响应数据转成字典
        dict_data = json.loads(data)
        # 判断out键是否存在，不能判断一个字符串是否在字典的索引
        # if 'out' in data:
        #     content = (dict_data['content']['out'])
        # else:
        #     content = (dict_data['content']['word_mean'][0])
        # 进行异常处理
        try:
            content = (dict_data['content']['out'])
        except:
            content = (dict_data['content']['word_mean'][0])
        print(content)



    def run(self):
        # 调用发送请求，并获取数据
        data = self.request_post()
        # 调用解析数据方法
        self.parse_data(data)


if __name__ == '__main__':
    import sys
    word = sys.argv[1]
    king = king(word)
    king.run()