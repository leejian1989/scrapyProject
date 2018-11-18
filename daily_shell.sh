cd /Users/wow/scrapyProject/freebuf && scrapy crawl freebuf &
cd /Users/wow/scrapyProject/mcafee && scrapy crawl mcafee &
cd /Users/wow/scrapyProject/fortinet && scrapy crawl fortinet &
cd /Users/wow/scrapyProject/zscaler && scrapy crawl zscaler &
cd /Users/wow/scrapyProject/lookout && scrapy crawl lookout &
cd /Users/wow/scrapyProject/trendMicro && scrapy crawl trendMicro &
cd /Users/wow/scrapyProject/qualys && scrapy crawl qualys &
cd /Users/wow/scrapyProject/f-secure && scrapy crawl f-secure

wait

cd /Users/wow/scrapyProject

rm daily.log
today=`date +%Y.%m.%d`
echo "晨报:" $today >daily.log
echo "一.安全" >> daily.log
python secure.py
cat secure.log >> daily.log

echo "二.电信诈骗">>daily.log
cd /Users/wow/scrapyProject/cheat
scrapy crawl cheat
python cheat_ui.py
cd /Users/wow/scrapyProject
cat cheat/cheat.log >> daily.log

echo "三.金融大数据">>daily.log
cd /Users/wow/scrapyProject/finacialData && scrapy crawl finacial &
cd /Users/wow/scrapyProject/finacial_bankjrj && scrapy crawl bankjrj

wait

cd /Users/wow/scrapyProject
python finacial.py
cat finacial.log >> daily.log
