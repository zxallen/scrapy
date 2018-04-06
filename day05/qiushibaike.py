import requests
from lxml import etree
import json


class Qiushi(object):

    def __init__(self):
        self.url = 'https://www.qiushibaike.com/8hr/page/{}/'
        self.url_list = None
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
        }
        self.file = open('qiushi.json', 'w')

    # 定义方法，用来生成url列表
    def generate_url_list(self):
        # 使用列表推导式生成url列表
        # 总共  13 页   for i in range(1, 4)
        self.url_list = [self.url.format(i) for i in range(1, 14)]
        print(self.url_list)

    # 发送请求
    def get_data(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content

    # 解析数据
    def parse_data(self, data):
        # 实例化etree 对象
        html = etree.HTML(data)
        # 提取响应数据的节点列表
        node_list = html.xpath('//*[contains(@id, "qiushi_tag_")]')
        # print(len(node_list))
        data_list = []
        # 遍历节点列表
        for node in node_list:
            temp = {}
            # 存储用户名信息
            try:
                # strip去除字符串边的不可见字符
                temp['user'] = node.xpath('./div[1]/a[2]/h2/text()')[0].strip()
                # 存储户用户的个人空间链接
                temp['link'] = 'https://www.qiushibaike.com/' + node.xpath('./div[1]/a[2]/h2/@href')[0]
                # 存储用户的性别,包含在div的class属性中，需要进行字符串的处理
                temp['gender'] = node.xpath('./div[1]/div/@class')[0].split(' ')[-1].replace('Icon',' ')
                # 存储用户的年龄
                temp['age'] = node.xpath('./div[1]/div/text()')[0]
            except:
                temp['usr'] = '匿名用户'
                temp['link'] = None
                temp['gender'] = None
                temp['age'] = None
            data_list.append(temp)
        # 返回数据
        return data_list

    # 保存数据
    def save_data(self, data_list):
        for data in data_list:
            str_data = json.dumps(data, ensure_ascii=False) + '.\n'
            self.file.write(str_data)

    def __del__(self):
        self.file.close()

    def run(self):
        # 构造请求url和请求头
        # 生成url 列表
        self.generate_url_list()
        # 循环执行发送请求，传入生成的url列表中的具体页数
        for url in self.url_list:
            # 发送请求  获取响应
            data = self.get_data(url)
            # 解析数据
            data_list = self.parse_data(data)
            # 保存数据，如果相应数据是json字符串，想要获取指定数据的时候，一般需要转成字典，提取数据
            self.save_data(data_list)
        pass


if __name__ == '__main__':
    qiushi = Qiushi()
    qiushi.run()