import random
import re
import time

import requests
from bs4 import BeautifulSoup

from user_agents import agents


def spider(url):
    '''
    :param url: 华夏经纬网主索引页
    '''
    agent = random.choice(agents)
    header = {'User-Agent': agent}
    res = requests.get(url, headers=header)
    res.encoding = 'gb2312'  # 网页编码格式为gb2312
    time.sleep(2)
    soup = BeautifulSoup(res.text, 'html.parser')
    newsArticle_href = soup.select('.A002')  # 爬取正文类别class=A002
    # total = []
    for href in newsArticle_href:
        new_url = 'http://www.huaxia.com' + href.get('href')
        formal_title = href.get_text()  # eg.:2018年10月
        get_content(new_url, formal_title)


def get_content(url, formal_title):
    '''
    :param url: 华夏经纬网月份索引页
    :param formal_title: 年月名称
    '''
    agent = random.choice(agents)
    header = {'User-Agent': agent}
    res = requests.get(url, headers=header)
    res.encoding = 'gb2312'  # 网页编码格式为gb2312
    time.sleep(2)
    soup = BeautifulSoup(res.text, 'html.parser')
    newsArticle = soup.select('.px14')  # 爬取正文类别class=px14
    res_disks = []

    for item in (str(newsArticle[0]).split('<strong>')):
        new_item = item.split('</strong>')
        if len(new_item) > 1:  # 正文页面格式用<strong>分割
            new_item[1] = re.sub('<[^>]+>', '', new_item[1])  # 正文去标签
            new_item[0] = re.sub('<[^>]+>', '', new_item[0])  # 日期去标签
            new_item[1] = ''.join(new_item[1].split())  # 正文去缩进
            new_item[0] = ''.join(new_item[0].split())  # 日期去缩进
            if new_item[0]:
                if new_item[0][-1] == '：':  # 去掉部分日期后的中文冒号
                    new_item[0] = new_item[0][:-1]
                text = re.sub('[\u4E00-\u9FA5]', ' ', new_item[0]
                              [:-1]).split(' ')  # 去掉部分日期中带月的部分
                if len(text) == 2:
                    new_item[0] = text[1] + '日'
                else:
                    new_item[0] = text[0] + '日'
                res_disks.append(new_item)
            test_lists = []
            i = -1
            for res_disk in res_disks:  # 将部分日期与正文分隔开的网页内容合并到一起
                if res_disk[0]:
                    test_lists.append(res_disk)
                    i += 1
                else:
                    test_lists[i][1] += res_disk[1]
            for test_list in test_lists:
                title = '/Users/steven/File/算文解字/爬虫/HuaXia/test/' + \
                    formal_title + test_list[0] + '.txt'
                with open(title, 'w') as f:
                    f.write(test_list[1])
        else:
            for item in (str(newsArticle[0]).split('<b>')):  # 正文页面格式用<b>分割
                new_item = item.split('</b>')
                if len(new_item) > 1:
                    for new_item_elem in new_item:
                        new_item[0] = re.sub(
                            '<[^>]+>', '', new_item[0])  # 日期去标签
                        new_item[1] = re.sub(
                            '<[^>]+>', '', new_item[1])  # 正文去标签
                        new_item[0] = ''.join(new_item[0].split())  # 日期去缩进
                        new_item[1] = ''.join(new_item[1].split())  # 正文去缩进
                    if new_item[0]:
                        if new_item[0][-1] == '：':  # 去掉部分日期后的中文冒号
                            new_item[0] = new_item[0][:-1]
                        if new_item[0].isdigit():  # 将部分日期中数字和“日”字分隔开的网页内容合并到一起
                            new_item[0] += '日'
                    res_disks.append(new_item)

            test_lists = []
            i = -1
            for res_disk in res_disks:  # 将部分日期与正文分隔开的网页内容合并到一起
                if not res_disk[1]:
                    test_lists.append(res_disk)
                    i += 1
                else:
                    test_lists[i][1] += res_disk[1]
            for test_list in test_lists:
                title = '/Users/steven/File/算文解字/爬虫/HuaXia/test/' + \
                    formal_title + test_list[0] + '.txt'
                with open(title, 'w') as f:
                    f.write(test_list[1])


if __name__ == '__main__':
    for i in range(1, 6):
        if i == 1:
            org_url = 'http://www.huaxia.com/lasd/twdsj/index.html'
            spider(org_url)
        else:
            org_url = 'http://www.huaxia.com/lasd/twdsj/index_{}.html'.format(i)
            spider(org_url)
