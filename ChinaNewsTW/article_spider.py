#-*- coding:utf-8 -*-

import time
from bs4 import BeautifulSoup
# from user_agents import agents
import requests
import random
import re

def get_article(url):
    '''
    :param url: 待爬取的url
    :return:
    '''
    # agent = random.choice(agents)
    # header = {'User-Agent': agent}
    res = requests.get(url)
    time.sleep(2)
    res.encoding = 'gb2312'
    soup = BeautifulSoup(res.text, 'html.parser')
    newsArticle = soup.select('.left_zw')
    # print(newsArticle_href)
    pattern = re.compile(r'<[^>]+>', re.S)
    content_list = []
    for item in (str(newsArticle[0]).split('\n')):
        content = pattern.sub('', str(item))
        content_list.append(content)

    sentences = ''.join(content_list).split('\n')
    return sentences