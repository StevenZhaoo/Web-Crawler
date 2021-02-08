# -*- coding: utf-8 -*-

from selenium import webdriver
from article_spider import *

def Set_page(url_org):
    url_list = []
    try:
        for i in range(11, 17):
            url = url_org[0] + str(20*i) +  url_org[1]
            url_list.append(url)
    except Exception as e:
        print(e)
    return url_list

def Get_content(driver,url,output_list):
    '''
    :param driver: Webdriver页面
    :param url: 指定日期的链接
    :param output_list: 输出list
    '''
    driver.get(url)
    time.sleep(2.5)
    driver.refresh()
    for j in range(1, 20):
        try:
            title = driver.find_element_by_xpath(
                '//*[@id="main-content"]/div/div/div[2]/div/div[' + str(j) + ']/div[1]/p/a').text
            href = driver.find_element_by_xpath(
                '//*[@id="main-content"]/div/div/div[2]/div/div[' + str(j) + ']/div[1]/p/a').get_attribute('href')
            classfy_en, content = get_article(href)
            content_list = [classfy_en, title, href, content]
        except Exception:
            title = driver.find_element_by_xpath(
                '//*[@id="main-content"]/div/div/div[2]/div/div[' + str(j) + ']/div[2]/p/a').text
            href = driver.find_element_by_xpath(
                '//*[@id="main-content"]/div/div/div[2]/div/div[' + str(j) + ']/div[2]/p/a').get_attribute('href')
            classfy_en, content = get_article(href)
            content_list = [classfy_en, title, href, content]
        except Exception as e:
            print(e)

        test = '/Users/steven/Documents/算文解字/爬虫/WPost/WPost_result/' + title + '.txt'
        with open(test, 'w') as f:
            for content_list_element in content_list:
                f.write(content_list_element)
                f.write('\n\n')
        output_list.append(content_list)
        print(len(output_list))
        print(title, href)
        print('\n')


def washingtonpost(url_org,output_list):
    '''
    :param url_org: 待爬取的url
    :param output_list: 输出list
    '''
    driver = webdriver.Chrome()
    url_list = Set_page(url_org)
    for url in url_list:
        try:
            print(url)
            Get_content(driver, url, output_list)
        except Exception as e:
            print(e)
    driver.close()