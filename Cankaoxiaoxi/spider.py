# -*- coding: utf-8 -*-

from article_spider import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

def Get_content(driver, url, output_list):
    '''
    :param driver: Webdriver页面
    :param url: 指定日期的链接
    :param output_list: 输出list
    '''
    driver.get(url)
    time.sleep(1)
    j = 1
    while j<=21:
        try:
            title = driver.find_element_by_xpath(
                '//*[@id="zuixin"]/div[' + str(j) + ']/div/h3/a').text
            href = driver.find_element_by_xpath(
                '//*[@id="zuixin"]/div[' + str(j) + ']/div/h3/a').get_attribute('href')
            content = get_article(href)
            filepath = '/Users/steven/Downloads/test/' + title + '.txt'
            with open(filepath, 'w') as f:
                f.write(title)
                f.write('\n')
                f.write(href)
                f.write('\n')
                f.write(content)
            content_list = [title, href]
            output_list.append(content_list)
            print(len(output_list))
            print(title, href)
            print('\n')
            if j == 20:
                click_btn = driver.find_element_by_xpath(
                    '//*[@id="next_page"]')
                ActionChains(driver).click(click_btn).perform()
                time.sleep(1)
                j = 1
            if j != 20:
                j += 1
        except Exception as e:
            print(e)

def cankaoxiaoxi(url, output_list):
    '''
    :param url: 待爬取的url
    :param output_list: 输出list
    '''
    driver = webdriver.Chrome()
    Get_content(driver, url, output_list)
    driver.close()

# output = []
# cankaoxiaoxi('http://tw.cankaoxiaoxi.com/', output)