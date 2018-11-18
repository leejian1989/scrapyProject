#-*- coding:UTF-8 -*-
import scrapy
from tutorial.items import DmozItem

class DomzSpider(scrapy.Spider):
    name = 'cheat'
    allowed_domains = ["baidu.com"]
    start_urls = [
        u"http://news.so.com/ns?q=电信诈骗&pq=大数据+金融&rank=rank&src=srp&tn=newstitle"
        ]

    def parse(self, response):
        for sel in response.xpath('//div[@class="result_wrap"]/ul'):
            #print  sel.extract()
            item=DmozItem()
            item['title'] = sel.xpath('li/a').extract()
            #baidu title: div[3]/div/h3/a
            #print item['title']
            item['link'] = sel.xpath('li/a/@href').extract()
            #baidu link:div[3]/div/h3/a/@href
            item['info'] = sel.xpath(
                'li/div/span[@class="stname"]').extract()
            #baidu info:div[3]/div/div
            #print title,link,desc
            yield item
