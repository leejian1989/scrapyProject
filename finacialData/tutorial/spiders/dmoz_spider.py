#-*- coding:UTF-8 -*-
import scrapy
from tutorial.items import DmozItem

class DomzSpider(scrapy.Spider):
    name = 'finacial'
    allowed_domains = ["baidu.com"]
    start_urls = [
        u"http://news.so.com/ns?j=0&rank=rank&src=filter_title&tn=newstitle&scq=&q=大数据+金融"

        ]

    def parse(self, response):
        #print "respone:",response
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
