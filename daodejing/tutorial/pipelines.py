# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import datetime
import re
import  sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

class TutorialPipeline(object):
    def __init__(self):
        self.file = open('daodejing.txt','w')
        #self.file2 = open('zh.txt','w')
    def process_item(self, item, spider):
        #print "len",len(item['title'])
        #p = re.compile(u'.*(\d{4}-\d{2}-\d{2}).*')

        if len(item['source'])>0:
            #self.file.write('四.鸡汤语录\n')
            for i in xrange(len(item['source'])):
                dat = item['source'][i].strip()
                print 'date=',dat
                #if (datetime.datetime.now()-datetime.datetime.strptime(dat,'%Y-%m-%d')).days>2:
                #    continue
                self.file.write(item['source'][i].strip()+'\n')
                self.file.writelines(item['translation'][i].strip()+'\n')
                #self.file.write(str(item['title'][i].strip())+'http://www.2cto.com'+item['link'][i]+'\n')
                #self.file.write(str(item['info'][i].strip().encode("utf-8"))+' ')
                #self.file.write(str('http://www.2cto.com'+item['link'][i])+'\n')
        return item
