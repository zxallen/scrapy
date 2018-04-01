import requests
import re
"""
使用cookie进行模拟登录
1、首先使用浏览器登录网站
2、获取cookie信息
3、保存cookie信息放到请求头中
"""
# 登录后用户信息页
url = 'http://www.renren.com/963112933'

# 构造请求头（保存cookie信息)
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
}

# 临时存储cookie信息
temp = 'anonymid=jf9n8n50xoknmp; depovince=BJ; _r01_=1; ln_uact=18949599846; ln_hurl=http://hdn.xnimg.cn/photos/hdn121/20180111/1930/h_main_TKoW_53900007f6ef1986.jpg; JSESSIONID=abc8gieV_FfurcjIQfXjw; ick_login=8026bf2c-8754-4c63-9929-ce84eb34269d; jebe_key=1a4e5c26-e2c6-4077-bb17-1d88cc271315%7C42420105704af4678321d141b5f75e18%7C1522154103573%7C1%7C1522315734563; first_login_flag=1; ch_id=10016; wp_fold=0; jebecookies=df6b8e51-0382-4365-88aa-abe8d29beda3|||||; _de=FD7D4EEB60D449F2FF8D98007282E0DA; p=32a9f56b781a4ccb437111f9e570520d3; t=c912235379f917a00f82c18581a9cdb33; societyguester=c912235379f917a00f82c18581a9cdb33; id=963112933; xnsid=8edec054; ver=7.0; loginfrom=null'

cookie = {}
# 字符串切割，获取cookie信息
for i in temp.split('; '):
    cookie[i.split('=')[0]] = i.split('=')[-1]

print(cookie)


# 发送请求,利用requests模块中的cookies参数，来指定传入的cookie信息
response = requests.get(url, headers=headers, cookies=cookie)

# 获取响应,并且解码成str,使用正则获取响应中的字符串
print(re.findall('风雨', response.content.decode()))
print(response.status_code)


