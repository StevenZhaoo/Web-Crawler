#-*- coding:utf-8 -*-

import time
from selenium import webdriver

def get_article(url):
    '''
    :param url: 指定日期的链接
    :return content: 指定url的正文内容
    '''
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)
    try:
        content = driver.find_element_by_xpath(
            '//*[@id="articleBody"]').text
        driver.close()
        return content
    except Exception as e:
        print(e)
