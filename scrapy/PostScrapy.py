import requests as r
import json as j
#post方式爬虫目前成功，但是返回的结果说是错误的
def get_translate_result():
    # url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    url = 'http://192.168.1.109:8080/fd-offline/testExecuteController.do?testRecorddatagrid&schemeId=4028ab816b0cedfc016b0d068398003e'
    # form_data = {'i': word,
    #              'from': 'AUTO',
    #              'to': 'AUTO',
    #              'smartresult': 'dict',
    #              'client': 'fanyideskweb',
    #              'salt': '15597189077612',
    #              'sign': '7e1a8bbfd732f26b7d0fcf522e2db756',
    #              'ts': '1559718907761',
    #              'bv': 'ab57a166e6a56368c9f95952de6192b5',
    #              'doctype': 'json',
    #              'version': '2.1',
    #              'keyfrom': 'fanyi.web',
    #              'action': 'FY_BY_CLICKBUTTION'}
    form_data = {'page':1,'rows':10}
    result = r.post(url,data=form_data)
    print(result.text)
    # result.encoding = 'utf-8'
    # t = j.loads(result.text)
    # print(t)
if __name__ == '__main__':
    get_translate_result()
