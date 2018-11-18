#-*- coding:UTF-8 -*-
import scrapy
from tutorial.items import DmozItem

class DomzSpider(scrapy.Spider):
    name = 'zscaler'
    allowed_domains = ["zscaler.com"]
    start_urls = [
        u"https://www.zscaler.com/blogs/mobile-malware"
        ]
    '''
    def start_requests(self):
        yield scrapy.Request(self.start_urls[0],
                             cookies={'maxPageNum5115385':19,
                                      '__jsluid':'bd77a712a4757cf44b5d742711350446',
                                      '__jsl_clearance':'1488007544.594|0|0Rw0sen34LVm%2BgT%2BldDpfPd6OMY%3D'
                                      },
                             callback=self.parse)
    '''
    def parse(self, response):
        print "response:=",response
        for sel in response.xpath('//div[@class="row posth"]'):
            #print  sel.extract()
            item=DmozItem()
            item['title'] = sel.xpath('div[@class="col-sm-6"]/div[@class="row post"]/div[@class="col-sm-12"]/h1/a/text()').extract()
            #baidu title: div[3]/div/h3/a
            #print item['title']
            item['link'] = sel.xpath('div[@class="col-sm-6"]/div[@class="row post"]/div[@class="col-sm-12"]/h1/a/@href').extract()

            #baidu link:div[3]/div/h3/a/@href
            #item['info'] = sel.xpath('li/p[@class="content"]').extract()
            #baidu info:div[3]/div/div
            item['dat']=sel.xpath('div[@class="col-sm-6"]/div[@class="row author"]/div/div[@class="author-info"]/div/time/text()').extract()
            #print title,link,desc
            yield item
