import time
from content_spider import *


def get_content_url(url):
    """
    :param url:  输入为初始url 该函数用于获取每页每一个笑话的url
    :return:
    """
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'}
    timeout = 5
    # print(url)
    html = requests.get(url, headers=headers, timeout=timeout)
    soup = bs(html.text, 'lxml')
    # 爬取用户信息
    for author in soup.select('.author'):
        if (len(author.find_all('a')))!=0:
            user_url = 'https://www.qiushibaike.com'+author.find_all('a')[0].get('href')
            user_name = author.get_text().split()[0]
            user_age = author.get_text().split()[1]
            print([user_url,user_name,user_age])
    # 爬取笑话原文
    for content in soup.select('.article'):
        content_url = 'https://www.qiushibaike.com'+content.select('.contentHerf')[0].get('href')
        time.sleep(1)
        stats_vote, content = get_content(content_url)
        print(content_url)
        print(content)
        print(stats_vote)


if __name__ == '__main__':
    page_number = 1 # 爬取多少页
    while True:
        try:
            org_url = 'https://www.qiushibaike.com/text/page/{}/'.format(page_number)   # 初始url 更改{}位置页码数即可
            get_content_url(org_url)
            # output_line(output,keywords)
            time.sleep(3)
            page_number+=1
        except Exception as e:
            print(e)