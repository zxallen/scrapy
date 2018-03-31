# coding=utf-8

import requests


url = 'http://www.zhihu.com/'

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"
}

response = requests.get(url, headers=headers)

print(response.text)   #输出数据

# #输出相应状态码   zhihu.com-------500（不是真实的）  >>>>>>   fanfou.com------200
print(response.status_code)
