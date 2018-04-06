# coding=utf-8


from selenium import webdriver
import time


url = 'http://www.fanfou.com/'

# 创建浏览器对象
driver = webdriver.Chrome()

# 发送请求  访问url
driver.get(url)

# 通过元素定位
# 首先需要进入内部的框架
# el_l = driver.find_element_by_xpath('//*[@id="sidebar"]/div')
# driver.switch_to.frame(el_l)

# 尝试点击帐号密码登录按钮
# el = driver.find_element_by_id('//*[@id="login"]/p[4]/input[3]')
# el.click()
time.sleep(2)

# 输入帐号密码
el_user = driver.find_element_by_xpath('//form[@id="login"]/p/input[@id="loginname"]')
el_user.send_keys('1072022525@qq.com')
el_pwd = driver.find_element_by_xpath('//form[@id="login"]/p/input[@id="loginpass"]')
el_pwd.send_keys('Zx10712.')
time.sleep(2)

# 点击登录
# el_sub = driver.find_element_by_class_name('//input[@class="formbutton""]')
el_sub = driver.find_element_by_xpath('//*[@id="login"]/p[4]/input[3]')
el_sub.click()

# 关闭当前页面，如果只有一个页面，会关闭浏览器
driver.close()

# 关闭浏览器
driver.quit()