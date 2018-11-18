import scrapy
from tutorial.items import DmozItem

class DomzSpider(scrapy.Spider):
    name = 'freebuf'
    allowed_domains = ["freebuf.com"]
    start_urls = [
        "http://www.freebuf.com",
        ]

    def parse(self, response):
        for sel in response.xpath('//*[@id="timeline"]'):
            item=DmozItem()
            item['title'] = sel.xpath('div/div[@class="news-info"]/dl/dt/a/text()').extract()
            #print item['title']
            item['link'] = sel.xpath('div/div[@class="news-info"]/dl/dt/a/@href').extract()
            item['dat'] = sel.xpath(
                'div/div[@class="news-info"]/dl/dd/span[@class="time"]/text()').extract()
            item['hot'] = sel.xpath(
                'div/div[@class="news-bot"]/span[@class="look"]/strong/text()').extract()
            item['info'] = sel.xpath(
                'div/div[@class="news-info"]/dl/dd[@class="text"]/text()').extract()
            #print title,link,desc
            yield item
