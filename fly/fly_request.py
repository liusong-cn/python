# -*- coding:utf-8 -*-
# @auther: ls
# @date: 2021/10/14
import requests as r
import json
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
          'Content-Type': 'application/json;charset=UTF-8'}
cookies = {'thor': '8C5FA384A6D8769551E6B4B95C0F8BF68F2937CF2285203F8F323134F125A37237C1246EAC1053C2FFB9E5AB'
                   '14E3828D98D8FA3073ECAE6BBB9C01FE68F815CE22A4BC4B01DFF2C7211B424FB9587ABAF60CC340FCFAA1CBB3918FFEE2FE52F198D'
                   '066FAF2F094F311FC8ADAD09496A531ADB489079C496C91E0059B53125750D2B7A4F5D19E8EF2E6688E815CC1CC56CFC63D07DC3A6771DA14480121BCDC8D'}
url = 'http://xx/mkt/api/label/all'
response = r.get(url=url, headers=header, cookies=cookies)
print("text:", response.text)
print('状态码:', response.status_code)
json_str = json.loads(response.text)
print(json_str)
# print(json_str['state'])
# print(json_str['data'][0]['name'])
