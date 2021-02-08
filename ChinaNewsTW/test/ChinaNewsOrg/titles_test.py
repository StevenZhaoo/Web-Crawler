import pickle
import time

import requests
from bs4 import BeautifulSoup

for i in range(1, 11):
    urls = ['http://www.chinanews.com/scroll-news/news' + str(i) + '.html']

    for url in urls:
        wb_data = requests.get(url)
        wb_data.encoding = 'gb2312'
        data_dic = {}

        soup = BeautifulSoup(wb_data.text, 'html.parser')

        titles = soup.select('#content_right > div.content_list > ul > li > div.dd_bt > a')
        title_urls = soup.select('#content_right > div.content_list > ul > li > div.dd_bt > a')
        catas = soup.select('#content_right > div.content_list > ul > li > div.dd_lm > a')
        times = soup.select('#content_right > div.content_list > ul > li > div.dd_time')

        docs = ['/Users/steven/Documents/算文解字/爬虫/Sina_test/spider_news_sina/2018_10_19/news_' + str(i) + '.txt']
        for doc in docs:
            f = open(doc, 'w')

            for title, title_url, cata, time in zip(titles, title_urls, catas, times):

                url = 'http://' + title_url.get('href').strip('//')
                new_wb_data = requests.get(url)
                new_wb_data.encoding = 'gb2312'
                soup = BeautifulSoup(new_wb_data.content, 'html5lib')
                articals = soup.select('#cont_1_1_2 > div.left_zw > p')

                data = {
                'title':title.get_text(),
                'title_url':title_url.get('href').strip('//'),
                'cata':cata.get_text(),
                'time':time.get_text()
                }

                for key in data:
                    f.write(key + ':' + data[key] + '\n')
                for artical in articals:
                    f.write(artical.get_text())
                    f.write('\n')
                f.write('\n\n\n')