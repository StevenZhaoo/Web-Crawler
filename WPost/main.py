from spider import *

if __name__ == '__main__':
    url_org = ['https://www.washingtonpost.com/newssearch/?datefilter=60%20Days&query=Kim%20Trump%20Summit&sort=Date&startat=', '&utm_term=.b20018c927ef&spellcheck#top']
    while True:
        output_list = []
        washingtonpost(url_org,output_list)