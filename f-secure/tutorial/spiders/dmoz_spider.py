#-*- coding:UTF-8 -*-
import scrapy
from tutorial.items import DmozItem

class DomzSpider(scrapy.Spider):
    name = 'f-secure'
    allowed_domains = ["f-secure.com"]
    start_urls = [
        u"https://labsblog.f-secure.com/"
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
        #print "response:=",response
        for sel in response.xpath('//div[@class="container"]'):
            #print  sel.extract()
            item=DmozItem()
            item['title'] = sel.xpath('div[@class="row post"]/div[@class="col-lg-8 col-md-7 col-sm-6 col-xs-12"]/a/h3/text()').extract()
            #baidu title: div[3]/div/h3/a
            #print item['title']
            item['link'] = sel.xpath('div[@class="row post"]/div[@class="col-lg-8 col-md-7 col-sm-6 col-xs-12"]/a/@href').extract()

            #baidu link:div[3]/div/h3/a/@href
            #item['info'] = sel.xpath('li/p[@class="content"]').extract()
            #baidu info:div[3]/div/div
            item['dat']=sel.xpath('div[@class="row post"]/div[@class="col-lg-2 col-md-2 col-sm-3 author-col hidden-xs"]/div/div/div[@class="post_title"]/p/text()').extract()
            #print title,link,desc
            yield item
