# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import datetime

class TutorialPipeline(object):
    def __init__(self):
        self.file = open('tencent.txt','w')
        #self.file2 = open('zh.txt','w')
    def process_item(self, item, spider):
        if len(item['title'])>0 and len(item['link'])>0:
            self.file.write('腾讯安全应急响应中心\n')
            for i in xrange(len(item['title'])):
                if (datetime.datetime.now()-datetime.datetime.strptime(item['dat'][i].strip(),'%Y-%m-%d')).days>1:
                    continue
                self.file.write(str(i+1)+': ')
                self.file.write(str(item['title'][i].encode("utf-8"))+'\n')
                self.file.write(str(item['info'][i].encode("utf-8"))+'\n')
                self.file.write('https://security.tencent.com/'+str(item['link'][i])+'\n\n')
        return item
