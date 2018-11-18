import scrapy
from tutorial.items import DmozItem

class DomzSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ["tencent.com"]
    start_urls = [
        "https://security.tencent.com/index.php/blog",
        ]

    def parse(self, response):
        for sel in response.xpath('//*[@class="mod-itemlist-article"]'):
            item=DmozItem()
            item['title'] = sel.xpath('li/div[@class="item_content"]/div[@class="content_title"]/a/text()').extract()
            #print item['title']
            item['link'] = sel.xpath('li/div[@class="item_content"]/div[@class="content_title"]/a/@href').extract()
            item['dat'] = sel.xpath(
                'li/div[@class="item_content"]/div[@class="content_info"]/span[@class="info_date"]/span/text()').extract()
            item['hot'] = sel.xpath(
                'li/div[@class="item_content"]/div[@class="content_info"]/span[@class="info_watched"]/span/text()').extract()
            item['info'] = sel.xpath(
                'li/div[@class="item_content"]/div[@class="content_brief"]/p/text()').extract()
            #print title,link,desc
            yield item
