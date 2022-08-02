import execjs


common = {
    'token': 'f325162ac64d88ce85de643b69752b47'
}

def get_sign(q):
    with open('baidufanyi_enc.js','r',encoding='utf-8') as f:
        baidu_fanyi = f.read()
    sign = execjs.compile(baidu_fanyi).call('tl',q)
    print(sign)

if __name__ == '__main__':
    get_sign('中国')