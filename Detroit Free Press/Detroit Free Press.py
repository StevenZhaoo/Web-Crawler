import requests
import json
from lxml import etree
num=7
date_list=['Aug. 4, 2020','Aug. 5, 2020','Aug. 6, 2020','Aug. 7, 2020','Aug. 8, 2020','Aug. 9, 2020','Aug. 10, 2020']
headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15'}
html=requests.get('https://www.freep.com/search/2020%20election/',headers = headers)
html.encoding='utf-8'
#print(html.text)
#获取所有文章的url
html = etree.HTML(html.text)
urls = html.xpath('/html/body/div[1]/div[2]/div[1]/div[2]/ul/li/a/@href')
for i in urls:
#   print(i)
    web='https://www.freep.com'+i
    print(str(num)+':'+str(web))
    artical_html=requests.get(web,headers = headers)
    artical_html.encoding='utf-8'
    artical_html = etree.HTML(artical_html.text)
    time0 = artical_html.xpath('//*/div/span[2]/span/text()')  # 获取发布时间
    if time0:
        time=time0[1]
        time=time[-12:]
    if time in date_list:
        print(time)
        title=artical_html.xpath('//*/h1/text()')          #获取文章标题
        title[0]=title[0].replace('\r\n            ','').replace('\r\n        ','')
        print(title)
        author=artical_html.xpath('//*/div/span[1]/a/text()')
        print(author)
        artical=artical_html.xpath('//*[@id="overlay"]/div[2]/article/div[3]/p/text()')
        for i in artical:
            print(i)
        if artical:
            file1 = open('/Users/pmeng/Desktop/2020-8-4/Detroit Free Press/'+str(num)+'.txt', 'a')  # 默认的路径是以/Users/xx/xx/NameofFile.txt
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
https://www.freep.com/search/2020%20election/
https://www.freep.com/picture-gallery/opinion/columnists/mike-thompson/2020/05/11/presidential-election-2020-trump-biden-cartoons-humor-satire-coronavirus/3110265001/
/html/body/div[1]/div[2]/div[1]/div[2]/ul/li[2]/a
//*[@id="mainContentSection"]/div/div/div[1]/story-timestamp
//*[@id="module-position-S64TUGDGhlI"]/div/span[2]/span
//*[@id="module-position-S6HwmzDnDSU"]/div/span[2]/span

//*[@id="overlay"]/div[2]/article/div[3]/p[1]/text()
//*[@id="overlay"]/div[2]/article/div[3]/p[2]/text()
//*[@id="overlay"]/div[2]/article/div[3]/p[3]/text()


https://oafishobservation.com/v2rtklLdHjFqcgOmMKWuVBgLHAHw-eqJ35JyGYJWUDD6uK6tcQPh-ar-6FcEc9L1acL4kN6SxF_rfLCxpSdc
    "subscription": {},
    "sessionID": "4-b1a186a9-358e6524f2cfc77913558c748087dd1a-6763652d75732d7765737431-5f30cd13-0",
    "now": 1597033747,
    "ids": [
        {
            "id": "1c48c-7b5cd476-5f30cd13",
            "type": "pageview"



'''