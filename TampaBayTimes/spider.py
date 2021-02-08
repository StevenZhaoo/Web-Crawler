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
    time.sleep(2.5)
    # driver.refresh()
    title = ''
    content_list = []
    href = ''
    for j in range(1,10,1):
        try:

            title = driver.find_element_by_xpath(
                '//*[@id="middle"]/div[3]/div[1]/div/ol/li['+str(j)+']/div/div[1]/div[1]').text
            ex=driver.find_element_by_xpath(
                '//*[@id="middle"]/div[3]/div[1]/div/ol/li['+str(j)+']/div/div[1]/div[2]').text
            href = driver.find_element_by_xpath(
                '//*[@id="middle"]/div[3]/div[1]/div/ol/li['+str(j)+']/div/div[1]/div[1]/a').get_attribute('href')
            content = get_article(href)
            content_list = [title, ex, href, content]
        except:
            click_btn = driver.find_element_by_xpath(
                '// *[ @ id = "middle"] / div[3] / div[1] / div / div[2] / div[2]/a[last()]')
            ActionChains(driver).click(click_btn).perform()
            time.sleep(10)

        test = 'F:/大三上/爬取内容/' + title.replace(':','').replace('?','').replace('|','') + '.txt'
        with open(test, 'w',encoding='utf-8') as f:
            for content_list_element in content_list:
                f.write(content_list_element)
                f.write('\n')
        output_list.append(content_list)
        print(len(output_list))
        print(title, href)
        print('\n')


def tampabay(url, output_list):
    '''
    :param url: 待爬取的url
    :param output_list: 输出list
    '''
    driver = webdriver.Chrome()
    Get_content(driver, url, output_list)
    driver.close()

