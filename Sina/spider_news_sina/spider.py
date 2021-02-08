# -*- coding: utf-8 -*-
# 爬虫新浪滚动新闻的url
from selenium import webdriver
from article_spider import *
import re

def get_pages(driver,url):
    '''
    :param driver: Webdriver页面
    :param url: 指定日期的链接
    :return page_num: 指定日期内页面的数量
    '''
    start_url = url + '1'
    driver.get(start_url)
    time.sleep(2)
    driver.refresh()
    time.sleep(2)
    page_html = driver.page_source
    pagelist = re.findall('onclick="newsList.page.goTo(.*?);return false', page_html, re.S)
    pattern = re.compile('\d+')  # 获取页码数
    page_num = pattern.findall(pagelist[len(pagelist)-1])[0]
    return (page_num)

def Get_content(driver,page_num,url,output_list,date):
    '''
    :param driver: Webdriver页面
    :param page_num: 指定日期内页面的数量
    :param url: 指定日期的链接
    :param output_list: 输出list 
    :param date: 指定日期
    '''
    k = 1
    while k <= int(page_num):
        driver.get(url + str(k))
        time.sleep(2.5)
        driver.refresh()
        for i in range(1, 11):
            for j in range(1, 6):
                #try:
                classfy_cn = driver.find_element_by_xpath(
                    '//*[@id="d_list"]/ul[' + str(i) + ']/li[' + str(j) + ']/span[1]').text
                    #//*[@id="d_list"]/ul[1]/li[1]/span[1]  #新浪滚动新闻
                    #//*[@id="content_right"]/div[3]/ul/li[1]/div[1]/a  #中国新闻网滚动新闻
                    #//*[@id="content_right"]/div[3]/ul/li[3]/div[1]/a
                    #//*[@id="content_right"]/div[3]/ul/li[4]/div[1]/a
                    #//*[@id="content_right"]/div[3]/ul/li[9]/div[1]/a
                #classfy_cn = '其他'
                title = driver.find_element_by_xpath(
                    '//*[@id="d_list"]/ul[' + str(i) + ']/li[' + str(j) + ']/span[2]/a').text
                    #//*[@id="d_list"]/ul[1]/li[1]/span[2]/a  #新浪滚动新闻
                    #//*[@id="content_right"]/div[3]/ul/li[1]/div[2]/a  #中国新闻网滚动新闻
                href = driver.find_element_by_xpath(
                    '//*[@id="d_list"]/ul[' + str(i) + ']/li[' + str(j) + ']/span[2]/a').get_attribute('href')
                    #//*[@id="d_list"]/ul[1]/li[1]/span[2]/a  #新浪滚动新闻
                    #//*[@id="content_right"]/div[3]/ul/li[1]/div[2]/a  #中国新闻网滚动新闻
                times = driver.find_element_by_xpath(
                    '//*[@id="d_list"]/ul[' + str(i) + ']/li[' + str(j) + ']/span[3]').text
                    #//*[@id="content_right"]/div[3]/ul/li[1]/div[3]
                pubtime = times.split(" ")[1]
                # content, classfy_en = get_article(href)
                print(href)
                # content_list = [classfy_cn, classfy_en, date, pubtime, title, href, content]
                #nonlocal content_list
                #except Exception as e:
                    #pass
                # test = '/Users/steven/Downloads/test/' + title + '.txt'
                # with open(test, 'w') as f:
                #     for content_list_element in content_list:
                #         f.write(content_list_element)
                # output_list.append(content_list)
                # print(len(output_list))
        k = k + 1

def sina(url,output_list,date):
    '''
    :param url: 待爬取的url
    :param output_list: 输出list
    :param date: 日期
    :return:
    '''
    driver = webdriver.Chrome()
    page_num = get_pages(driver, url)
    Get_content(driver, page_num, url, output_list, date)
    driver.close()

output_list = []
sina('http://roll.news.sina.com.cn/s/channel.php?ch=01#col=89&spec=&type=&date={}&ch=01&k=&offset_page=0&offset_num=0&num=60&asc=&page=',output_list,2018-4-3)