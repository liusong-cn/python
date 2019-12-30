#python中模块、包名约定均小写，必要时可以加_分隔符
#类名采用驼峰命名，和java一致

import requests as r

url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
form_data = {'i': '中国',
             'from': 'AUTO',
             'to': 'AUTO',
             'smartresult': 'dict',
             'client': 'fanyideskweb',
             'salt': '15766587904033',
             'sign': '5d7a843352dc0b9d2d7cc9ff1df24e21',
             'ts': '1576658790403',
             'bv': 'ab57a166e6a56368c9f95952de6192b5',
             'doctype': 'json',
             'version': '2.1',
             'keyfrom': 'fanyi.web',
             'action': 'FY_BY_CLICKBUTTION'}

response = r.post(url,data=form_data)
print(response.text)

import json

t = json.loads(response.text)
print(t)