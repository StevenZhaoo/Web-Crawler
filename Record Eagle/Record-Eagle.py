import requests
from lxml import etree
num=1
page=100
date_list=['Aug 4, 2020','Aug 5, 2020','Aug 6, 2020','Aug 7, 2020','Aug 8, 2020','Aug 9, 2020','Aug 10, 2020']
headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15'}
for i in range(1,page+1):
    print('现在是第'+str(i)+'页')
    html=requests.get('https://www.record-eagle.com/search/?l=25&sd=desc&s=start_time&f=html&app%5B0%5D=editorial&q=2020+election&nsa=eedition&o='+str((i-1)*25),headers = headers)
    html.encoding='utf-8'
#    print(html.text)
#获取所有文章的url
    html = etree.HTML(html.text)
    urls = html.xpath('//*/div[1]/div[2]/div[2]/h3/a/@href')
    for i in urls:
#        print(i)
        web='https://www.record-eagle.com'+i
        print(str(num)+':'+str(web))
        artical_html=requests.get(web,headers = headers)
        artical_html.encoding='utf-8'
        artical_html = etree.HTML(artical_html.text)
        time = artical_html.xpath('//*/header/div[2]/span/ul/li[3]/time[1]/text()')  # 获取发布时间
        for i in time:
            if i in date_list:
                print(time)
                title=artical_html.xpath('//*/header/h1/span/text()')          #获取文章标题
                title[0]=title[0].replace('\r\n            ','').replace('\r\n        ','')
                print(title)
                author=artical_html.xpath('//*/header/div[2]/span/ul/li[1]/span/text()')
                print(author)
                artical=artical_html.xpath('//*[@id="asset-content"]/div[1]/div/div/div[5]/p/text()')
                for i in artical:
                    print(i)
                if artical:
                    file1 = open('/Users/pmeng/Desktop/2020-8-4/Record-Eagle/'+str(num)+'.txt', 'a')  # 默认的路径是以/Users/xx/xx/NameofFile.txt
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
    num=1
    for i in list_url:
        print('page'+str(num))
        web='https://www.record-eagle.com'+i
        print(web)
        news_html=requests.get(web,headers=headers)
        news_html.encoding='utf-8'
'''
'''
https://www.record-eagle.com/search/?l=25&sd=desc&s=start_time&f=html&app=editorial&q=2020+election&nsa=eedition
https://www.record-eagle.com/search/?l=25&sd=desc&s=start_time&f=html&app%5B0%5D=editorial&q=2020+election&nsa=eedition&o=0
https://www.record-eagle.com/search/?l=25&sd=desc&s=start_time&f=html&app%5B0%5D=editorial&q=2020+election&nsa=eedition&o=25
https://www.record-eagle.com/search/?l=25&sd=desc&s=start_time&f=html&app%5B0%5D=editorial&q=2020+election&nsa=eedition&o=50

//*[@id="card-summary-23af1cba-b78a-5b04-9ea3-779476e5215e"]/div[1]/div[2]/div[2]/h3/a
//*[@id="card-summary-3f233c9b-13dc-56aa-bfdb-42fec19efc98"]/div[1]/div[2]/div[2]/h3/a

//*[@id="asset-258e11e8-ace2-5e03-ad2a-de1e24638686"]/header/div[2]/span/ul/li[3]/time[1]
https://www.record-eagle.com/search/?l=25&sd=desc&s=start_time&f=html&app%5B0%5D=editorial&q=2020+election&nsa=eedition&o=325
//*[@id="asset-content"]/div[1]/div/div/div[5]/p[1]
//*[@id="asset-content"]/div[1]/div/div/div[5]/p[2]
//*[@id="asset-content"]/div[1]/div/div/div[5]/p[1]/text()
/Users/pmeng/Desktop/2020-8-4
//*[@id="asset-258e11e8-ace2-5e03-ad2a-de1e24638686"]/header/div[2]/span/ul/li[1]/span
'''