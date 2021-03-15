# coding= utf-8
# author= Administrator
# date= 2021/1/7 23:03
import requests
response = requests.get("http://www.baidu.com")
print("这是content:",response.content)
print("这是header：",response.headers)
print("这是状态码：",response.status_code)
# put请求带参
res = requests.put("http://httpbin.org/put",data={'key':"value"})
print("这是put请求的content", res.content)
