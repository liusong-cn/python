# coding: utf-8
# @auther: 11411
# @date: 2022/7/12
# @desc:

import base64
import datetime
import gzip
import json
import time
from urllib.parse import parse_qs
from urllib.parse import urlparse

import execjs
import requests

figureprint = {}
trace = {}


def login(user: str, password: str):
    tm = int(time.time() * 1000)
    global figureprint
    figureprint = {
        "basic": {
            "platform": "win32",
            "os": "Windows",
            "DeviceType": "desktop",
            "Browser": "Chrome 83",
            "localStorage": True,
            "sessionStorage": True
        },
        "header": {"Connection": True, "historyLength": 6},
        "navigator": {
            "numMimeTypes": 4,
            "numPlugins": 3,
            "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            "plugins": [{
                "fileName": "internal-pdf-viewer",
                "pluginName": "Chrome PDF Plugin",
                "Description": "Portable Document Format"
            },
                {
                    "fileName": "mhjfbmdgcfjbbpaeojofohoefgiehjai",
                    "pluginName": "Chrome PDF Viewer",
                    "Description": ""
                },
                {
                    "fileName": "internal-nacl-plugin",
                    "pluginName": "Native Client",
                    "Description": ""
                }],
            "language": "zh-CN",
            "vendor": "Google Inc.",
            "mimeTypes": [{
                "type": "application/pdf",
                "Description": ""
            },
                {
                    "type": "application/x-google-chrome-pdf",
                    "Description": "Portable Document Format"
                },
                {
                    "type": "application/x-nacl",
                    "Description": "Native Client Executable"
                },
                {
                    "type": "application/x-pnacl",
                    "Description": "Portable Native Client Executable"
                }],
            "appVersion": "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            "numCPU": 4,
            "hardwareConcurrency": 4,
            "appName": "Netscape",
            "appCodeName": "Mozilla",
            "cookieEnabled": True,
            "platform": "Win32",
            "product": "Gecko",
            "productSub": "20030107",
            "vendorSub": ""
        },
        "screenData": {
            "width": 1920,
            "height": 1080,
            "availWidth": 1920,
            "availHeight": 1050,
            "colorDepth": 24,
            "pixelDepth": 24,
            "devicePixelRatio": 1,
            "realWidth": 1920,
            "realHeight": 1080
        },
        "sysfonts": ["Courier", "FangSong", "Helvetica", "KaiTi", "NSimSun", "SimHei", "SimSun", "Times", "等线",
                     "Agency FB",
                     "Algerian", "Arial", "Arial Black", "Arial Narrow", "Arial Unicode MS", "Baskerville Old Face",
                     "Bauhaus 93", "Bell MT", "Berlin Sans FB", "Bernard MT Condensed", "Bodoni MT", "Bodoni MT Black",
                     "Book Antiqua", "Bookman Old Style", "Bookshelf Symbol 7", "Broadway", "Brush Script MT",
                     "Calibri",
                     "Calibri Light", "Californian FB", "Calisto MT", "Cambria", "Cambria Math", "Candara", "Castellar",
                     "Centaur", "Century", "Century Gothic", "Century Schoolbook", "Chiller", "Colonna MT",
                     "Comic Sans MS",
                     "Consolas", "Constantia", "Cooper Black", "Copperplate Gothic Light", "Corbel", "Courier New",
                     "Curlz MT", "Ebrima", "Edwardian Script ITC", "Elephant", "Engravers MT", "Felix Titling",
                     "Footlight MT Light", "Forte", "Franklin Gothic Book", "Franklin Gothic Heavy",
                     "Franklin Gothic Medium", "Freestyle Script", "French Script MT", "Gabriola", "Garamond",
                     "Georgia",
                     "Gigi", "Gill Sans MT", "Gill Sans MT Condensed", "Goudy Old Style", "Goudy Stout",
                     "Haettenschweiler",
                     "Harrington", "High Tower Text", "Impact", "Imprint MT Shadow", "Informal Roman", "Jokerman",
                     "Juice ITC", "Kristen ITC", "Kunstler Script", "Leelawadee", "Lucida Bright", "Lucida Calligraphy",
                     "Lucida Console", "Lucida Fax", "Lucida Handwriting", "Lucida Sans", "Lucida Sans Typewriter",
                     "Lucida Sans Unicode", "MS Gothic", "MS PGothic", "MS Reference Sans Serif",
                     "MS Reference Specialty",
                     "MS UI Gothic", "MT Extra", "MV Boli", "Magneto", "Maiandra GD", "Malgun Gothic", "Marlett",
                     "Matura MT Script Capitals", "Microsoft Himalaya", "Microsoft JhengHei", "Microsoft New Tai Lue",
                     "Microsoft PhagsPa", "Microsoft Sans Serif", "Microsoft Tai Le", "Microsoft Uighur",
                     "Microsoft Yi Baiti", "MingLiU-ExtB", "MingLiU_HKSCS-ExtB", "Mistral", "Modern No. 20",
                     "Mongolian Baiti", "Monotype Corsiva", "Niagara Engraved", "Niagara Solid", "Old English Text MT",
                     "Onyx", "PMingLiU-ExtB", "Palatino Linotype", "Papyrus", "Parchment", "Perpetua",
                     "Perpetua Titling MT", "Playbill", "Poor Richard", "Pristina", "Ravie", "Rockwell",
                     "Rockwell Condensed", "Segoe Print", "Segoe Script", "Segoe UI", "Segoe UI Light",
                     "Segoe UI Semibold",
                     "Segoe UI Symbol", "Showcard Gothic", "SimSun-ExtB", "Snap ITC", "Stencil", "Sylfaen", "Symbol",
                     "Tahoma", "Tempus Sans ITC", "Times New Roman", "Trebuchet MS", "Tw Cen MT", "Verdana",
                     "Viner Hand ITC", "Vivaldi", "Vladimir Script", "Webdings", "Wide Latin", "Wingdings",
                     "Wingdings 2",
                     "Wingdings 3", "仿宋", "华文中宋", "华文仿宋", "华文宋体", "华文彩云", "华文新魏", "华文楷体", "华文琥珀", "华文细黑", "华文行楷",
                     "华文隶书",
                     "宋体", "幼圆", "微软雅黑", "新宋体", "方正姚体", "方正舒体", "楷体", "隶书", "黑体"],
        "geoAndISP": {"ClientTimezoneOffset": -480},
        "browserType": {
            "isOpera": False,
            "isFirefox": False,
            "isSafari": False,
            "isIE": False,
            "isEdge": False,
            "isChrome": False,
            "isBlink": False,
            "isWebKit": True,
            "isWeixin": False,
            "isQQ": False
        },
        "performanceTiming": {
            "navigationStart": tm,
            "unloadEventStart": tm + 151,
            "unloadEventEnd": tm + 151,
            "redirectStart": 0,
            "redirectEnd": 0,
            "fetchStart": tm + 5,
            "domainLookupStart": tm + 5,
            "domainLookupEnd": tm + 5,
            "connectStart": tm + 5,
            "connectEnd": tm + 5,
            "secureConnectionStart": 0,
            "requestStart": tm + 24,
            "responseStart": tm + 76,
            "responseEnd": tm + 97,
            "domLoading": tm + 183,
            "domInteractive": tm + 1448,
            "domContentLoadedEventStart": tm + 1448,
            "domContentLoadedEventEnd": tm + 1458,
            "domComplete": 0,
            "loadEventStart": 0,
            "loadEventEnd": 0
        },
        "canvasFp": {"canvasWinding": True, "canvasData": "f4259d4bbad01352e5f53b27a609e63a"},
        "visTime": [str(tm + 3181)],
        "other": {"adblock": False, "hasLiedLanguages": False, "hasLiedResolution": False, "hasLiedOs": False}
    }
    global trace
    trace = {"keypress": True, "scroll": True, "click": True, "mousemove": True,
             "mousemoveData": [351, 382, 435, 1058, 475, 799, 249, 1060, 3365, 1837],
             "keypressData": [7620, 71730, 32135, 39145, 63830, 136075, 119610, 175895, 119605, 103730],
             "mouseclickData": [{"interval": 148930, "x1": 1273, "y1": 216, "x2": 1273, "y2": 216},
                                {"interval": 134480, "x1": 1228, "y1": 151, "x2": 1228, "y2": 151},
                                {"interval": 165580, "x1": 1286, "y1": 156, "x2": 1286, "y2": 156},
                                {"interval": 135225, "x1": 1284, "y1": 104, "x2": 1284, "y2": 104},
                                {"interval": 149315, "x1": 1243, "y1": 85, "x2": 1243, "y2": 85},
                                {"interval": 149035, "x1": 1328, "y1": 36, "x2": 1328, "y2": 36}],
             "wheelDeltaData": [-1, -1, 1, 1, 1, 1]}
    with open('wd.js', 'r', encoding='utf-8') as f:
        content = f.read()
    ctx = execjs.compile(content)
    res = ctx.call('result', figureprint) + '|' + ctx.call('result', trace) + '|' + hex(int(time.time() * 1000))[2:]
    ua = (base64.b64encode(gzip.compress(res.encode()))).decode()
    ua = "H4sIAAAAAAAAA" + ua[13:]
    data = {
        "phone": user,
        "countryCode": "86",
        "password": password,
        "version": "1",
        "subaccountId": "",
        "clientInfo": '{"clientType":1}',
        "captcha_session": "",
        "captcha_answer": "",
        "vcode": "",
        "mediaVcode": "",
        "ua": ua.replace('/', '%2F'),
    }
    headers = {
        "accept": "application/json,*/*",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "content-length": "1289",
        "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
        "origin": "https://d.weidian.com",
        "pragma": "no-cache",
        "referer": "https://d.weidian.com/weidian-pc/login/",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/83.0.4103.116Safari/537.36"
    }
    r = requests.post('https://sso.weidian.com/user/login', data=data, headers=headers)
    # 字典cookie
    cookies = requests.utils.dict_from_cookiejar(r.cookies)
    cookie_str = ''
    for key, value in cookies.items():
        cookie_str = cookie_str + ';' + key + "=" + value
    cookie_str = cookie_str[1:]
    print("cookie_str:")
    print(cookie_str)
    return cookies


def create_order(cookies: dict):
    param = '{"channel":"bjh5","source_id":"88208fe618827991903857fece63c546","q_pv_id":"16e700000182ac7acce20a20e78d0496","biz_type":1,"buyer":{"buyer_id":"1429671525","eat_in_table_name":""},"shop_list":[{"shop_id":"1733124914","f_shop_id":"","sup_id":"","item_list":[{"item_id":"4746057450","quantity":1,"item_sku_id":"0","ori_price":"49.00","price":"49.00","extend":{},"price_type":1,"discount_list":[],"item_convey_info":{}}],"order_type":3,"ori_price":"49.00","price":"49.00","express_fee":"0.00","discount_list":[],"invalid_item_list":[]}],"deliver_type":0,"is_no_ship_addr":1,"total_pay_price":"49.00","total_vjifen":"","wfr":"","appid":"","discount_list":[],"invalid_shop_list":[],"pay_type":0}'
    context = '{"shopping_center": "1733124914"}'
    # 加密参数
    # udc = 'H4sIAAAAAAAAA%2BVUiZUlIQhMSW4MR1Gj2OC39M%2FslcLaTxsFoSjobpHVMNZd%2BGtiDG3%2FjBKpcwWifK%2B03iCtmk9P7Xh1WnyOaU4b5ZuKl%2B4pUyus9r8u26AoOp9V%2BaQcSngHhhRdfmJ498JDfMR4C1ScWjjdYZEyuSn5dg32g1PlJn7tnmY7bGAnODXsOez5Qyhdxkpikrq5Xy%2FRokFnFm7OOr2H3qgiEvAo8HtjT01TXVpcfO27T7%2B%2B7y2BfJ438XyIFnRHCHj0of%2Be7Wbn%2FNDgtomTuxPu9L9j%2FubKBUu%2B2UGckYOrTgOoiIWVjZ0D0Sdv%2BGi4rRLID7kpqwD50mNsYmGonU0rWwbugHyAwxMnNSMze45ceXrr1LlLt%2B49e%2FXVdz8DwQcPGTZi1FgzZs4%2B56xCj5RWVq9R2NZatHzFyjVWrb1px%2B577NkCDB1U5jKAtaUie2AIMHHuu3VN4Kpw6BVWYKgZqkLeDXt42LDtvkxQ1d38s3u3%2BvfuS2f3xq1FSLOI2z1gh1%2Bb%2F1mp9qlUm6jmwROf6ijsXXjH%2FE97MF8WGnKrAIQG9v%2F6OsHkxfzNq%2F1Ggg%2BZEfl244fduL0ss339NJIz0UFtMKQVRDbpI5mKPYnHPPGkOKI9eTCjwZSvJC237yehxmgkHgFnVPNJJ7bxR0IKzP076juh0jbM0Mlo6PBGEfiN8a%2FHPBt54RzvisZ3Xvg2v2YhqXaGB9r6iNxf2QR704ccWSWxbq9ibEv%2F0W7PgawTn0%2F6xwNCJIP8J7MxNt2JBQAA'
    udc = get_ua()
    param_data = {
        "param": param,
        "context": context,
        "udc": udc
    }
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://weidian.com",
        "referer": "https://weidian.com/",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36"
    }
    r = requests.post('https://thor.weidian.com/vbuy/CreateOrder/1.0', data=param_data, cookies=cookies, headers=headers)
    return r.text


def get_pay_url(cookies: dict, order_info: str):
    order = json.loads(order_info)
    cashier_url = order['result']['url']
    url_parse = urlparse(url=cashier_url)
    q = parse_qs(url_parse.query)
    now = str(datetime.datetime.now().timestamp()).split('.')[0]
    param = {"ct": q['ct'][0], "token": q['token'][0], "from": "H5", "platForm": "browser", "environment": "DEFAULT",
             "appVersion": "", "orderAmount": "49.00", "isMall": 1, "entrance": "common_cashier", "instCode": "ALIPAY",
             "dbcr": "GC", "payMode": "ONLINE_BANK", "concession": True, "refreshChannel": "true",
             "clientExt": {"deviceType": "H5", "itemIds": "4746057450"}}
    param = json.dumps(param)
    data = {
        "param": param,
        "v": 1.0,
        "timestamp": now
    }
    wd_pay_url = 'https://thor.weidian.com/cashier/pay.pre/1.0'
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://weidian.com",
        "referer": "https://weidian.com/",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36"
    }
    r = requests.post(url=wd_pay_url, data=data, headers=headers, cookies=cookies)
    return json.loads(r.text)['result']['aliPay']['payUrl']


def get_ua():
    with open('wd.js', 'r', encoding='utf-8') as f:
        content = f.read()
    ctx = execjs.compile(content)
    res = ctx.call('result', figureprint) + '|' + ctx.call('result', trace) + '|' + hex(int(time.time() * 1000))[2:]
    ua = (base64.b64encode(gzip.compress(res.encode()))).decode()
    ua = "H4sIAAAAAAAAA" + ua[13:]
    return ua


# def concat_cookie():
#     cookies = {}
#     cookie_str = 'duid=1429671525;is_login=true;login_source=LOGIN_USER_SOURCE_MASTER;login_token=_EwWqqVIQgERJMy2y9sujpbW7yxojAECLzUtkV-ncN-e9ganGBZ6OUitl4yFl9QHt7YA_FVHJZHuR50jbXxTXY3omGkdC-kyAvQf4eNmi0_mFwVL3OHEXvq9UieXjEjww7GDFDOk2JgXTLxa-lK_FZfPlm3Usbi0slE-WUJUSft5FTQotYZs4I4TTQsjBN7iPztl9cz-Ks2a5NsxaJv8LXa5zc2ATvQXFoPs50jxfbdk7dLx-oEKhVUeneeyhBktgXxz8TbvC;login_type=LOGIN_USER_TYPE_MASTER;sid=1614578144;uid=1429671525;wdtoken=28b9d310'
#     for pair in cookie_str.split(';'):
#         a = pair.split('=')
#         cookies[a[0]] = a[1]
#     print(cookies)
#     return cookies

# def create_order1():
#     ua = 'H4sIAAAAAAAAA%2BVVi9njOAhsCfGSVI6eVWzxN%2BDsZv%2FzdXDJ58QGhJhhhKm2Rfjs%2BOHPRVTuoX99Vqdx01da%2FjXrZL72ms8Sumupd8PiDmvXVuS6T%2B6q2%2FTKKyX1UnY5zy%2BzDNmlITtqaKLbbx3efeFb%2BIrxEbi46YL1VKtNJpMWP66V%2FcKqTOIRl57jiEGcwGp45mqZT%2FmiItYiJk0P98hSqRJ8ZtXNWaf3qrGriFRkFOSNvac2Ax5dvDjiu0%2BP3LFKcH8zm3jLijZ8Vwrq0az%2B90WBzjmrwWoTL%2B5esKb%2F3PPLFQok3tQIfaBJq1xEVJt%2B8NjnXrLrbnvsdcqpp59xZgHGqCHyeuxxTGsHTqs1bFXDR%2BPhEH5Uk5Udv3S%2FnADPxf%2BtrObhR19oatYbq7QFZ3hCXqp%2F2dF3ci3manq0A2qDt6Mn6g14EUVHOSrzGn1OJuIedYPlg13grcEsKq3%2B0YOhZokMuJ8eTMeeiuivVaPzH4SeCMIH5WTUTWyRMxCWiEPlYX%2FYilVodGgKNqWlBg95IN2BzsAKkAlye%2BDJdQX4QgkG5RYkRGXwhyW06B9%2FYniQVinQDnQ5EkHU0V8cjIiAdyNuBoa09mR9IWuwmf2l%2FbblKbBEN5GxJ9qIvfl88C3R%2B9euXWeNEwNbdgvowcJK3DjSWgAZ%2BkJfVa0U6KZk7v78%2B35l9IhJdqGwfLq5uyRLTx0W%2FALxCdZDT6G62L92xFyLpgT%2BwHpTw%2F0%2Fase4MXQHpxWMG30qC0ZS2YiPu0cp79VqobfUJu5OMIp%2BcWgjz0nLeCWoO9YEp68cOGnZCQN79vJihiBLoOdHbwRakSfOqlC1UAO5f%2BptvpOlmHqZFeNg%2FJgx9MwYKBt84VufuaKxXvjU%2BT%2Bdni1RKPQuyWicgh%2FvFTDZUrmiX3btWw9eRIz9Cdkejuvz4qLyDOXGY9VxVDbPvy2YwpjdIz88MCX4dRmxLIC9pDpI7yCLq%2BAs2PlcuC80veKn8RQfEwP%2BFFpAxCJsOuO9QEXLtl8k%2FOd18etTyB33%2FgNovPZJ5QcAAA%3D%3D'
#     cookie = 'duid=1429671525;is_login=true;login_source=LOGIN_USER_SOURCE_MASTER;login_token=_EwWqqVIQMBr2PFIr6rM6nZs90Wd98zG8tmIhyuzf1XKKgsuvadapoedIhBC2v-Np7v8Ctc-jvMOgF2USBGWaBpC3AlbhfEX-0yf_uJRsVxPAd4sRf_JnIz0hT2vMmZAvEjQKp8zw1jHUyyRLQH-KjUuUuHhNblTZ1KvfUthAzPx6Yea4Oh4j41oF0AL8B_E4FQaNXm5Z8NH9_-Uq9eh5dsFVP1ynG0iSq21IlJRB2xb7-49JSTLqgBgIV8HnXCLtuCFIhy7X;login_type=LOGIN_USER_TYPE_MASTER;sid=1614578144;uid=1429671525;wdtoken=53e89347'
#     order_url = 'https://thor.weidian.com/vbuy/CreateOrder/1.0'
#     user_agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36'
#     headers = {
#         "Accept": "*/*",
#         "Origin": "https://weidian.com",
#         "Referer": "https://weidian.com/",
#         "Content-Type": "application/x-www-form-urlencoded",
#         "Cookie": cookie,
#         "User-Agent": user_agent
#     }
#     data = {
#         "param": '{"channel":"bjh5","source_id":"88208fe618827991903857fece63c546","q_pv_id":"16e700000182ac7acce20a20e78d0496","biz_type":1,"buyer":{"buyer_id":"1429671525","eat_in_table_name":""},"shop_list":[{"shop_id":"1733124914","f_shop_id":"","sup_id":"","item_list":[{"item_id":"4746057450","quantity":1,"item_sku_id":"0","ori_price":"49.00","price":"49.00","extend":{},"price_type":1,"discount_list":[],"item_convey_info":{}}],"order_type":3,"ori_price":"49.00","price":"49.00","express_fee":"0.00","discount_list":[],"invalid_item_list":[]}],"deliver_type":0,"is_no_ship_addr":1,"total_pay_price":"49.00","total_vjifen":"","wfr":"","appid":"","discount_list":[],"invalid_shop_list":[],"pay_type":0}',
#         "context":'{"shopping_center":"1733124914"}',
#         "udc": ua
#     }
#     r = requests.post(order_url,headers=headers,data=data)
#     print(r.text)

def flask():
    cookie_dict = login('', '')
    ali_pay_url = get_pay_url(cookie_dict, create_order(cookie_dict))
    print(ali_pay_url)
    return ali_pay_url

if __name__ == '__main__':
    cookie_dict = login('', '')
    ali_pay_url = get_pay_url(cookie_dict, create_order(cookie_dict))
    print(ali_pay_url)
