#-*- coding:UTF-8 -*-
import scrapy
from tutorial.items import DmozItem

class DomzSpider(scrapy.Spider):
    name = 'bankjrj'
    allowed_domains = ["http://bank.jrj.com.cn/"]
    start_urls = [
        u"http://bank.jrj.com.cn/list/hydt.shtml"

        ]

    def parse(self, response):
        #print "respone:",response
        for sel in response.xpath('//div[@class="newlist"]/ul'):
            #print  sel.extract()
            item=DmozItem()
            item['title'] = sel.xpath('li/span/a/text()').extract()
            #baidu title: div[3]/div/h3/a
            #print item['title']
            item['link'] = sel.xpath('li/span/a/@href').extract()
            #baidu link:div[3]/div/h3/a/@href
            #item['info'] = sel.xpath('li/div/span[@class="stname"]').extract()
            item['dat']=sel.xpath('li/i/text()').extract()
            print item['title'],item['link'] ,item['dat']
            yield item
