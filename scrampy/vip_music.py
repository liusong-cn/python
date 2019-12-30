import requests
import json

# Request URL: https://music.163.com/weapi/cloudsearch/get/web?csrf_token=
# Request Method: POST
url = 'https://music.163.com/weapi/cloudsearch/get/web?csrf_token='
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
data = {
    'params': 'idokQyeL84XyJfl4Lej1S/nFjDQqQCkfuEg1FgF+ktqUGAUzhdKOLGKbonS/YaHEl2B8gxKCwjq0klneLEwWDzGuoDxLcrUhlgYLIYE1ot7aO/A94sN3PO35e2jMm6C9vReYwfESX2nI18hN4ZlIg8JL9p3lPAOMJhB11+tXbdGVE1jjRi6H5VLpPpItm0ybMvp7cDGOxmXMYXcPDEOEsjl6U5Oce2OpreWK9v7bi5VAqSkoZVTsr/7rToAxWEYwhf5ikafTg4hP82xqYDhEvv2YnlFjW9Rrj1WxeVtfjCwmL4f1TAgh4P3j1lmEdkA7',
    'encSecKey': '4ce11203082e9afafa0200d00d3806be222167e2edf57236f101e5a2b9914883d4bdb227c8675ce8d084f56a01c2d0558e0afbb86ebbcb07f16a9552af34de29413c1785921497a3d93272c1477c65b3dc2550c2659e36fab608f48b7ac3712176b99f9f3d016aa46b75486688dd5da51df170da40389f004f203683920661a0'}
def get_music():
    r = requests.post(url,headers=headers,data=data)
    rjson = r.json()
    result_dict = []
    for i in rjson['result']['songs']:
        item = {}
        item['id'] = i['id']
        item['name'] = i['name']
        result_dict.append(item)
    #print(r.text)
    print(result_dict)
    return result_dict

def download_music():
    download_url = 'http://music.163.com/song/media/outer/url?id={}.mp3'
    urls = get_music()
    for i in urls:
        r = requests.get(download_url.format(i['id']),headers=headers).content
        filename = 'mp3/{}.mp3'
        with open(filename.format(i['name']),'wb') as f:
            f.write(r)


download_music()
