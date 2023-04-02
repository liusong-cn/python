# coding: utf-8
# @auther: ichigo
# @date: 2023-04-02
# @desc:
import execjs


class Yunpian:
    """
    云片验证码解析
    """
    appId = "b68fba1577964dc59c10a46c142b12ac"

    fingerprint = 'a5759ab9fa1715c631b172e0824c112d'

    address = 'address'

    def __init__(self):
        with open('yunpian.js',mode='r',encoding='utf-8') as f:
            content = f.read()
        self.ctx = execjs.compile(content)

    def getAppId(self):
        return self.appId

    def getR(self):
        return self.ctx.call("r")

    def createUUID(self):
        return self.ctx.call('createUUID')

    def getRandomStr(self,length):
        return self.ctx.call('getRandomStr',length)




if __name__ == '__main__':
    yun = Yunpian()
    print(yun.getRandomStr(16))