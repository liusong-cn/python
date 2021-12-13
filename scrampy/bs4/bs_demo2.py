# coding: utf-8
# @auther: 11411
# @date: 2021/12/5
# @desc: 笔趣阁小说
import requests as re
from bs4 import BeautifulSoup
r = re.get('https://www.777zw.cc/0/761/1411988.html')
r.encoding = 'gbk'
html_doc = r.text
print(html_doc)

soup = BeautifulSoup(html_doc, 'html.parser')
# 章节名
# print(soup.h1.string)
# 内容
# print(soup.find(id='content').contents)
data = soup.find(id='content').contents
with open(r'D:\novel.txt','w', encoding='utf-8') as f:
    for d in data:
        if isinstance(d,str):
            f.write(d)