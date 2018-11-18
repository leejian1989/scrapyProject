import scrapy
from tutorial.items import DmozItem

class DomzSpider(scrapy.Spider):
    name = 'heiba'
    allowed_domains = ["myhack58.com"]
    start_urls = [
        "http://www.myhack58.com/Article/html/1/4/Article_004_1.htm",
        ]

    def parse(self, response):
        for sel in response.xpath('//*[@class="ArticleListBox"]'):
            item=DmozItem()
            item['title'] = sel.xpath('ul/li[@class="Noptitle"]/a/text()').extract()
            #print item['title']
            item['link'] = sel.xpath('ul/li[@class="Noptitle"]/a/@href').extract()
            item['dat'] = sel.xpath(
                'ul/li[@class="Noptinfo"]/text()').extract()
            item['info'] = sel.xpath(
                'ul/li[@class="Noptdes"]/text()').extract()
            #print title,link,desc
            yield item
