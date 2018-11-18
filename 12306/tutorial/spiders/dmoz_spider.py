#-*- coding:UTF-8 -*-
import scrapy
from tutorial.items import DmozItem

class DomzSpider(scrapy.Spider):
    name = '12306'
    allowed_domains = ["baidu.com"]
    start_urls = [

        "https://news.so.com/ns?q=12306黄牛&pq=12306黄牛"
        ]

    def parse(self, response):
        print  "respone",response
        for sel in response.xpath('//div[@id="content_left"]'):
            print  sel.extract()
            item=DmozItem()
            item['title'] = sel.xpath('li/a').extract()
            # baidu title: div[3]/div/h3/a
            # print item['title']
            item['link'] = sel.xpath('li/a/@href').extract()
            # baidu link:div[3]/div/h3/a/@href
            item['info'] = sel.xpath(
                'li/div/span[@class="stname"]').extract()
            # baidu info:div[3]/div/div
            # print title,link,desc
            yield item
