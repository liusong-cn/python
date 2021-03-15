# coding= utf-8
# author= Administrator
# date= 2021/3/15 0:18
# 模拟http超时请求
import requests
for a in range(1, 50):
    try:
        # 设置超时时间为0.1s
        response = requests.get("http://www.baidu.com", timeout = 0.1)
        print("模拟超时:", response.status_code)
    except Exception as e:
        print("异常:", str(e))