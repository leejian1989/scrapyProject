import scrapy
from tutorial.items import DmozItem

class DomzSpider(scrapy.Spider):
    name = '2cto'
    allowed_domains = ["2cto.com"]
    start_urls = [
        "http://www.2cto.com/News/safe/",
        ]

    def parse(self, response):
        for sel in response.xpath('//div[@class="box_ListBody"]'):
            item=DmozItem()
            item['title'] = sel.xpath('div/div[@class="LTitle"]/a/text()').extract()
            #print item['title']
            item['link'] = sel.xpath('div/div[@class="LTitle"]/a/@href').extract()
            item['info'] = sel.xpath(
                'div/ul[@class="ArtInfo"]/li/text()').extract()
            #print title,link,desc
            yield item
