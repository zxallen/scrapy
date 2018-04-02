import requests
import json

"""
目标：
爬取豆瓣网电视信息
1、电视名称、封面信息、评分等
"""


class Douban(object):

    def __init__(self):
        # self.url = 'https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%BE%8E%E5%89%A7&sort=recommend&page_limit=20&page_start=1'
        self.url = 'https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=200&page_start=1'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
        }
        # 创建文件对象
        self.file = open('douban.json', 'w', encoding='utf8')

     # 发送请求， 获取数据
    def get_data(self):
        response = requests.get(url=self.url, headers=self.headers)
        # 把响应数据转成str类型
        return response.content.decode()


    # 解析数据
    def parse_data(self, data):
        dict_data = json.loads(data)  # 把电影数据转成字典
        result_list = dict_data['subjects']
        data_list = []
        # 遍历获取电视列表
        for result in result_list:
            temp = {}
            temp['title'] = result['title']
            temp['rate'] = result['rate']
            temp['url'] = result['url']
            data_list.append(temp)
        # 返回数据列表
        return data_list


    # 保存 数据
    def save_data(self, data_list):
        # 遍历列表
        for data in data_list:
            # 转成json字符串   ensure_ascii=False解决中文乱码问题
            str_data = json.dumps(data, ensure_ascii=False) + ',\n'
            # 写入文件
            self.file.write(str_data)


    # 关闭文件
    def __del__(self):
        self.file.close()

    # 启动
    def run(self):
        data = self.get_data()  # 发送请求
        data_list = self.parse_data(data)   # 解析数据
        self.save_data(data_list)


if __name__ == '__main__':
    douban = Douban()
    douban.run()