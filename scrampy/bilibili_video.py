# coding=utf-8
import requests,re,os
from urllib.request import quote
from lxml import html
etree = html.etree
from multiprocessing import Pool
from ffmpy3 import FFmpeg
from prettytable import PrettyTable
order,infors = 1,[]
table = PrettyTable(['序号', 'up主', '标题', '视频时长', '投稿日期', '播放量', '试看链接'])
path='D:\爬虫视频'
path_='D:\爬虫视频\m4s文件集'
# folder=os.path.exists(path)
# if not folder:                #判断是否存在文件夹如果不存在则创建为文件夹
#     os.makedirs(path)
# os.makedirs(path_)
def data(content,page):
    global order,infors
    url='https://search.bilibili.com/all?keyword=%s&from_source=banner_search&page=%d'%(quote(content),page)
    headers={
        'Referer':'https://www.bilibili.com/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    if page==1:
        responses=etree.HTML(requests.get(url,headers=headers).content.decode('utf-8')).xpath('//*[@id="all-list"]/div[1]/div[2]/ul[2]/li')
        if responses==[]:
            responses=etree.HTML(requests.get(url,headers=headers).content.decode('utf-8')).xpath('//*[@id="all-list"]/div[1]/div[2]/ul/li')
    else:
        responses=etree.HTML(requests.get(url,headers=headers).content.decode('utf-8')).xpath('//*[@id="all-list"]/div[1]/ul/li')
    for response in responses:
        infors.append([str(order),
                       response.xpath('./div/div[3]/span[4]/a/text()')[0],
                       response.xpath('./div/div[1]/a/@title')[0],
                       response.xpath('./a/div/span[1]/text()')[0],
                       response.xpath('./div/div[3]/span[3]/text()')[0].replace('\n', '').replace(' ', ''),
                       response.xpath('./div/div[3]/span[1]/text()')[0].replace('\n','').replace(' ',''),
                       'https:'+response.xpath('./div/div[1]/a/@href')[0].split('?')[0]])
        order+=1
def make(content,page):
    #在函数内部声明global，用于函数操作在外部变量，若未定义global，则无法操作外部变量
    global table,infors
    for i in range(1, page+1):
        data(content, i)
    for i in infors:
        table.add_row(i)
    print(table)
    number=input('输入要下载的视频序号：').split('.')
    return [infors[int(i)-1][-1] for i in number]
def download(url):
    global path
    hv={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    response=requests.get(url,headers=hv).content.decode('utf-8')
    print(url)
    # 问号被重载，放在表示重复次数的元字符后，表示正则引擎在匹配‘？’前面的字符时尽量少匹配，给后面留下更多的机会，表示重复的元字符有：+ * {m,n}
    # 那么就能更多的匹配字符串，也就是贪婪模式
    #括号的意义在于存在子组，表示括号内的和前面的匹配合起来是一个匹配，但是该匹配中又有一个子组
    urls1=re.findall('"baseUrl":"(.+?)"',response)
    urls2=re.findall('"url":"(.+?)"',response)
    headers={
        'Referer':url,
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        #由于采用m4s格式后，下载的视频是分段的，其中在request.header上用range来管控单个视频的大小
        #通过设置range如下，可以直接下载完整视频
        'Range':'bytes=0-'
    }
    if urls1!=[]:
        print(url.split('/')[-1] + '开始下载!')
        with open(path_+'\%s.mp4'%(url.split('/')[-1]),'wb')as f:
            f.write(requests.get( urls1[0],headers=headers).content)
        with open(path_+'\%s.mp3'%(url.split('/')[-1]),'wb')as f:
            f.write(requests.get(urls1[-1],headers=headers).content)
        ff = FFmpeg(inputs={path_+'\%s.mp4'%(url.split('/')[-1]): None, path_+'\%s.mp3' % (url.split('/')[-1]): None},
                    outputs={path+'\%s.mp4'%(url.split('av')[-1]): '-c:v h264 -c:a ac3'})
        ff.run()
        print(url.split('/')[-1]+'下载完成!')
    else:
        print(url.split('/')[-1] + '开始下载!')
        with open(path+'\%s.flv'%(url.split('/')[-1]),'wb')as f:
            f.write(requests.get (urls2[0],headers=headers).content)
        print(url.split('/')[-1] + '下载完成!')
def start(content,page,onlymp3):
    urls=make(content,page)
    pool=Pool(processes=4)
    if onlymp3:
        pool.map(download_mp3,urls)
    else :
        pool.map(download,urls)

def download_mp3(url):
    global path
    hv = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    response = requests.get(url, headers=hv).content.decode('utf-8')
    print(url)
    # 问号被重载，放在表示重复次数的元字符后，表示正则引擎在匹配‘？’前面的字符时尽量少匹配，给后面留下更多的机会，表示重复的元字符有：+ * {m,n}
    # 那么就能更多的匹配字符串，也就是贪婪模式
    # 括号的意义在于存在子组，表示括号内的和前面的匹配合起来是一个匹配，但是该匹配中又有一个子组
    urls1 = re.findall('"baseUrl":"(.+?)"', response)
    urls2 = re.findall('"url":"(.+?)"', response)
    headers = {
        'Referer': url,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        # 由于采用m4s格式后，下载的视频是分段的，其中在request.header上用range来管控单个视频的大小
        # 通过设置range如下，可以直接下载完整视频
        'Range': 'bytes=0-'
    }
    if urls1 != []:
        print(url.split('/')[-1] + '开始下载!')
        with open(path_ + '\%s.mp3' % (url.split('/')[-1]), 'wb')as f:
            f.write(requests.get(urls1[-1], headers=headers).content)
        print(url.split('/')[-1] + '下载完成!')
    else:
        print(url.split('/')[-1] + '开始下载!')
        with open(path + '\%s.flv' % (url.split('/')[-1]), 'wb')as f:
            f.write(requests.get(urls2[0], headers=headers).content)
        print(url.split('/')[-1] + '下载完成!')


if __name__ == '__main__':
    content=input('输入内容：')
    #是否只下载MP3，否者下载video
    start(content,3,True)
