# coding:utf-8

import requests
import re
from openpyxl import Workbook

# openpyxl官方文档：https://openpyxl.readthedocs.io/en/latest/usage.html

class NeiHan(object):

    def __init__(self):

        self.headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"
        }

        self.start_url = "http://neihanshequ.com/"

        self.wk = Workbook()  # 实例化一个工作薄
        self.ws = self.wk.active  # 激活一个工作表


    def parse(self):

        response = requests.get(self.start_url,self.headers)

        content = response.text

        reg = re.compile(r'data-text="(.*?)"')

        jokes_list = reg.findall(content)

        return jokes_list


    def save(self,jokes_list):
        for con in jokes_list:
            print(con)
            detail_list_con = []
            detail_list_con.append(con)
            self.ws.append(detail_list_con)
            self.ws.title = "内涵"
            self.wk.save("./NeiHan.xlsx")


    def run(self):
        con_list = self.parse()
        self.save(con_list)


if __name__ == '__main__':
    neihan=NeiHan()
    neihan.run()

