from spider import *

if __name__ == '__main__':
    for i in range(0, 21):
        url = 'http://channel.chinanews.com/cns/cl/tw-lahd.shtml?pager=' + str(i)
        output_list = []
        chinanewstw(url, output_list)