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
            '//*[@id="story"]/section').text
        driver.close()
        content_list = content.split('\n')
        result = ''
        for elem in content_list:
            if elem not in ['ADVERTISEMENT', 'Continue reading the main story', 'Unlock more free articles.', 'Create an account or log in', '___']:
                result = result + elem + '\n'
        return result
    except Exception as e:
        print(e)

# get_article('https://www.nytimes.com/aponline/2020/07/19/arts/ap-election-2020-kanye-west.html?searchResultPosition=1')
