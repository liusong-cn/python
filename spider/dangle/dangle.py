# coding: utf-8
# @auther: ichigo
# @date: 2023-04-05
# @desc:
import execjs

class Dangle:
    """
    当乐登录
    """

    def __init__(self):
        pass

    def encryptPwd(self,pwd):
        with open('dangle.js','r',encoding='utf-8') as f:
            content = f.read()
        encrypted_pwd = execjs.compile(content).call('rsa',pwd)
        print(encrypted_pwd)

if __name__ == '__main__':
    d = Dangle()
    d.encryptPwd('123')