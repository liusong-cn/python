# -*- coding:utf-8 -*-
# @auther: ls
# @date: 2021/10/14
import requests as r
import json

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'Content-Type': 'application/json;charset=UTF-8'}
cookies = {'thor': '8C5FA384A6D8769551E6B4B95C0F8BF68F2937CF2285203F8F323134F125A372C13711B2F22AC7BB1F7B18AAD15B3E60D63'
                   'F474DB2D27DAB2A82C60A9F9C2A4639B12CF04C8D978B498E508081F03C49F525D5C933BF678FF6946497BCD89650F87D2F242'
                   'AADE66171763A659A7BFC222090DB5A8DFBC1EEE13DD8CFF0C227D86E1280722CA9E6437E784CFD822D442D73546156EC8FF62A8B6217D8367032A1'}
url = 'http://xx/mkt/api/label/options/pin-count'
skus = '100018635576,3195185,100007618984,100014608268,100012354238'

response = r.get(url=url, headers=header, cookies=cookies)


def pin_count(sku: list = [100018635576, 3195185, 100007618984, 100014608268, 100012354238], ge: int = 1) -> int:
    """
    人群预估
    :return:
    """
    sku_condition = {'sku': ','.join(str(x) for x in sku), 'gte': str(ge)}
    label_condition = {'labelId': 34, 'labelOptionType': 5, 'operate': "INTSCT",
                       'value': str(sku_condition)}
    condition_list = []
    condition_list.append(label_condition)
    # print(condition_list)
    json_str = json.dumps(label_condition)
    # print(json_str)
    response = r.post(url, headers=header, cookies=cookies, json=condition_list)
    print(response.text)
    result = json.loads(response.text)
    if (result['data'] is not None):
        print(result['data'])


def build_condition(sku: list = None) -> dict:
    gtes = [i for i in range(1, 10)]
    if sku is None:
        return
    if isinstance(sku, list):
        skus = list(sku)
        skus_half = [j for j in skus if skus.index(j) < len(skus)/2 - 1]
        print(skus_half)


if __name__ == '__main__':
    # pin_count()
    build_condition([1,2,3,4,5,6,7,8,9])
