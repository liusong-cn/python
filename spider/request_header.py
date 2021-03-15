# 模拟使用浏览器的header
import  requests
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
# 百度首页的其中一个url
url = 'https://www.baidu.com/'
response = requests.get(url, headers=header)
print("这是添加了浏览器header:", response.content)