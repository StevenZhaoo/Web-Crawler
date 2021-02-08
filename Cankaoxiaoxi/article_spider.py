#-*- coding:utf-8 -*-

import time
from bs4 import BeautifulSoup
from user_agents import agents
import requests
import random
import re

def get_article(url):
    '''
    :param url: 指定日期的链接
    :return content: 指定url的正文内容
    '''
    agent = random.choice(agents)
    header = {'User-Agent': agent}
    res = requests.get(url, headers=header)
    time.sleep(2)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    newsArticle = soup.select('.articleText')
    pattern = re.compile(r'<[^>]+>', re.S)
    for item in (str(newsArticle[0]).split('<strong>')):
        new_item = item.split('</strong>')
        if len(new_item) > 1:
            contents = pattern.sub('', str(new_item))
            content_list = contents.split('\'')
            content = ''.join(content_list)
    return content