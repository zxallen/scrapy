# -*- coding: utf-8 -*-
import scrapy
# 导入模型item
from mySpider.items import ItcastItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ["http://www.itcast.cn/channel/teacher.shtml"]

    def parse(self, response):
        # with open("teacher.html", "w") as f:
        #     f.write(response.text)

        node_list = response.xpath('//div[@class="li_txt"]')

        # items = []
        for node in node_list:
            # 将我们得到的数据封装到一个 `ItcastItem` 对象
            item = ItcastItem()
            # 提取响应数据中的字符串，本质上进行序列化unicode字符串
            # extract()方法返回的都是unicode字符串
            # xpath返回的是包含一个元素的列表    下标取值0
            item['name'] = node.xpath('./h3/text()').extract()[0]
            item['title'] = node.xpath('./h4/text()').extract()[0]
            item['desc'] = node.xpath('./p/text()').extract()[0]
            # print(temp)
            # data_list.append(temp)
            #生成器返回数据，当有列表页面或详情页面，需要再次发送请求进行下载等操作，需要使用yield
            yield item  # 使用生成器
        # 返回数据
        # return data_list
