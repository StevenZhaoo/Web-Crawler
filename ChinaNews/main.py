from date_helper import date_processing
from data_helper import pickle_writer
from spider import *


if __name__ == '__main__':
    url_org = 'http://www.chinanews.com/scroll-news/{}/{}/news.shtml'
    date = date_processing()  # 获取日期
    output_list = []  # 存放输出序列 list
    year = date.split('-')[0]
    day_month = date.split('-')[1] + date.split('-')[2]
    url = url_org.format(year, day_month)  # 生成待爬取URL
    #print(url)
    China_News(url)  # 爬虫



