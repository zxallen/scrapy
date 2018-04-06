# coding=utf-8

from selenium import webdriver

url = 'http://bj.58.com/'

driver = webdriver.Chrome()

driver.get(url)

# 获取当前的url，窗口
print(driver.current_url)
print(driver.window_handles)

# 模拟点击房屋出租
el = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div/div[1]/div[1]/span[1]/a')
el.click()

# 点击房屋出租后，会打开新的标签页，需要传入新打开标签页的索引
driver.switch_to.window(driver.window_handles[-1])
print(driver.current_url)
print(driver.window_handles)

# 定位所有title
node_list = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[5]/div[2]/ul/li/div[2]/h2/a')
for node in node_list:
    print(node.text, node.get_attribute('href'))

driver.close()

driver.quit()