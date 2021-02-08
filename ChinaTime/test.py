# -*- encoding = 'utf-8' -*-

#import pickle
#import time

import requests
from bs4 import BeautifulSoup

# for i in range(1, 11):
urls = ['https://www.chinatimes.com/cn/chinese/total?page=' + format(a) + '&chdtv' for a in range(1, 10)]
# print(urls)
for url in urls:
    print(url)
    wb_data = requests.get(url)
    # # wb_data.encoding = 'utf-8'
    print(wb_data)
    # soup = BeautifulSoup(wb_data.text, 'html.parser')
    # titles = soup.select('#page > div.wrapper > div.page_container.stack.clear-fix.chinese-news-idx > div.clear-fix > div > section > ul > li > h3 > a')
    # times = soup.select('#page > div.wrapper > div.page_container.stack.clear-fix.chinese-news-idx > div.clear-fix > div > section > ul > li > div > time > span.date')
    # links = soup.select('#page > div.wrapper > div.page_container.stack.clear-fix.chinese-news-idx > div.clear-fix > div > section > ul > li > h3 > a')
    # for title, time, link in zip(titles, times, links):
    #
    #     url = 'https://www.chinatimes.com' + link.get('href')
    #
    #     new_wb_data = requests.get(url)
    #     new_wb_data.encoding = 'utf-8'
    #     soup = BeautifulSoup(new_wb_data.content, 'lxml')
    #     articles = soup.select('#page > div.wrapper > section > div > div.contentbox.clear-fix > div > div.clummbox.clear-fix > article > p')
    #
    #     data = {
    #         'title':title.get_text().strip('\r\n '),
    #         'time':time.get_text(),
    #         'link':'https://www.chinatimes.com' + link.get('href')
    #     }
    #     test = '/Users/steven/File/算文解字/爬虫/ChinaTime/2018_10_24' + title.get_text().strip('\r\n ') + '.txt'
    #     with open(test, 'w') as f:
    #         for article in articles:
    #             f.write(article.get_text())
    #             f.write('\n')