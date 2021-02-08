# -*- coding: utf-8 -*-

import time
from selenium import webdriver


def get_article(url):
    '''
    :param url: 指定日期的链接
    :return origin: 指定url新闻的原来源
    :return content: 指定url的正文内容
    '''
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2.5)
    try:
        origin = driver.find_element_by_xpath(
            '/html/body/div[5]/div[3]/div[1]/div[2]/div[1]/span[2]').text
        content = driver.find_element_by_xpath(
            '/html/body/div[5]/div[3]/div[1]/div[2]/div[2]').text
        driver.close()
        return origin, content
    except BaseException:
        origin = driver.find_element_by_xpath(
            '/html/body/div[5]/div[3]/div[1]/div[2]/div[1]/span[2]/a').text
        content = driver.find_element_by_xpath(
            '/html/body/div[5]/div[3]/div[1]/div[2]/div[2]').text
        driver.close()
        return origin, content


def Get_content(driver, url, output_list):
    '''
    :param driver: Webdriver页面
    :param url: 指定日期的链接
    :param output_list: 输出list
    '''
    driver.get(url)

    for j in range(1, 61):
        title = driver.find_element_by_xpath(
            '/html/body/div[4]/div/div[3]/ul/li[' + str(j) + ']/h3/a').text
        time = driver.find_element_by_xpath(
            '/html/body/div[4]/div/div[3]/ul/li[' + str(j) + ']/h6').text
        href = driver.find_element_by_xpath(
            '/html/body/div[4]/div/div[3]/ul/li[' + str(j) + ']/h3/a').get_attribute('href')
        origin_text, content_text = get_article(href)
        content_list = [time, title, origin_text, content_text]

        text = '/Users/steven/File/算文解字/爬虫/Huanqiu/test/' + title + '.txt'
        with open(text, 'w') as f:
            for content_list_element in content_list:
                f.write(content_list_element)
                f.write('\n')
        output_list.append(content_list)
        print(len(output_list))
        print(title, href)


def huanqiu(url, output_list):
    '''
    :param url: 待爬取的url
    :param output_list: 输出list
    '''
    driver = webdriver.Chrome()
    Get_content(driver, url, output_list)
    driver.close()


if __name__ == '__main__':
    url = 'http://taiwan.huanqiu.com/article/''.html?agt=15438'
    for i in range(1, 5):
        if i == 1:
            url = 'http://taiwan.huanqiu.com/article/index.html?agt=15438'
            output_list = []
            huanqiu(url, output_list)
        else:
            url = 'http://taiwan.huanqiu.com/article/' + \
                str(i) + '.html?agt=15438'
            output_list = []
            huanqiu(url, output_list)
