import requests
from bs4 import BeautifulSoup as bs


# Get_original(url,cookie,file_path)
def get_content(content_url):
    '''
    :param content_url:
    :return:
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'}
    timeout = 5
    html = requests.get(content_url, headers=headers, timeout=timeout)
    soup = bs(html.text, 'lxml')
    content = data_process(soup.select('.content')[0].get_text())
    stats_vote = soup.select('.stats-vote')[0].get_text().split()[0]
    return stats_vote,content


def data_process(content):
    return ''.join(content.split())

if __name__ == '__main__':
    url = 'https://www.qiushibaike.com/article/121094787'
    get_content(url)


