from selenium import webdriver
import re
import time
import calendar
import re
import codecs
from data_helper import *

def count_days(year, month):
    cal = calendar.monthrange(year, month)
    pattern = re.compile(r'\d+')
    days = pattern.findall(str(cal))[1]
    return days

def month_sub(year,month):
    if month > 10:
        month -= 1
        month = str(month)
    elif month <= 10 and month > 1 :
        month -= 1
        month = '0'+str(month)
    else:
        year -= 1
        month = 12
    return year,month

def date_sub(year,month,day):
    if day > 10:
        day -= 1
        day = str(day)
    elif day <= 10 and day > 1:
        day -= 1
        day = '0'+str(day)
    else:
        year, month = month_sub(int(year),int(month))
        days = count_days(year, int(month))
        day = days
    date = str(year)+'-'+str(month) +'-'+str(day)  #新浪滚动新闻
    #date = str(year) + '//' + str(month) + str(day)  #中国新闻网滚动新闻
    return date

def date_processing():
    date_txt = "/Users/steven/Documents/算文解字/爬虫/Sina/spider_news_sina/temp/date.txt"
    last_date = txt_load(date_txt)
    date = str(last_date[0])
    year = int(date.split("-")[0])
    month = date.split("-")[1]
    day = int(date.split("-")[2])
    date = date_sub(year, month, day)
    writer = codecs.open(date_txt,'w','UTF-8')
    writer.write(date)
    writer.flush()
    return date

