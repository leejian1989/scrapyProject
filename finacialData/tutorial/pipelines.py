# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import datetime
import  re
import MySQLdb
from twisted.enterprise import  adbapi
import MySQLdb.cursors

class TutorialPipeline(object):
    def __init__(self,dbpool):
        self.file = open('finacial.txt','w')
        #self.file2 = open('zh.txt','w')
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparams = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=False,
        )

        dbpool = adbapi.ConnectionPool('MySQLdb', **dbparams)
        return cls(dbpool)

    def process_item(self, item, spider):
        p = re.compile('.*/p>(.+)<span.*')
        t = re.compile('noreferrer">(.*)</a>')
        if len(item['title'])>0 and len(item['link'])>0 :
            #self.file.write('金融大数据\n')
            #self.file.write(str(len(item['title']))+' '+str(len(item['info'])))
            for i in xrange(len(item['title'])):
                #print "item info------",item['info'][i]
                #print  "search result-----",p.search(item['info'][i]).group()
                #info = p.search(item['info'][i]).group(1)
                #info=info.replace('<em>','')
                #info=info.replace('</em>','')
                print 'title-------',item['title'][i],len(item['title'][i]),len(item['link'][i])

                title=t.search(item['title'][i]).group(1)
                title=title.replace('<em>','')
                title=title.replace('</em>','')
                '''fuck off 360 advertisement'''
                if len(item['link'][i])<200:
                    self.file.write(str(i + 1) + ': ')
                    self.file.write(str(title.strip().encode("utf-8")) + str(item['link'][i]) + '\n')

                    dict_item = {
                        's_date': datetime.date.today(),
                        'title': str(title.strip().encode("utf-8")),
                        'source': '360',
                        'link': str(item['link'][i].strip()),
                        'title_hash': hash(str(title.strip().encode("utf-8")))
                    }
                    query = self.dbpool.runInteraction(self._conditional_insert, dict_item)
                    query.addErrback(self._handle_error, item, spider)
                    #continue

                #self.file.write(str(info.strip().encode("utf-8"))+' ')
                #self.file.write(str(item['link'][i])+'\n')
        return item

    def _conditional_insert(self,tx,dict_item):
        sql="insert into dailyfinacial(s_date,source,title,link,title_hash) values(%s,%s,%s,%s,%s)"
        params=(dict_item['s_date'],dict_item['source'],dict_item['title'],dict_item['link'],dict_item['title_hash'])
        tx.execute(sql,params)

    def _handle_error(self,failue,item,spider):
        print failue