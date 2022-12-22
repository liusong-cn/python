# coding=utf-8
import re
import execjs
import requests

session = requests.session()
index_url = 'https://passport.fang.com/'
login_url = 'https://passport.fang.com/login.api'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'


def get_key_to_encode():
    headers = {"User-Agent": user_agent}
    response = session.get(url=index_url, headers=headers)
    # re.findall返回匹配字符串组，其中index=0的部分表示其各个匹配子串的tuple
    key_to_encode = re.findall(r'RSAKeyPair\((.*)\);', response.text)[0].replace('"', '').split(', ')
    return key_to_encode


def get_encrypt_pwd(n, t, i, pwd):
    with open('fangtx_enc.js', 'r') as f:
        ctx = f.read()
    r = execjs.compile(ctx).call('getEncryptCode', pwd, n, t, i)
    return r


def login(uid, pwd):
    headers = {"User-Agent": user_agent,
               'X-Requested-With': 'XMLHttpRequest',
               'Host': 'passport.fang.com',
               'Origin': 'https://passport.fang.com',
               'Referer': 'https://passport.fang.com/?backurl=http%3a%2f%2fmy.fang.com%2f',
               'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    data = {"uid": uid, "pwd": pwd, "Service": "soufun-passport-web", "AutoLogin": 1}
    r = session.post(url=login_url, headers=headers, data=data)
    print(r.text)


if __name__ == '__main__':
    keys = get_key_to_encode()
    pwd = get_encrypt_pwd(keys[0], keys[1], keys[2], 'xxx')
    login('xxx', pwd)
