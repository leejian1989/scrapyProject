#!/usr/bin/python
#-*- coding: UTF-8 -*-
import re
import Queue
import copy
#s='''http://ssxd.mediav.com/s?type=2&r=20&pinfo=&mv_ref=news%2Eso%2Ecom&enup=CAABDhEWKAgAAigWEQ4A&mvid=NjQzOTIyNjg3MzI1MDE0MTQwMTAwMTc&bid=1117342e04422eaf&price=AAAAAFh5yjgAAAAAAAqXpVWGtWy8Mn+qxybxPQ==&finfo=DAABCAABAAAFPwgAAgAAANIEAAM/dhh053vezAAIAAIAAAADCgADVkxd6d7mYXYIAAQAAAD5CAAIAMzs8AoACQAAAAAABgAEBgAKAAAA&ugi=FZjsDhXcrkBMFQIVQBVeFQAAFbyt89wDAA&uai=FbLqzQElAhUCFrKj9riotKrMrAEV8Acl/pG25gcA&ubi=Fb7CIxWUk78BFYTQsg0Vhv2URRUEFRwWrIXO7RQWsqOLoLL6rsysATQCFoiAMCUGFf/Zx84JAA&clickid=0&csign=850d1ef6c115523f&url=http%3A%2F%2Fszdx%2Essmdjf%2Ecom%2Findex%5Fxxl%2Ehtml'''
#print  len(s)
#ss='''<a class="news_title" href="http://www.toutiao.com/i6434840994960638465/" target="_blank" rel="noopener noreferrer">掌众金服获得"年度中国<em>金融大数据</em>风控应用先锋奖"</a>'''
#t = re.compile('noreferrer">(.*)</a>')

#title=t.search(ss).group(1)
#title=title.replace('<em>','')
#title=title.replace('</em>','')

#s='abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa'
s="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
#s='babad'
#s='aaaaaaaa'
#s='cbbd'
max_len=0
max_s=''

def getMaxString(s,f,b):
    while f<len(s) and b>=0 and s[f]==s[b] :
        f+=1
        b-=1
    #print f,b
    return s[b+1:f]

#print range(len(s),0)
for i in xrange(len(s)):
    t=getMaxString(s,i,i)
    #print i,t
    if len(t)>max_len:
        max_len=len(t)
        max_s=t
        #print max_s
    if i<len(s)-1 and s[i+1]==s[i]:
        t=getMaxString(s,i+1,i)
        if len(t)>max_len:
            max_len=len(t)
            max_s=t
            max_len
print max_s
'''file=open('page.log','r')
page_index=file.readline()

file.close()
print page_index
curr=int(page_index)+1
file=open('page.log','w')
file.writelines(str(curr))
print  "http://www.daodejing.org/"+page_index+".html"'''