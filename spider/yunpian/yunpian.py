# coding=utf-8
import requests
import execjs
session = requests.session()
base_url = 'https://captcha.yunpian.com/v1/jsonp/captcha/get?'
headers ={
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
fingerprint = '7613c073d512f732c36daaf50d64e999'
origin = 'https://www.yunpian.com'
def get_captch():
    with open('yunpian_enc.js','r',encoding='utf-8') as f:
        content = f.read()
    r = execjs.compile(content).call('r')
    print(r)
    uuid = execjs.compile(content).call('getUUid')
    print(uuid)
    e = {
        'additions':{'username':None},
        'browserInfo':[{'key':'userAgent','value':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"},
                       {'key':'language','value':'zh-CN'},
                       {'key':'hardware_concurrency','value':8},
                       {'key':'resolution','value':[1440,900]},
                       {'key':'navigator_platform','value':'MacIntel'}],
        'options':{
            'hosts':'https://captcha.yunpian.com',
            'sdk':'https://www.yunpian.com/static/official/js/libs/riddler-sdk-0.2.2.js',
            'sdkBuildVersion':'1.5.0(2021111001)'
        },
        "nativeInfo":None,
        'fp':fingerprint,
        'address':origin,
        'yp_riddler_id':uuid
    }


if __name__ == '__main__':
    get_captch()