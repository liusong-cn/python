# coding: utf-8
# @auther: 11411
# @date: 2022/7/12
# @desc:

import base64

import execjs
import requests
import time
import gzip
from requests_toolbelt import MultipartEncoder


def login(user: str, password: str):
    tm = int(time.time() * 1000)
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
    with open('wd.js', 'r', encoding='utf-8')as f:
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
    print(r.text)
    # 字典cookie
    cookies = requests.utils.dict_from_cookiejar(r.cookies)
    cookie_str = '';
    for key,value in cookies.items():
        cookie_str = cookie_str + ';' + key + "=" + value;
    cookie_str = cookie_str[1:]
    print(cookie_str)
    return cookies;

def create_order(cookies: dict):
    param = {"channel":"bjh5","source_id":"88208fe618827991903857fece63c546","q_pv_id":"12b4000001829fd82bb30a20c4bd38d9","biz_type":1,"buyer":{"buyer_id":"1429671525","eat_in_table_name":""},"shop_list":[{"shop_id":"1733124914","f_shop_id":"","sup_id":"","item_list":[{"item_id":"4746057450","quantity":1,"item_sku_id":"0","ori_price":"49.00","price":"49.00","extend":{},"price_type":1,"discount_list":[],"item_convey_info":{}}],"order_type":3,"ori_price":"49.00","price":"49.00","express_fee":"0.00","discount_list":[],"invalid_item_list":[]}],"deliver_type":0,"is_no_ship_addr":1,"total_pay_price":"49.00","total_vjifen":"","wfr":"","appid":"","discount_list":[],"invalid_shop_list":[],"pay_type":0}
    context = {"shopping_center":"1733124914"}
    # 加密参数
    udc = 'H4sIAAAAAAAAA%2BVVC9ojKQi8EvJSj%2BPzFHP4LeieyfybvcEmXyc2IFJFqVTbInx2%2FPD7EJV76F%2Bf1WXd9JWWf816ub72ms8Uumupd8PkDmvXVuS6T%2B6q2%2FTKV0rqRUs5zy9zY9mlITtqaKLbbx3efeFb%2BIrxEbi46YL1VKtNJpMWP66V%2FcKqTOIRl57jiEGcwGp452qZT%2FmiItYiJk0P98hSqRJ8ZtXNWaf3qrGqiFRkFOSNtac2Ax5dvDjiu0%2BP3DFLML6ZTbxlRRu%2BKwX1aFb%2F%2B6FA55zVYLaJF3cvmNN%2FrvnhCgUSb2rUadCkVS4iqk0%2FeO1zL9l1tz32OuXU0884swBj1BB5PdY4prUDp9Uatqrho%2FFwCD%2BqycqOX7ofToAHnUY%2FWM3Dj77Q1Kw3ZmkLzvCGvFT%2FsqPv5FrM1fRoB9QGb0dP1BvwIoqOclTmNfqcTMQYdYPlg1XgrcEsKq3%2B6sFQs0QGjKcH07GmIvpj1ej8i9ATQfignIy6iS1yBsIScag87A9bMQuNDk3BprTU4CEPpDvQGVgBMkFuDzw5rwBfKMGg3IKEqAz%2BsIQW%2FfUnhgdplQLtQJcjEUQd%2FYuDERHwbsTNwJDWnqwvZA02s7%2B0v225CyzRTWTsiTZib74ffEv0%2FmvVrrPGjoEtuwX0YGElbmxpLYAMfaGvqlYKdFMyd3%2F%2BfX9l9IhJdqGwfLu5uiRLTx0W%2FALxCdZDT6G6WL92xFyLpgT%2BwHpTw%2F0%2FasdxY%2BgOdisYN3orC0ZS2YiP0aOU79lqobfUJkYnGEW%2FOLSR%2B6RlvBLUHXOC068c2GnZCQN79uXFGYIsgZ4fvRFoRZ7Yq0LVQg3k%2FtbbfCdLceplVhwH48cZQ88ZA2WDL3zrc65ozBc%2Bdf5PT8%2BWKBR6l2Q0dsGPewVMtlSu6Idd%2B9SDi4ixPiHbw3GNs1gmvZde43aH3Atw3Al3GQ7WGFm%2F86TNBq07Y1RprnNiNNaYHDZeg%2BqQZ1S4xmjOLV3Cu%2Fo9u0W%2BuxMJpr6rhoVHKTTMho3BQ404HtI%2F3yWLWFCbVlwdhyke3LTFyvsIIwVpUxpdzsWFDTUz7pSLA9svUlxsH6xoc%2FEvEv5zHf16i7Be9z8jcTCtRQgAAA%3D%3D'
    param_data = 'param={}&context={}&udc={}'.format(param,context,udc)
    r = requests.post('https://thor.weidian.com/vbuy/CreateOrder/1.0',cookies=cookies,data=param_data,headers={'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'})
    print(r.text)

if __name__ == '__main__':
    cookie_dict = login('18349220243', 'lhs22@ri')
    # create_order(cookie_dict)
