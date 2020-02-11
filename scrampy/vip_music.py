import requests
import random
from Crypto.Cipher import AES
import base64,codecs
import execjs


# Request URL: https://music.163.com/weapi/cloudsearch/get/web?csrf_token=
# Request Method: POST
url = 'https://music.163.com/weapi/cloudsearch/get/web?csrf_token='
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
#'params': 'b9v9eZseYhH2aUzxthwUFOLYIFZCw/D6wb5A050irvQAcONqOmvAQzMlqHwdy/gwzmiJCSHnpnIEuYmJ37CJmNX+PB+rZc0V+wqhc/5VNoj63L61xaYHKCo42ftXrFRqgXYGr72wl+SrlkdIbfOi496M2X8V8AFLiV6XisCKwtVuswz7U21kPHTiqYgAp3eILltZBZBvURryG8woRnOhAcZxsVI+SeRKxFirFpywJdmsRujQd36EKTbrccLxFDcWTwhKMDXqfcT4sjNKcSzcKQtk/4RSJmJ2RctBYY7VOJFCAYxZPcjTsNkh8AaHmSOb',
#'encSecKey': '503473307c750c6c278c5a4ad368156038171060ea092e2fb63e864761feedfcb989d4553e65abc185ec6b87cfd8e9f79db44037b63941e2f31e2b31fed4d326a1e64a10eaf1e8aee6704984a0ef6a5e08130a8313814b9d8176a86f8b39b10a7e49b3d0ea5d482aa38ba60d4140344861f53b3cb0bada8fa88cfee7c2cefda3'}

data = {
    'params': 'zzgFET63LOulZAffmvgvLXko5ia9MLgww4wv12p2LaHBEViebjMI9XxW4HIm/XwSsfQqBSCYalRt50kgP5Lmk9NpB2/WKi5sFrdx19hfYz8A8E1TvXKOHRzO6vuwQ6NPWybioqw1y+Ac7OqHKbdmpOgfUKq3voUNHwtcPw6LgcIMlLEjCjIF3svU6zMK0+tGUC8stfFmqqawSwGovdIRoZGjChicBPVudoWrEDD5cAGKuC+1kPggkC449fBHlZSQnYpUVloAItgG5vm2caxAaiqD0oaS6A/fHK5T/1w4CkM=',
    'encSecKey': '6cb4d5cdd9bfc2141d46d4f08fe028ce0aeea9af28a289d24d9ca2520af9b801b0e02f85dbac66d74a64d80e7a1f95a07d6ea93709431eed6eb9c71172de5f3be398d9d03add102d917436d078542c9da04775a92014ebd0e1fb7fccbd88b497ea7d5baab7f533c25ec99ac488ffed20774e7fcb02f32bff4856183fe6d1371f'}
def get_music():
    data1 = {'params':get_params(),'encSecKey':get_encSecKey()}
    r = requests.post(url,headers=headers,data=data1)
    print(r.text)
    # rjson = r.json()
    # result_dict = []
    # for i in rjson['result']['songs']:
    #     item = {}
    #     item['id'] = i['id']
    #     item['name'] = i['name']
    #     result_dict.append(item)
    # print(result_dict)
    # return result_dict

def download_music():
    download_url = 'http://music.163.com/song/media/outer/url?id={}.mp3'
    urls = get_music()
    for i in urls:
        r = requests.get(download_url.format(i['id']),headers=headers).content
        filename = 'mp3/{}.mp3'
        with open(filename.format(i['name']),'wb') as f:
            f.write(r)

#产生16位随机数
def random16():
    content = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    i = 0
    result = ''
    while i < 16:
        a = random.randint(0,len(content)-1)
        result += content[a:a+1]
        i += 1
    # print(result)
    return result

rand = random16();



def to_16(key):
    while len(key) % 16 != 0:
        key += '\0'
    return str.encode(key)
def AES_encrypt(text, key, iv):
    bs = AES.block_size
    pad2 = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
    encryptor = AES.new(to_16(key), AES.MODE_CBC,to_16(iv))
    encrypt_aes = encryptor.encrypt(str.encode(pad2(text)))
    encrypt_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')
    return encrypt_text

def RSA_encrypt(text, pubKey, modulus):
    text=text[::-1]
    rs=int(codecs.encode(text.encode('utf-8'), 'hex_codec'), 16) ** int(pubKey, 16) % int(modulus, 16)
    return format(rs, 'x').zfill(256)

def get_params():
    # encText = str({'csrf_token':"",'limit':8,'s':'芒种'})
    encText = str({'s': '句号', 'type': 1, 'offset': 0, 'total': 'true', 'limit': 9})
    key = '0CoJUm6Qyw8W8jud'#buU9L(["爱心", "女孩", "惊恐", "大笑"])的值
    iv = "0102030405060708"  # 偏移量
    return AES_encrypt(AES_encrypt(encText,key,iv),rand1,iv)

def get_encSecKey():
    pubKey = "010001"  # buU9L(["流泪", "强"])的值
    modules = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
    text = rand1
    return RSA_encrypt(text,pubKey,modules)

#使用node.js环境执行js代码
get_i=execjs.compile(r"""
    function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
""")

rand1 = get_i.call('a',16)

if __name__ == '__main__':
    # download_music()
    get_music()
