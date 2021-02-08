# -*- coding: utf-8 -*-

# from article_spider import *
from selenium import webdriver

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

def Get_content(driver, url, output_list):
    '''
    :param driver: Webdriver页面
    :param url: 指定日期的链接
    :param output_list: 输出list
    '''
    driver.get(url)
    time.sleep(2.5)
    for j in range(1, 21):
        try:
            i = j*2-1
            title = driver.find_element_by_xpath(
                '/html/body/div/div[3]/div[2]/table[' + str(i) + ']/tbody/tr[1]/td[1]/a').text
            href = driver.find_element_by_xpath(
                '/html/body/div/div[3]/div[2]/table[' + str(i) + ']/tbody/tr[1]/td[1]/a').get_attribute('href')
            content = get_article(href)
            filepath = '/Users/steven/Downloads/test/' + title + '.txt'
            with open(filepath, 'w') as f:
                for sentence in content:
                    f.write(sentence)
            content_list = [title, href]
            output_list.append(content_list)
            print(len(output_list))
            print(title, href)
            print('\n')
        except Exception as e:
            print(e)

def chinanewstw(url, output_list):
    '''
    :param url: 待爬取的url
    :param output_list: 输出list
    '''
    driver = webdriver.Chrome()
    Get_content(driver, url, output_list)
    driver.close()

url = 'http://channel.chinanews.com/cns/cl/tw-lahd.shtml?pager=1'
output_list = []
chinanewstw(url, output_list)
print(output_list)