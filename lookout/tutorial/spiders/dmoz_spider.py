#-*- coding:UTF-8 -*-
import scrapy
from tutorial.items import DmozItem

class DomzSpider(scrapy.Spider):
    name = 'lookout'
    allowed_domains = ["lookout.com"]
    start_urls = [
        u"https://blog.lookout.com/"
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
        for sel in response.xpath('//div[@class="content"]/div[@class="row"]/div[@class="col-8"]'):
            #print  sel.extract()
            item=DmozItem()
            item['title'] = sel.xpath('div/h2/a/@title').extract()
            #baidu title: div[3]/div/h3/a
            #print item['title']
            item['link'] = sel.xpath('div/h2/a/@href').extract()

            #baidu link:div[3]/div/h3/a/@href
            #item['info'] = sel.xpath('li/p[@class="content"]').extract()
            #baidu info:div[3]/div/div
            item['dat']=sel.xpath('div/div[@class="date"]/text()').extract()
            #print title,link,desc
            yield item
