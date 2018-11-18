import scrapy
from tutorial.items import DmozItem

class DomzSpider(scrapy.Spider):
    name = 'daodejing'
    allowed_domains = ["daodejing.org"]
    file = open('page.log', 'r')
    page_index=file.readline().strip()
    file.close()
    file=open('page.log','w')
    file.writelines(str(int(page_index)+1))
    file.close()
    start_urls = [
        "http://www.daodejing.org/"+page_index+".html"
        ]

    def parse(self, response):
        for sel in response.xpath('//div[@id="contain"]'):
            item=DmozItem()
            item['source'] = sel.xpath('div[5]/p[2]/text()').extract()
            print item['source']
            item['translation'] = sel.xpath('div[5]/p[4]/text()').extract()

            #print title,link,desc
            yield item
