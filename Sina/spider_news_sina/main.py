from date_helper import date_processing
from data_helper import pickle_writer
from spider import *
import time

start = time.clock()
if __name__ == '__main__':
    url_org = 'http://roll.news.sina.com.cn/s/channel.php?ch=01#col=89&spec=&type=&date={}&ch=01&k=&offset_page=0&offset_num=0&num=60&asc=&page='
    #url_org = 'http://www.chinanews.com/scroll-news/{}/news.shtml'
    while True:
        date = date_processing()  # 获取日期
        output_list = []          # 存放输出序列 list
        url = url_org.format(date) # 生成待爬取URL
        sina(url,output_list,date) # 爬虫
        #print(output_list)
        #print(len(output_list))
        #file_name = '/Users/steven/Documents/算文解字/爬虫/Sina_test/spider_news_sina/result/{}.plk'.format(date)
        #pickle_writer(output_list, file_name)  # 写入临时文件存放
end = time.clock()
print('Running:%s seconds.'%(end - start))