from bs4 import BeautifulSoup
# from user_agents import agents
import requests
import time
import random
import re

# url = 'http://www.huaxia.com/lasd/twdsj/2018/07/5814893.html' # 2018.6
# url = 'http://www.huaxia.com/lasd/twdsj/2018/11/5933802.html' # 2018.10
# url = 'http://www.huaxia.com/lasd/twdsj/2013/11/3611791.html' # 2013.10
# url = 'http://www.huaxia.com/lasd/twdsj/2011/11/2643834.html' # 2011.11
url = 'http://www.huaxia.com/lasd/twdsj/2014/08/4044336.html' #2014.7
# url = 'http://www.huaxia.com/lasd/twdsj/2012/10/3029551.html' # 2012.8
# url = 'http://www.huaxia.com/lasd/twdsj/2012/11/3099900.html' # 2012.10
# url = 'http://www.huaxia.com/lasd/twdsj/2005/08/473453.html' # 2003.9
# url = 'http://www.huaxia.com/lasd/twdsj/2009/01/1290043.html' # 2009.1

# agent = random.choice(agents)
# header = {'User-Agent': agent}
res = requests.get(url)
res.encoding = 'gb2312'
#print(res)
time.sleep(2)
soup = BeautifulSoup(res.text, 'html.parser')
newsArticle = soup.select('.px14')
# print(newsArticle)
# print(newsArticle[0])
# test = re.sub(r'<[^>]+>', '', newsArticle[0])
# print(test)
res_disks = []
res = []
stop = 1
for item in (str(newsArticle[0]).split('<b>')):
    # print(item)
    dr = re.compile(r'<[^>]+>', re.S)
    dd = dr.sub('', item)
    art = (''.join(dd.split()))
    print(art)
    stop += 1
    if stop == 5:
        break