# -*- coding: utf-8 -*-

from article_spider import *
from selenium.webdriver.common.action_chains import ActionChains

def Get_content(driver, url, output_list):
    '''
    :param driver: Webdriver页面
    :param url: 指定日期的链接
    :param output_list: 输出list
    '''
    driver.get(url)
    time.sleep(5)
    # driver.refresh()
    for j in range(1, 1001):
        print(j)
        try:
            title = driver.find_element_by_xpath(
                '//*[@id="site-content"]/div/div[2]/div[2]/ol/li[' + str(j) + ']/div/div[2]/div/a/h4').text
            if title not in title_list:
                href = driver.find_element_by_xpath(
                    '//*[@id="site-content"]/div/div[2]/div[2]/ol/li[' + str(j) + ']/div/div[2]/div/a').get_attribute('href')
                content = get_article(href)
                content_list = [title, href, content]
                if title not in title_list:
                    with open('/Users/steven/File/Code/UIR-ISC/WebCrawler/NYtimes/title.txt', 'a') as title_file:
                        title_file.write(title)
                        title_file.write('\n')
                        title_file.close()
                    test = '/Users/steven/Downloads/test/' + str(j) + '.txt'
                    with open(test, 'w') as f:
                        for content_list_element in content_list:
                            f.write(content_list_element)
                            f.write('\n\n')
                    output_list.append(content_list)
                    print(len(output_list), title, href)
        except:
            click_btn = driver.find_element_by_xpath(
                '//*[@id="site-content"]/div/div[2]/div[3]/div/button')
            ActionChains(driver).click(click_btn).perform()
            time.sleep(10)

def nytimes(url, output_list):
    '''
    :param url: 待爬取的url
    :param output_list: 输出list
    '''
    driver = webdriver.Chrome()
    Get_content(driver, url, output_list)
    driver.close()

output = []
title_file = open('/Users/steven/File/Code/UIR-ISC/WebCrawler/NYtimes/title.txt', 'r')
title_list = []
try:
    titles = title_file.readlines()
    for exist_title in titles:
        title_list.append(exist_title.strip())
    print(title_list)
    title_file.close()
except:
    print('none')

nytimes('https://www.nytimes.com/search?dropmab=true&endDate=20200720&query=2020%20Election&sections=U.S.%7Cnyt%3A%2F%2Fsection%2Fa34d3d6c-c77f-5931-b951-241b4e28681c&sort=newest&startDate=20190720&types=article', output)
