# coding=utf-8
import requests
import execjs

def login(user,password):
    url = 'https://oauth.d.cn/auth/login?'
    with open('dl.js','r',encoding='utf-8') as f:
        content = f.read()
    ctx = execjs.compile(content)
    encrypt_data = ctx.call('getEncryptedPassword',password)
    url = url + 'display=web&name=%s&pwd=%s'%(user,encrypt_data)
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'Referer':'https://oauth.d.cn/auth/goLogin.html',
        'Host':'oauth.d.cn'
    }
    res = requests.get(url=url,headers=headers)
    print(res.text)

if __name__ == '__main__':
    login('13453','fafafdd')