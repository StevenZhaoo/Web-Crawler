from spider import *

if __name__ == '__main__':
    for i in range(1,9,1):
        url = 'https://www.tampabay.com/search/?q=2020%20election&page='+str(i)+'&sort=date&timeframe=12|M'
        while True:
            output_list = []
            tampabay(url, output_list)
