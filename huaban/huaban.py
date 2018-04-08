#coding:utf-8

import requests
import os
import lxml.html
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


#创建浏览器对象
# browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)  #WebDriverWait标明最大等待浏览器加载为10秒，
browser.set_window_size(1400, 900)  #set_window_size可以设置一下模拟浏览网页的大小。有些网站如果大小不到位，那么一些资源就不加载出来。



# 解析网页
def parser(url, param):
    browser.get(url)
    wait.until(EC.presence_of_element_located(By.CSS_SELECTOR, param))
    html = browser.page_source
    doc = lxml.html.fromstring(html)
    return doc


# 解析数据， 解析本次主页面http://huaban.com/boards/favorite/beauty/ 然后获取到每个栏目的网址和栏目的名称，使用xpath来获取栏目的网页
def get_main_url():
    print('打开主页收寻链接中...')
    try:
        doc = parser('http://huaban.com/boards/favorite/beauty/', '#waterfall')
        name = doc.xpath('')