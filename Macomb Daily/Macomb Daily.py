import requests
from lxml import etree
num=1
page=20
today=['Aug 10, 2020']
date_list=['Aug 4, 2020','Aug 5, 2020','Aug 6, 2020','Aug 7, 2020','Aug 8, 2020','Aug 9, 2020','Aug 10, 2020']
headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15'}
for i in range(1,page+1):
    print('这是第'+str(i)+'页')
    html=requests.get('https://www.macombdaily.com/search/?l=25&s=start_time&sd=desc&f=html&t=article%2Cvideo%2Cyoutube%2Ccollection&app%5B0%5D=editorial&nsa=eedition&q=2020+election&o='+str((i-1)*25),headers = headers)
    html.encoding='utf-8'
#    print(html.text)
#获取所有文章的url
    html = etree.HTML(html.text)
    urls = html.xpath('//*/div[1]/div[2]/div[2]/h3/a/@href')
    for i in urls:
#        print(i)
        web = 'https://www.macombdaily.com' + i
        print(str(num) + ':' + str(web))
        artical_html = requests.get(web, headers=headers)
        artical_html.encoding = 'utf-8'
        artical_html = etree.HTML(artical_html.text)
        time = artical_html.xpath('//*/div[3]/header/div[4]/span/ul/li[3]/time/text()')  # 获取发布时间
        print(time)
        title = artical_html.xpath('//*/div[3]/header/h1/span/text()')  # 获取文章标题
        title[0] = title[0].replace('\r\n            ', '').replace('\r\n        ', '')
        print(title)
        artical = artical_html.xpath('//*[@id="asset-content"]/div[1]/div/div[1]/div[3]/p/text()')
        for i in artical:
            print(i)
        if artical:
            file1 = open('/Users/pmeng/Desktop/2020-8-4/Macomb Daily/' + str(num) + '.txt','a')  # 默认的路径是以/Users/xx/xx/NameofFile.txt
            file1.write(title[0] + '\r\n')
            print('文章名称已写入')
            if time:
                file1.write(time[0] + '\r\n')
                print('创作时间已写入')
            file1.write(web + '\r\n')
            print('网址已写入')
            for i in artical:
                file1.write(i + '\r\n')
            print('内容已写入')
            file1.close()
            num = num + 1
'''
https://www.macombdaily.com/search/?l=25&s=start_time&sd=desc&f=html&t=article%2Cvideo%2Cyoutube%2Ccollection&app=editorial&nsa=eedition&q=2020+election
https://www.macombdaily.com/search/?l=25&s=start_time&sd=desc&f=html&t=article%2Cvideo%2Cyoutube%2Ccollection&app%5B0%5D=editorial&nsa=eedition&q=2020+election&o=25

/news/elections/macomb-voters-deliver-congressional-district-for-mcclain/article_f6e3fa2e-d710-11ea-8c62-27d878c21ae2.html
https://www.macombdaily.com/news/elections/macomb-voters-deliver-congressional-district-for-mcclain/article_f6e3fa2e-d710-11ea-8c62-27d878c21ae2.html

//*[@id="card-summary-f6e3fa2e-d710-11ea-8c62-27d878c21ae2"]/div[1]/div[2]/div[2]/h3/a
//*[@id="card-summary-5fabecaa-d6a9-11ea-bf5d-a3c9f7c9ae5d"]/div[1]/div[2]/div[2]/h3/a

//*[@id="asset-f6e3fa2e-d710-11ea-8c62-27d878c21ae2"]/div[3]/header/div[4]/span/ul/li[3]/time

//*[@id="asset-content"]/div[1]/div/div[1]/div[3]/p[1]/text()
//*[@id="asset-content"]/div[1]/div/div[1]/div[3]/p[2]/text()

//*[@id="asset-content"]/div[1]/div/div[1]/div[3]/p[1]
//*[@id="asset-content"]/div[1]/div/div[1]/div[3]/p[1]/text()
'''