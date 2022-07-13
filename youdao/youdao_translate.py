# coding: utf-8
# @auther: 11411
# @date: 2022/7/13
# @desc:
import requests
import hashlib
import time
import random


def translate(word):
    url = "https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    headers = {
        "User-Agent": user_agent,
        "Host": "fanyi.youdao.com",
        "Origin": "https://fanyi.youdao.com",
        "Referer": "https://fanyi.youdao.com/",
        'X-Requested-With': 'XMLHttpRequest',
        "Cookie": 'UM_distinctid=17f9da1f6845ad-043dc7b9a673f1-9771539-1fa400-17f9da1f6855db; OUTFOX_SEARCH_USER_ID=1466141461@10.110.96.160; OUTFOX_SEARCH_USER_ID_NCOO=1526403334.7897952; fanyi-ad-id=307888; fanyi-ad-closed=1; ___rl__test__cookies=1657729040285'
    }
    bv = hashlib.md5(user_agent.encode()).hexdigest()
    lts = str(int(time.time() * 1000))
    salt = lts + str(random.randint(0, 9))
    cyper = "fanyideskweb" + word + salt + "Ygy_4c=r#e#4EX^NUGUc5"
    sign = hashlib.md5(cyper.encode()).hexdigest()

    data = {
        'i': word,
        'from': "AUTO",
        'to': "AUTO",
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'lts': lts,
        'bv': bv,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }
    res = requests.post(url=url, headers=headers, data=data)
    print(res.text)


if __name__ == '__main__':
    translate("测试")
