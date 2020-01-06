import requests
import json

# Request URL: https://music.163.com/weapi/cloudsearch/get/web?csrf_token=
# Request Method: POST
url = 'https://music.163.com/weapi/cloudsearch/get/web?csrf_token='
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
#'params': 'b9v9eZseYhH2aUzxthwUFOLYIFZCw/D6wb5A050irvQAcONqOmvAQzMlqHwdy/gwzmiJCSHnpnIEuYmJ37CJmNX+PB+rZc0V+wqhc/5VNoj63L61xaYHKCo42ftXrFRqgXYGr72wl+SrlkdIbfOi496M2X8V8AFLiV6XisCKwtVuswz7U21kPHTiqYgAp3eILltZBZBvURryG8woRnOhAcZxsVI+SeRKxFirFpywJdmsRujQd36EKTbrccLxFDcWTwhKMDXqfcT4sjNKcSzcKQtk/4RSJmJ2RctBYY7VOJFCAYxZPcjTsNkh8AaHmSOb',
#'encSecKey': '503473307c750c6c278c5a4ad368156038171060ea092e2fb63e864761feedfcb989d4553e65abc185ec6b87cfd8e9f79db44037b63941e2f31e2b31fed4d326a1e64a10eaf1e8aee6704984a0ef6a5e08130a8313814b9d8176a86f8b39b10a7e49b3d0ea5d482aa38ba60d4140344861f53b3cb0bada8fa88cfee7c2cefda3'}

data = {
    'params': 'gaZAfJbEYDZGAwHSjq/g5yv4C2k22TclVDDyMuU4haIWJtyHT4bFLISx9SLpJJK9JX5bpeJIxE6wfg1z1fWNHTl2DXbSQVM9IJeSyJVClMo=',
    'encSecKey': '59a4424dc6f1ee91f075881fb11a60b196855217f9c08ee4a47880a74ba50dea38265d89711875ae2ebf0771b97c044c1f24ff1d063edfd8562a1d0f5f25c1ae63e17cbeebbb68bb2c712a02661c20bdb49f3f3e11fc355172f039ac3cede1a1b920bd0cad79f705cd37eb7a0b8cc2e45ccedeb0b1dfbc56d7b04f4e51dee99b'}
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


if __name__ == '__main__':
    download_music()
