import scrapy
from tutorial.items import DmozItem

class DomzSpider(scrapy.Spider):
    name = 'hitb'
    allowed_domains = ["new.hitb.org"]
    start_urls = [
        "http://news.hitb.org/",
        ]

    def parse(self, response):
        for sel in response.xpath('//*[@div="view-content"]'):
            item=DmozItem()
            item['title'] = sel.xpath('div/article/h2/span/@content').extract()
            #print item['title']
            item['link'] = sel.xpath('div/article/h2/a/@href').extract()
            item['dat'] = sel.xpath(
                'div/article/div[@class="submitted"]/span/@content').extract()
            item['hot'] = sel.xpath(
                'div/article/div[@class="node-links clearfix"]/ul/li[@class="statistics_counter last"]/span/text()').extract()
            item['info'] = sel.xpath(
                'div/article/div[@class="node-content content"]/div/div/div/p[2]/text()').extract()
            #print title,link,desc
            yield item
