# coding=utf-8

import requests

#构造url
url = 'https://www.baidu.com/s?'

#构造请求头
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"
}

# 构造参数
data = {
    'wd': 'python'
}

#发送请求,post请求data，使用params来传入get请求的参数
response = requests.get(url, headers=headers, params=data)
# 响应的状态码
# print(response.status_code)
# # 获取响应的字符串
# print(response.text)

#保存响应的结果，写入文件bytes
with open('baidu.html', 'wb') as f:
    f.write(response.content)