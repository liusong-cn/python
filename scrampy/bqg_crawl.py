
# -*- coding: utf-8 -*-
import requests as re
from bs4 import BeautifulSoup
def bqg_crawl():
    url = 'https://www.biqooge.com/43_43875/'

    r = re.get(url)
    r.encoding = 'gbk'
    text = r.text
    bs = BeautifulSoup(text, 'html_parser')
    print(bs.title)

if __name__ == '__main__':
    bqg_crawl()
    # print('中国人')