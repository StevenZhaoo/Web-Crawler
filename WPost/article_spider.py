#-*- coding:utf-8 -*-

from bs4 import BeautifulSoup
from user_agents import agents
import requests
import time
import random

def get_article(url):
    '''
    :param url: 指定日期的链接
    :return content: 文本的内容
    :return classfy[1]: 文本的类型
    '''
    try:
        classfy = url.split('//')[1].split(('/')[0])
        agent = random.choice(agents)
        header = {'User-Agent': agent}
        res = requests.get(url.rsplit('\r\n')[0], headers=header)
        time.sleep(1)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')
        newsArticle = getnewsArticle(soup.select('.paywall'))
        content = ''
        for con in newsArticle:
            content = content + con
        return classfy[1], content
    except Exception as e:
        print(e)

def getnewsArticle(news):
    '''
    :param news: 新闻主题内容链接
    :return newsArticle: 新闻主题内容
    '''
    newsArticle = []
    for p in news:
         newsArticle.append(p.text.strip())
    return newsArticle