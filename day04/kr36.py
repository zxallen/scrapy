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

    def get_data(self):
        response = requests.get(url=self.url, headers=self.headers)
        return response.content.decode()


    def parse_data(self, data):
        with open('36kr.json', 'w') as f:
            f.write(data)



    def run(self):
        data = self.get_data()
        self.parse_data(data)

        pass


if __name__ == '__main__':
    Kr36 = Kr36()
    Kr36.run()