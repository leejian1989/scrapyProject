import scrapy
from tutorial.items import DmozItem

class DomzSpider(scrapy.Spider):
    name = 'secwiki'
    allowed_domains = ["sec-wiki.com"]
    start_urls = [
        "https://www.sec-wiki.com/news",
        ]

    def parse(self, response):
        for sel in response.xpath('//tbody'):
            item=DmozItem()
            item['title'] = sel.xpath('tr/td[2]/a/text()').extract()
            #print item['title']
            item['link'] = sel.xpath('tr/td[2]/a/@href').extract()
            item['dat'] = sel.xpath(
                'tr/td[1]/text()').extract()
            item['hot'] = sel.xpath(
                'tr/td[4]/text()').extract()

            #print title,link,desc
            yield item
