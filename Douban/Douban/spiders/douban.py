# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Douban.items import DoubanItem


class DoubanSpider(CrawlSpider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250?start=0&filter=']

    rules = (
        # 指定url匹配规则   start=0&filter=
        Rule(LinkExtractor(allow=r'start=\d+&filter='), callback='parse_item'),
    )

    def parse_item(self, response):

        # print(response.url)

        node_list = response.xpath('//div[@class="info"]')

        for node in node_list:
            item = DoubanItem()
            item['name'] = node.xpath('./div[1]/a/span[1]/text()').extract_first()
            item['score'] = node.xpath('./div[2]/div/span[2]/text()').extract_first()
            item['info'] = node.xpath('./div[2]/p[1]/text()').extract_first().replace('\xa0', ' ').strip()
            # item['info'] = node.xpath('./div[2]/p[1]/text()').extract_first().replace('\xa0','').strip()

            item['desc'] = node.xpath('./div[2]/p[2]/span/text()').extract_first()
            # print(item)
            yield item