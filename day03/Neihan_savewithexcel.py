import requests
import re
from openpyxl import Workbook

class Neihan(object):

    def __init__(self):
        self.url = 'http://neihanshequ.com/'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"
        }
        self.wk = Workbook()  # 实例化一个工作薄
        self.ws = self.wk.active  # 激活一个工作表

    # 发送请求 获取数据
    def get_data(self):

        response = requests.get(self.url, self.headers)

        content = response.text

        # 使用正则匹配想要的段子数据
        reg = re.compile(r'data-text="(.*?)"')

        jokes_list = reg.findall(content)

        # 返回数据
        return jokes_list

    # 保存 数据
    def save(self, jokes_list):
        # 遍历正则匹配结果，获取分组后的数据
        for jokes in jokes_list:
            print(jokes)
            detail_jokes_list = []
            detail_jokes_list.append(jokes)
            self.ws.append(detail_jokes_list)
            self.ws.title = "内涵"
            self.wk.save("./NeiHanduanzi.xlsx")

    def run(self):
        data = self.get_data()
        self.save(data)


if __name__ == '__main__':
    neihan = Neihan()
    neihan.run()