# -*- coding=utf-8 -*-
#jd检测某商品是否有货
import requests
import json
url = "https://c0.3.cn/stock?skuId=66161391733&area=22_1930_49324_52511&venderId=734943&buyNum=1&choseSuitSkuIds=&cat=9855,9858,9924&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=15399512321901596048157&ch=1&callback=jQuery1985225"
session = requests.session()
session.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/531.36",
}

def check_stock():
    r = session.get(url)
    parse_json(r.text)
    dic = parse_json(r.text)
    state = dic['stock']['StockState']
    state_name = dic['stock']['StockStateName']
    print(state,state_name)


def parse_json(str):
    begin = str.find('{')
    str = str.replace('null','\"\"')
    return json.loads(str[begin:-1])

if __name__ == "__main__":
    check_stock()