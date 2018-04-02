# coding:utf-8


import requests
import re
import json


"""
网站  内涵段子
<a target="_blank" class="image share_url" href="（.*?)" .*?<p>(.*?)</p>

"""

class Neihan(object):

    def __init__(self):
        self.url = 'http://neihanshequ.com/'
        self.ajax_url = 'http://neihanshequ.com/joke/?'
        self.headers = {
         "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"
        }
        # 创建问家对象
        self.file = open('neihan.json', 'w', encoding='utf8')


    # 发送请求
    def get_data(self, url, params=None, headers=None):
        if params is None:
            response = requests.get(url, headers=self.headers)
        else:
            response = requests.get(url, headers=headers, params=params)
        return response.content.decode()


    # 解析首页数据,
    def parse_data(self, data):
        # 使用正则匹配想要的段子数据
        result_list = re.findall('<a target="_blank" class="image share_url" href="(.*?)" .*?<p>(.*?)</p>', data, re.S)
        # print(result_list)
        data_list = []
        # 遍历正则匹配结果，获取分组后的数据
        for result in result_list:
            temp = {}
            temp['url'] = result[0]
            temp['content'] = result[1]
            data_list.append(temp)
        # 获取时间戳
        max_time = re.findall("max_time: '(\d+)'", data)[0]
        return data_list, max_time

    # 解析ajax数据
    def parse_ajax_data(self, data_list):
        # 转成字典
        dict_data = json.loads(data_list)
        # print(dict_data)
        result_list = dict_data['data']['data']
        data_list = []
        for result in result_list:
            temp = {}
            temp['url'] = result['group']['share_url']
            temp['content'] = result['group']['content']
            # print(temp)
            data_list.append(temp)
        # 获取时间戳
        max_time = dict_data['data']['max_time']
        # print(max_time)
        return data_list, max_time


    def save_data(self, data_list):
        for data in data_list:
            dict_data = json.dumps(data, ensure_ascii=False) + ',\n'
            self.file.write(dict_data)
            # print(dict_data)

    # 关闭文件
    def __del__(self):
        self.file.close()

    def run(self):
        data = self.get_data(self.url)
        # 解析数据,获取下一页的时间戳
        data_list, max_time = self.parse_data(data)
        self.save_data(data_list)
        while True:
            # 构造请求下一页的参数
            params = {
                "is_json": "1",
                "app_name": "neihanshequ_web",
                "max_time": max_time
            }
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"
                'Cookie: csrftoken=8d83f69982ff7449a7a4794380d0eb15; tt_webid=6539672804715218436; uuid="w:2e574805544f470aa04492bfa77f848e"; _ga=GA1.2.1981516041.1522636295; _gid=GA1.2.1283588988.1522636295; _gat=1'
            }
            data_lists = self.get_data(self.ajax_url, params=params, headers=headers)
            data_list, max_time = self.parse_ajax_data(data_lists)
            self.save_data(data_list)

            if len(data_list) is 0:
                break


if __name__ == '__main__':
    neihan = Neihan()
    neihan.run()