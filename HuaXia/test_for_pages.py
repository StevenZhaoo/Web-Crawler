from bs4 import BeautifulSoup
from user_agents import agents
import requests
import time
import random
import re


def spider(url):
    #print(url)
    agent = random.choice(agents)
    header = {'User-Agent': agent}
    res = requests.get(url, headers = header)
    res.encoding = 'gb2312'
    #print(res)
    time.sleep(2)
    soup = BeautifulSoup(res.text, 'html.parser')
    newsArticle_href = soup.select('.A002')
    total = []
    for href in newsArticle_href:
        url = 'http://www.huaxia.com'+ href.get('href')
        # print(href.get_text())
        formal_title = href.get_text()
        print(url)
        get_content(url, formal_title)
    #     art_line = get_content(url)
    #     print(art_line)
    #     total.append(art_line)
    # print(total)

def get_content(url, formal_title):
    agent = random.choice(agents)
    header = {'User-Agent': agent}
    res = requests.get(url, headers=header)
    res.encoding = 'gb2312'
    #print(res)
    time.sleep(2)
    soup = BeautifulSoup(res.text, 'html.parser')
    newsArticle = soup.select('.px14')
    for item in (str(newsArticle[0]).split('<strong>')):
        new_item = item.split('</strong>')
        if len(new_item) > 1:
            new_item[1] = re.sub('<[^>]+>', '', new_item[1])
            new_item[0] = re.sub('<[^>]+>', '', new_item[0])
            new_item[1] = ''.join(new_item[1].split())
            new_item[0] = ''.join(new_item[0].split())
            #print(new_item)
            title = '/Users/steven/Documents/算文解字/爬虫/HuaXia/test/' + formal_title + new_item[0] + '.txt'
            with open(title ,'w') as f:
                f.write(new_item[1])
    # res = []
    # for item in (str(newsArticle[0]).split('<strong>')):
    #     dr = re.compile(r'<[^>]+>', re.S)
    #     dd = dr.sub('', item)
    #     art = (''.join(dd.split()))
    #     print(art)
    #     if art:
    #         res.append(art)
    # print(res)
    # return res


if __name__ == '__main__':
    org_url = 'http://www.huaxia.com/lasd/twdsj/index_4.html'
    spider(org_url)
