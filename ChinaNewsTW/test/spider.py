from bs4 import BeautifulSoup
from user_agents import agents
import requests
import time
import random


def China_News(url):
    '''
    :param url: 待爬取的url
    :return:
    '''
    agent = random.choice(agents)
    header = {'User-Agent': agent}
    res = requests.get(url, headers=header)
    time.sleep(1)
    # res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    newsArticle_href = soup.select('body > div > div.cont > div.con2 > table > tbody > tr > td.color065590 > a')
    print(newsArticle_href)
    # for href in newsArticle_href:
    #     url = (href.find_all('a')[0].get('href'))
    #     if url[0] == '/':
    #         url = 'http://www.chinanews.com'+url
    #         print(url)

China_News('http://channel.chinanews.com/cns/cl/tw-lahd.shtml')