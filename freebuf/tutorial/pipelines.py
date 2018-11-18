# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import datetime
import MySQLdb
from twisted.enterprise import  adbapi
import MySQLdb.cursors

class TutorialPipeline(object):
    def __init__(self,dbpool):
        self.file = open('freebuf.txt','w')
        self.dbpool=dbpool
        #self.file2 = open('zh.txt','w')

    @classmethod
    def from_settings(cls,settings):
        dbparams=dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=False,
        )

        dbpool=adbapi.ConnectionPool('MySQLdb',**dbparams)
        return cls(dbpool)

    def process_item(self, item, spider):
        if len(item['title'])>0 and len(item['link'])>0:
            self.file.write('freeBuf\n')
            for i in xrange(len(item['title'])):
                if (datetime.datetime.now()-datetime.datetime.strptime(item['dat'][i].strip(),'%Y-%m-%d')).days>2:
                    continue
                self.file.write(str(i+1)+': ')
                self.file.write(str(item['title'][i].strip().encode("utf-8"))+str(item['link'][i].strip())+'\n')
                dict_item={
                    's_date':datetime.date.today(),
                    'title':str(item['title'][i].strip().encode("utf-8")),
                    'source':'freebuf',
                    'link':str(item['link'][i].strip()),
                    'title_hash':hash(str(item['title'][i].strip().encode("utf-8")))
                }
                query=self.dbpool.runInteraction(self._conditional_insert,dict_item)
                query.addErrback(self._handle_error,item,spider)
                #self.file.write(str(item['info'][i].strip().encode("utf-8"))+' ')
                #self.file.write(str(item['link'][i])+'\n')
        return item

    def _conditional_insert(self,tx,dict_item):
        sql="insert into dailysecuriy(s_date,source,title,link,title_hash) values(%s,%s,%s,%s,%s)"
        params=(dict_item['s_date'],dict_item['source'],dict_item['title'],dict_item['link'],dict_item['title_hash'])
        tx.execute(sql,params)

    def _handle_error(self,failue,item,spider):
        print failue