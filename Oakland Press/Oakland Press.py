import requests
from lxml import etree
num=1
page=15
today='Aug 10, 2020'
date_list=['Aug 4, 2020','Aug 5, 2020','Aug 6, 2020','Aug 7, 2020','Aug 8, 2020','Aug 9, 2020','Aug 10, 2020']
headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15'}
for i in range(1,page+1):
    html=requests.get('https://www.theoaklandpress.com/search/?l=25&s=start_time&sd=desc&f=html&t=article%2Cvideo%2Cyoutube%2Ccollection&app%5B0%5D=editorial&nsa=eedition&q=2020+election&o='+str((i-1)*25),headers = headers)
    html.encoding='utf-8'
#    print(html.text)
#获取所有文章的url
    html = etree.HTML(html.text)
    urls = html.xpath('//*/div[1]/div[2]/div[2]/h3/a/@href')
    for i in urls:
#        print(i)
        web='https://www.theoaklandpress.com'+i
        print(str(num)+':'+str(web))
        artical_html=requests.get(web,headers = headers)
        artical_html.encoding='utf-8'
#        print(artical_html)
        artical_html = etree.HTML(artical_html.text)
        time = artical_html.xpath('//*/div[3]/header/div/span/ul/li[3]/time/text()')  # 获取发布时间
        if time:
            if len(time)!=1:
                del time[1]
#           print(time)
            for i in time:
                if 'hrs ago' in i:
                    time[0]=today
#           print(time)
            for x in time:
                if x in date_list:
                    print(time)
                    title=artical_html.xpath('//*/div[3]/header/h1/span/text()')          #获取文章标题
                    title[0]=title[0].replace('\r\n            ','').replace('\r\n        ','')
                    print(title)
                    author=artical_html.xpath('//*/div[3]/header/div/span/ul/li[1]/span/text()')
                    print(author)
                    artical=artical_html.xpath('//*/div[1]/div[1]/div/div[3]/p/text()')
                    for i in artical:
                        print(i)
                    if artical:
                        file1 = open('/Users/pmeng/Desktop/2020-8-4/Oakland Press/'+str(num)+'.txt', 'a')  # 默认的路径是以/Users/xx/xx/NameofFile.txt
                        file1.write(title[0]+'\r\n')
                        print('文章名称已写入')
                        if author:
                            file1.write(author[0]+'\r\n')
                            print('文章作者已写入')
                        file1.write(time[0]+'\r\n')
                        print('创作时间已写入')
                        file1.write(web+'\r\n')
                        print('网址已写入')
                        for i in artical:
                            file1.write(i+'\r\n')
                        print('内容已写入')
                        file1.close()
                        num=num+1

'''
https://www.theoaklandpress.com/search/?l=25&s=start_time&sd=desc&f=html&t=article%2Cvideo%2Cyoutube%2Ccollection&app=editorial&nsa=eedition&q=2020+election
https://www.theoaklandpress.com/search/?l=25&s=start_time&sd=desc&f=html&t=article%2Cvideo%2Cyoutube%2Ccollection&app%5B0%5D=editorial&nsa=eedition&q=2020+election&o=25

//*[@id="card-summary-051e7236-d7fc-11ea-ada5-7f1d8f064584"]/div[1]/div[2]/div[2]/h3/a
//*[@id="card-summary-57bd8e04-a045-5042-b2c7-bf48078b67c8"]/div[1]/div[2]/div[2]/h3/a
https://www.theoaklandpress.com/news/ny-attorney-general-seeks-to-dissolve-nra/article_051e7236-d7fc-11ea-ada5-7f1d8f064584.html

//*[@id="asset-content"]/div[1]/div[1]/div/div[4]/p[1]
//*[@id="asset-content"]/div[1]/div[1]/div/div[4]/p[2]/text()
//*[@id="asset-content"]/div[1]/div[1]/div/div[4]/p[3]/text()
//*[@id="asset-content"]/div[1]/div[1]/div/div[4]/p[1]/text()
'''