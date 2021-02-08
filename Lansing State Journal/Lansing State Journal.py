import requests
import re
from lxml import etree
num=1
page=5
today='2020/08/10'
date_list=['2020/08/04','2020/08/05','2020/08/06','2020/08/07','2020/08/08','2020/08/09','2020/08/10']
headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15'}
for i in range(1,page+1):
    html=requests.get('https://www.lansingstatejournal.com/search/?q=2020%20election&page='+str(i),headers = headers)
    html.encoding='utf-8'
#    print(html.text)

#获取所有文章的url
    html = etree.HTML(html.text)
    urls = html.xpath('/html/body/main/div[1]/a/@href')
    for i in urls:
#        print(i)
        web='https://www.lansingstatejournal.com'+i
        for each in date_list:
            if each in web:
                print(str(num)+':'+str(web))
                artical_html=requests.get(web,headers = headers)
                artical_html.encoding='utf-8'
        #        print(artical_html.text)
                artical_html=etree.HTML(artical_html.text)
                title=artical_html.xpath('/html/body/div[2]/main/article/h1/text()')          #获取文章标题
#        title[0]=title[0].replace('\r\n            ','').replace('\r\n        ','')
                print(title)
                author=artical_html.xpath('/html/body/div[2]/main/article/div[1]/text()')
                print(author)
                artical=artical_html.xpath('/html/body/div[2]/main/article/div[4]/p/text()')
                for i in artical:
                    print(i)
                if artical:
                    file1 = open('/Users/pmeng/Desktop/2020-8-4/Lansing State Journal/'+str(num)+'.txt', 'a')  # 默认的路径是以/Users/xx/xx/NameofFile.txt
                    file1.write(title[0]+'\r\n')
                    print('文章名称已写入')
                    if author:
                        file1.write(author[0]+'\r\n')
                        print('文章作者已写入')
                    file1.write(web+'\r\n')
                    print('网址已写入')
                    for i in artical:
                        file1.write(i+'\r\n')
                    print('内容已写入')
                    file1.close()
                    num=num+1

'''
https://www.lansingstatejournal.com/search/?q=2020+election
https://www.lansingstatejournal.com/search/?q=2020%20election&page=2
https://www.lansingstatejournal.com/search/?q=2020%20election&page=3

/html/body/main/div[1]/a[1]
/html/body/main/div[1]/a[2]
https://www.lansingstatejournal.com/story/news/politics/elections/2020/08/04/michigan-primary-election-2020-live-updates-results-voting-august/5578133002/

/html/body/div[2]/main/article/div[2]
<div class="gnt_ar_dt" aria-label="Published: 8:41 a.m. ET Aug. 4, 2020 Updated: 7:36 a.m. ET Aug. 6, 2020"></div>
<div class="gnt_ar_dt" aria-label="Published: 10:11 a.m. ET Jul. 13, 2020 Updated: 9:28 a.m. ET Aug. 3, 2020"></div>

<div class="gnt_ar_dt" aria-label="Published: 8:41 a.m. ET Aug. 4, 2020 Updated: 7:36 a.m. ET Aug. 6, 2020"></div>
/html/body/div[3]/main/article/div[2]

/html/body/div[2]/main/article/div[4]/p[1]
/html/body/div[2]/main/article/div[4]/h3[1]
/html/body/div[2]/main/article/div[4]/p[2]
'''