# coding=utf-8
import requests
import execjs
import json


def get_data():
    headers = {
        'host': 'jzsc.mohurd.gov.cn',
        'referer': 'https://jzsc.mohurd.gov.cn/data/company',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    url = 'https://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/list?qy_region=510100&pg=%i'%0
    encrypto_data = requests.get(url= url,headers=headers).text
    # print(encrypto_data)
    return encrypto_data



def decrytoData(d):
    with open('jzsc_enc.js','r',encoding='gbk') as f :
        decrypt_js = f.read()
    r = execjs.compile(decrypt_js).call('decrypt',d)
    return json.loads(r)

if __name__ == '__main__':
    encrypto_data = get_data()
    r = decrytoData(encrypto_data)
    print(r)
