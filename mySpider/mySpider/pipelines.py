# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json


class MyspiderPipeline(object):
    # def process_item(self, item, spider):
    #     return item

    # def __init__(self):
    #     self.file = open('itcast3.json', 'wb')


    # 实现两个方法open_spider/close_spider
    def open_spider(self, item):
        self.file = open('itcast3.json', 'w')

    def process_item(self, item, spider):
        # item是字典形式的对象
        # dict_item = dict(item)
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(content)
        # 返回item给引擎
        return item

    def close_spider(self, item):
        self.file.close()