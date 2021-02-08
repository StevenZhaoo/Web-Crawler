import pickle
import requests
from bs4 import BeautifulSoup

url = 'http://www.chinanews.com/gn/2018/10-18/8653065.shtml'

wb_data = requests.get(url)
wb_data.encoding = 'gb2312'
soup = BeautifulSoup(wb_data.content, 'html5lib')

#titles = soup.select('#cont_1_1_2 > h1')
#origins = soup.select('#cont_1_1_2 > div.left-time > div.left-t')
articals = soup.select('#cont_1_1_2 > div.left_zw > p')
#cont_1_1_2 > div.left_zw > p:nth-child(4)
#cont_1_1_2 > div.left_zw > p:nth-child(1)

for artical in articals:
    print(artical.get_text())