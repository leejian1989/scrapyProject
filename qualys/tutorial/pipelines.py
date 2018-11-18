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
        self.file = open('qualys.txt','w')
        self.file.write('qualys\n')
        self.counter=0
        self.dbpool = dbpool
        #self.file2 = open('zh.txt','w')

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

        #print  'helloo------------'

        month={'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,
               'September':9,'October':10,'November':11,'December':12}

        if len(item['title'])>0 and len(item['link'])>0:

            #self.file.write(str(len(item['title']))+' '+str(len(item['info'])))

            '''March 7, 2017 '''
            #print 'ddate--------',item['dat']
            dat=item['dat'].replace(',','')
            dat_list=dat.split()
            #if len(dat_list)!=3:
            #    print 'date is not right!!!!'
            #print 'date--------',dat_list[-1],dat_list[-3],dat_list[-2]

            dat_1=datetime.date(int(dat_list[-1]),month[dat_list[-3]],int(dat_list[-2]))
            dat_t=datetime.date.today()
            if (dat_t-dat_1).days<=2:
                print 'date--------',dat_1,dat_t,(dat_t-dat_1).days
                print 'title-------',item['title']
                self.file.write(str(self.counter+1)+': ')
                self.counter+=1
                self.file.write(str(item['title'][0].strip().encode("utf-8"))+str(item['link'][0])+'\n')

                dict_item = {
                    's_date': datetime.date.today(),
                    'title': str(item['title'][0].strip().encode("utf-8")),
                    'source': 'qualys',
                    'link': str(item['link'][0].strip()),
                    'title_hash': hash(str(item['title'][0].strip().encode("utf-8")))
                }
                query = self.dbpool.runInteraction(self._conditional_insert, dict_item)
                query.addErrback(self._handle_error, item, spider)

            #self.file.write(str(info.strip().encode("utf-8"))+' ')
            #self.file.write(str(item['link'][i])+'\n')
        return item

    def _conditional_insert(self,tx,dict_item):
        sql="insert into dailysecuriy(s_date,source,title,link,title_hash) values(%s,%s,%s,%s,%s)"
        params=(dict_item['s_date'],dict_item['source'],dict_item['title'],dict_item['link'],dict_item['title_hash'])
        tx.execute(sql,params)

    def _handle_error(self,failue,item,spider):
        print failue