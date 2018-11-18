# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import datetime
import re

class TutorialPipeline(object):
    def __init__(self):
        self.file = open('heiba.txt','w')
        #self.file2 = open('zh.txt','w')
    def process_item(self, item, spider):
        if len(item['title'])>0 and len(item['link'])>0:
            p = re.compile(u'时间：(.*)相关')
            self.file.write('黑吧安全网\n')
            for i in xrange(len(item['title'])):
                print "date",item['dat'][i].strip()

                dat=p.search(item['dat'][i].strip()).group(1)
                if (datetime.datetime.now()-datetime.datetime.strptime(dat.strip(),'%Y-%m-%d')).days>1:
                    continue
                self.file.write(str(i+1)+': ')
                self.file.write(str(item['title'][i].strip().encode("utf-8"))+str(dat.strip())+'\n')
                self.file.write(str(item['info'][i].strip().encode("utf-8"))+' ')
                self.file.write('http://www.myhack58.com/'+str(item['link'][i])+'\n')
        return item
