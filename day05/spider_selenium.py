# coding=utf-8

from selenium import webdriver


if __name__ == '__main__':
    # 打开PhantomJS浏览器
    driver = webdriver.PhantomJS()  # PhantomJS需要先下载，配置环境变量，如果没有配置环境变量，需要使用executable_path参数指定
    # 请求url
    driver.get("http://www.baidu.com")
    # 打印出网页的title
    print(driver.title)  # 输出结果：百度一下，你就知道

    # 保存截图
    driver.save_screenshot("baidu.png")

    # 关闭当前页面，如果只有一个页面，会关闭浏览器
    # driver.close()

    # 关闭浏览器
    driver.quit()