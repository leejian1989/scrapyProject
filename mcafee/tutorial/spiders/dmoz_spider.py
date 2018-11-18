import scrapy
from tutorial.items import DmozItem

class DomzSpider(scrapy.Spider):
    name = 'mcafee'
    allowed_domains = ["mcafee.com"]
    start_urls = [
        "https://securingtomorrow.mcafee.com",
        ]

    def parse(self, response):
        for sel in response.xpath('//main[@id="main"]'):
            item=DmozItem()
            item['title'] = sel.xpath(
                'div[@class="grid-item"]/div[@class="box"]/a[@class="main-link"]/@title'
                                      ).extract()
            #print "title........", item['title']
            item['link'] = sel.xpath(
                'div[@class="grid-item"]/div[@class="box"]/a[@class="main-link"]/@href'
                                     ).extract()
            '''item['dat'] = sel.xpath(
                'div/div[@class="news-info"]/dl/dd/span[@class="time"]/text()').extract()
            item['hot'] = sel.xpath(
                'div/div[@class="news-bot"]/span[@class="look"]/strong/text()').extract()
            item['info'] = sel.xpath(
                'div/div[@class="news-info"]/dl/dd[@class="text"]/text()').extract()'''
            #print title,link,desc
            yield item
