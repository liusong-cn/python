import requests as r
#首次利用python爬取网页数据，get方式爬取
url = 'http://news.sina.com.cn/s/2019-06-05/doc-ihvhiews6901394.shtml'
html = r.get(url)
html.encoding='utf-8'
print(html.text)