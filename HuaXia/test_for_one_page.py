from bs4 import BeautifulSoup
from user_agents import agents
import requests
import time
import random
import re

# url = 'http://www.huaxia.com/lasd/twdsj/2018/07/5814893.html' # 2018.6
# url = 'http://www.huaxia.com/lasd/twdsj/2018/11/5933802.html' # 2018.10
# url = 'http://www.huaxia.com/lasd/twdsj/2013/11/3611791.html' # 2013.10
# url = 'http://www.huaxia.com/lasd/twdsj/2011/11/2643834.html' # 2011.11
# url = 'http://www.huaxia.com/lasd/twdsj/2014/08/4044336.html' #2014.7
# url = 'http://www.huaxia.com/lasd/twdsj/2012/10/3029551.html' # 2012.8
# url = 'http://www.huaxia.com/lasd/twdsj/2012/11/3099900.html' # 2012.10
# url = 'http://www.huaxia.com/lasd/twdsj/2005/08/473453.html' # 2003.9
url = 'http://www.huaxia.com/lasd/twdsj/2009/01/1290043.html' # 2009.1

agent = random.choice(agents)
header = {'User-Agent': agent}
res = requests.get(url, headers=header)
res.encoding = 'gb2312'
#print(res)
time.sleep(2)
soup = BeautifulSoup(res.text, 'html.parser')
newsArticle = soup.select('.px14')
# print(newsArticle[0])
# test = re.sub('<[^>]+>', '', newsArticle[0])
# print(test)
res_disks = []
res = []
for item in (str(newsArticle[0]).split('<b>')):
    dr = re.compile(r'<[^>]+>', re.S)
    dd = dr.sub('', item)
    art = (''.join(dd.split()))
    print(art)
#     if art:
#         res.append(art)
# print(newsArticle[0])
# print('\n')
# for item in (str(newsArticle[0]).split('<b>')):
#     # print(item)
#     new_item = item.split('</b>')
#     # print(len(item.split('</strong>')))
#     # print(new_item)
#     if len(new_item) > 1:
#         for new_item_elem in new_item:
#             # new_item_elem = re.sub('<[^>]+>', '', new_item_elem)
#             new_item[0] = re.sub('<[^>]+>', '', new_item[0])
#             new_item[1] = re.sub('<[^>]+>', '', new_item[1])
#             # new_item_elem = ''.join(new_item_elem.split())
#             new_item[0] = ''.join(new_item[0].split())
#             new_item[1] = ''.join(new_item[1].split())
#         print(new_item)
        # if new_item[0]:

        #     #***************     b     *************
        #     if new_item[0][-1] == '：':
        #         new_item[0] = new_item[0][:-1]
        #     if new_item[0].isdigit():
        #         new_item[0] += '日'
        #     #print(new_item)

        #     #***************  strong  ***************
        #     # text = re.sub('[\u4E00-\u9FA5]', ' ', new_item[0][:-1]).split(' ')
        #     # print(text)
        #     # if len(text) == 2:
        #     #     new_item[0] = text[1] + '日'
        #     # else:
        #     #     new_item[0] = text[0] + '日'
        # # print(new_item)
        # res_disks.append(new_item)
        # print(res_disks)


#*****************************    b    ******************************
# test_lists = []
# i = -1
# for res_disk in res_disks:
#     if not res_disk[1]:
#         test_lists.append(res_disk)
#         i += 1
#     else:
#         test_lists[i][1] += res_disk[1]
# for test_list in test_lists:
#     print(test_list)
# for test_list in test_lists:
#     title = '/Users/steven/Documents/算文解字/爬虫/HuaXia/test/' + test_list[0] + '.txt'
#     with open(title ,'w') as f:
#         f.write(test_list[1])


#*****************************  strong  *****************************
# test_lists = []
# i = -1
# for res_disk in res_disks:
#     if res_disk[0]:
#         test_lists.append(res_disk)
#         i += 1
#     else:
#         test_lists[i][1] += res_disk[1]

# for test_list in test_lists:
#     title = '/Users/steven/Documents/算文解字/爬虫/HuaXia/test/' + test_list[0] + '.txt'
#     with open(title ,'w') as f:
#         f.write(test_list[1])