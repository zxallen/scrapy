import requests
import json
import re

"""
目标：36kr网站数据

"""

class Kr36(object):

    def __init__(self):
        self.url = 'http://36kr.com/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
        }
        self.file = open('kr36-1.json', 'w', encoding='utf8')


    def get_data(self):
        response = requests.get(url=self.url, headers=self.headers)
        return response.content.decode()


    def parse_data(self, data):
        # with open('36kr.json', 'w') as f:
        #     f.write(data)
        result = re.findall('<script>var props=(.*?)</script>', data, re.S)[0]
        result_list = re.sub(',locationnal={.*', '', result)
        # print(result_list)
        # with open('36kr.json', 'w') as f:
        #     f.write(result_list)

        # 那个数据转化为字典
        dict_data = json.loads(result_list)['feedPostsLatest|post']

        data_list = []
        for data in dict_data:
            temp = {}
            temp['cover'] = data['cover']
            temp['title'] = data['title']
            data_list.append(temp)
        # 返回结果
        return data_list


    def save_data(self, data_list):
        for data in data_list:
            str_data = json.dumps(data, ensure_ascii=False) + ',\n'
            self.file.write(str_data)


    def __del__(self):
        self.file.close()


    def run(self):
        data = self.get_data()
        data_list = self.parse_data(data)
        self.save_data(data_list)



if __name__ == '__main__':
    Kr36 = Kr36()
    Kr36.run()